# Kunci Sudo Sing Kesasar — Cara Mendapatkan Flag

[← Overview](78-kunci-sudo-sing-kesasar.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.**
>
> **Flag:** `NFX{Wh33W0kTh3Tok-k}`
> **Status:** `VERIFIED`

## Binary

Binary **tersedia** di bundle publik:

```text
work/upstream/qazwsx/pwn/KunciSudoSingKesasar.zip
└── peserta/kunci   (ELF 64-bit, non-PIE, not stripped)
```

```bash
unzip -o KunciSudoSingKesasar.zip -d kunci
file kunci/peserta/kunci
readelf -h kunci/peserta/kunci | grep Type
strings -n 5 kunci/peserta/kunci | grep -iE 'flag|sudo|ALL|rule'
```

Temuan:

- `Type: EXEC` (non-PIE), not stripped.
- String: `flag.txt`, `FLAG: %s`, `sudo - penjaga aturan sudoers`,
  `format rule : ALL ALL=(ALL) CMD`, `rule : `.
- `main` membaca rule ke stack `0x400`, lalu:
  - `malloc(len+1)` untuk rule,
  - `malloc(0x18)` untuk struct `{ char owner[16]; int uid; int suid; }`,
  - `snprintf(struct, 0x10, "%s", "user")`,
  - `struct->uid = 1000`, `struct->suid = 1000`,
  - `unescape_copy(rule, buf, len)`,
  - `strncmp(rule, "ALL", 3)`,
  - jika `struct->suid == 0` → `buka_kunci()` membaca `flag.txt`.

## Reproduksi lokal

```bash
cd kunci/peserta
echo TESTFLAG > flag.txt
printf 'ALL ALL=(ALL) /bin/sh\n' | ./kunci
```

Output normal:

```text
[-] sudo ditolak: uid=1000 suid=1000 (bukan root)
```

## Kenapa `suid==0` tidak bisa dicapai dari binary ini

Gate suksesnya ada:

```text
401635: mov rax,[rbp-0x20]   ; struct
401639: mov eax,[rax+0x14]   ; struct->suid
40163c: test eax,eax
40163e: jne 401669           ; kalau != 0 -> tolak
401640: call buka_kunci
```

Tapi tidak ada write user-controlled ke `struct->suid` setelah inisialisasi
`1000`:

1. `baca_baris(buf, 0x400)`:
   - loop berjalan selama `i+1 < 0x400`, jadi maksimum `i=0x3fe`;
   - null terminator ditulis di `buf[i]`, maksimum `buf[0x3ff]`;
   - buffer `buf` berukuran `0x400`; `buf[0x3ff]` masih di dalam buffer.
2. Pointer `struct` ada di `rbp-0x20` = `buf+0x400`; tidak tersentuh input.
3. `unescape_copy(dest, buf, len)`:
   - output index `j` bertambah satu per iterasi;
   - jumlah iterasi <= `len`;
   - `dest` berukuran `len+1`, lalu `dest[j]=0`; tidak overflow.
4. Setelah `struct->uid=1000` dan `struct->suid=1000`, tidak ada assignment
   lain ke offset `0x14`.

Uji lokal dengan panjang input 16–1100 byte (termasuk 1023/1024/1025) selalu
berakhir `uid=1000 suid=1000`; tidak ada crash yang mengarah ke overwrite
struct.

Kesimpulan: **binary publik tidak memperlihatkan jalur input** untuk membuat
`suid==0`. Flag tetap diterima platform, tetapi berasal dari service live yang
mungkin memakai build berbeda. Ini sebabnya status metode tetap **PARTIAL**,
bukan diklaim FULL.

## Flag

Dari service:

```text
NFX{Wh33W0kTh3Tok-k}
```

> Catatan audit: klaim lama “memory leak, token reuse” tidak didukung binary.
> Binary dan static finding di atas adalah bukti yang bisa direproduksi.

### Evidence langkah ini

![00b-terminal-evidence.png](assets/kunci-sudo-sing-kesasar/00b-terminal-evidence.png)

*Terminal evidence (arsip/log asli) — `00b-terminal-evidence.png`.*
