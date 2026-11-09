# Medium RC4 — Recon

[← Overview](46-medium-rc4.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: cypera**
>
> Sebuah layanan validasi menggunakan RC4 dengan kunci yang tertanam di binary. Ciphertext flag disimpan sebagai array byte. RC4 bersifat simetris, jadi dekripsi memakai fungsi yang sama dengan enkripsi.
>
> Format: `NFX{...}`

Deskripsi sudah memberi petunjuk besar: algoritmanya RC4, key tertanam, ciphertext berupa array byte. Tantangannya adalah menemukan **di mana** key dan ciphertext berada, lalu membalik arahnya.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 | MD5 |
|---|---|---|---|
| `reverse/Medium_01_RC4/medium_rc4` | 14.472 byte | `cc8b962d1501755603febfb884c5c49b42d9814aff165ed21d9cc81cda71d0f1` | `1fc7cd71f875fb9ad48c1b4e986e5781` |

Direktori challenge hanya berisi satu binary; tidak ada source, README, atau service jaringan. Binary adalah target lokal yang membaca flag dari argumen.

### 1.3 Environment

- OS: Linux x86-64 (Ubuntu 22.04/24.04-based).
- Tool yang dipakai: `file`, `readelf`, `objdump`, `strings`, `gdb`, `python3`, `pyelftools`, `pwntools` (untuk `checksec`).
- `checksec` standalone tidak terpasang di environment ini, sehingga digunakan implementasi `ELF.checksec()` dari pwntools. Hasilnya identik dengan `checksec --file`.
- Binary dijalankan langsung; tidak perlu library atau flag tambahan.

### 1.4 Triage awal

```bash
$ file reverse/Medium_01_RC4/medium_rc4
reverse/Medium_01_RC4/medium_rc4: ELF 64-bit LSB pie executable, x86-64,
version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=8bfdd28a937fb4bafda042b415e4484687ff60a9, for GNU/Linux 3.2.0, stripped
```

```text
$ sha256sum reverse/Medium_01_RC4/medium_rc4
cc8b962d1501755603febfb884c5c49b42d9814aff165ed21d9cc81cda71d0f1  reverse/Medium_01_RC4/medium_rc4

$ md5sum reverse/Medium_01_RC4/medium_rc4
1fc7cd71f875fb9ad48c1b4e986e5781  reverse/Medium_01_RC4/medium_rc4

$ stat -c '%s bytes' reverse/Medium_01_RC4/medium_rc4
14472 bytes
```

```text
$ python3 -c "from pwn import *; print(ELF('reverse/Medium_01_RC4/medium_rc4').checksec())"
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
FORTIFY:    Enabled
SHSTK:      Enabled
IBT:        Enabled
```

```text
$ strings -n 4 reverse/Medium_01_RC4/medium_rc4
/lib64/ld-linux-x86-64.so.2
__cxa_finalize
__printf_chk
__libc_start_main
puts
strlen
memcmp
__stack_chk_fail
libc.so.6
...
Pemakaian: %s <flag>
Wrong!
n0t_s3cur3_k3y_2026
Correct! RC4 memang simetris.
...
```

**Temuan dari triage:**

1. Binary **stripped** dan **PIE**, jadi alamat di disassembly adalah offset relatif terhadap base. Untuk analisis statis ini tidak masalah karena semua referensi `rip-relative` tetap valid.
2. Ada string yang sangat mencolok: `n0t_s3cur3_k3y_2026`. Ini kandidat kuat untuk key RC4.
3. Pesan sukses menyebut RC4 secara eksplisit.
4. Binary memakai stack canary (`__stack_chk_fail`, akses `fs:0x28`) dan full RELRO, tetapi untuk challenge reversing proteksi ini tidak menghalangi analisis.
5. Argumen dibaca dari `argv[1]`, bukan stdin.

Menjalankan binary tanpa argumen:

```text
$ ./reverse/Medium_01_RC4/medium_rc4
Pemakaian: reverse/Medium_01_RC4/medium_rc4 <flag>
```

Menjalankan dengan input asal:

```text
$ ./reverse/Medium_01_RC4/medium_rc4 'NFX{wrong}'
Wrong!
```

### 1.5 Perintah akuisisi bukti

```bash
mkdir -p writeups/assets/medium-rc4
BIN=reverse/Medium_01_RC4/medium_rc4
file "$BIN"                                  >  writeups/assets/medium-rc4/01-identitas.txt
sha256sum "$BIN"                             >> writeups/assets/medium-rc4/01-identitas.txt
md5sum "$BIN"                                >> writeups/assets/medium-rc4/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  writeups/assets/medium-rc4/02-readelf.txt
strings -n 4 "$BIN"                          >  writeups/assets/medium-rc4/03-strings.txt
objdump -d -Mintel "$BIN"                    >  writeups/assets/medium-rc4/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  writeups/assets/medium-rc4/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  writeups/assets/medium-rc4/08-checksec.txt
python3 writeups/assets/medium-rc4/solve_rc4.py \
                                             | tee writeups/assets/medium-rc4/06-solver-output.txt
```
