# Kunci Sudo Sing Kesasar — analisis binary (2026-11-13)

## Kesimpulan singkat

Binary lokal **tidak memperlihatkan jalur input yang bisa membuat
`struct->suid == 0`**. Gate sukses ada, tetapi tidak ada write yang
user-controlled ke field `suid` setelah inisialisasi. Jadi klaim "exploit
`suid==0` berhasil" **belum bisa dibuktikan dengan binary ini**.

Flag `NFX{Wh33W0kTh3Tok-k}` tetap tercatat accepted di platform, tetapi
asalnya dari service live, bukan dari exploit lokal yang bisa direproduksi.

## Binary

```text
peserta/kunci
ELF 64-bit LSB executable, x86-64, non-PIE, not stripped
```

Fungsi:

| Alamat | Fungsi | Peran |
|---:|---|---|
| `0x4012b6` | `tulis` | `write(1, s, strlen(s))` |
| `0x4012e9` | `baca_baris` | baca satu baris ke buffer, max `size-1` byte |
| `0x40136c` | `unescape_copy` | copy sambil membuang backslash |
| `0x4013fe` | `buka_kunci` | buka `flag.txt`, cetak `FLAG: %s` |
| `0x4014b6` | `main` | parser rule + gate `suid==0` |

## Alur `main`

1. `baca_baris(buf, 0x400)` — buffer stack `rbp-0x420`, ukuran `0x400`.
2. `len = strlen(buf)` (lewat `strcspn` dengan delimiter kosong).
3. `dest = malloc(len+1)`.
4. `struct = malloc(0x18)`; layout:
   - `owner[16]` di offset `0x00`
   - `uid` di offset `0x10`
   - `suid` di offset `0x14`
5. `snprintf(struct, 0x10, "%s", "user")`.
6. `struct->uid = 1000`, `struct->suid = 1000`.
7. `unescape_copy(dest, buf, len)`.
8. `strncmp(dest, "ALL", 3)`.
9. Jika `struct->suid == 0` → `buka_kunci()`.

## Kenapa tidak ada overflow

`baca_baris`:

- Loop berjalan selama `i+1 < size`; untuk `size=0x400`, maksimum
  `i=0x3fe` saat membaca.
- Setelah loop, null terminator ditulis di `buf[i]`, maksimum `buf[0x3ff]`.
- Buffer `0x400` byte; `buf[0x3ff]` masih di dalam buffer.
- Struct pointer ada di `rbp-0x20`, yaitu `buf[0x400]`. Tidak tersentuh.

`unescape_copy`:

- Menulis tepat satu byte output per iterasi, dan indeks sumber maju 1 atau 2
  (kalau ada backslash).
- Panjang output `j <= i <= len`.
- Dest berukuran `len+1`, lalu `dest[j]=0`. Tidak overflow.

Tidak ada write kedua ke `struct->uid`/`struct->suid` di seluruh binary.

## Uji lokal

Dengan `flag.txt` berisi `TESTFLAG`:

```text
$ printf 'ALL ALL=(ALL) /bin/sh\n' | ./kunci
[-] sudo ditolak: uid=1000 suid=1000 (bukan root)
```

Input panjang 16–1100 byte, termasuk 1023/1024/1025, semuanya ditolak atau
tidak mencapai `buka_kunci`. Tidak ada crash yang mengarah ke overwrite
struct.

## Kemungkinan penjelasan

1. Binary yang diunduh adalah build berbeda dari service live.
2. Service membungkus binary dengan parser/privilege lain.
3. Challenge memang menerima flag lewat jalur yang tidak ada di binary ini.

Tanpa source/build service, exploit `suid==0` **tidak bisa diklaim**.

## File

- `disasm-main.txt`
- `disasm-baca-barisy.txt`
- `disasm-unescape.txt`
- `disasm-buka-kunci.txt`
- `local-tests.txt`
