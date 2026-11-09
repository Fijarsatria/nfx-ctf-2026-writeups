# Starved — Recon

[← Overview](40-starved.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Kesatria Baja Ringan**
>
> **Starved** adalah layanan relay kecil yang meminta nickname sebelum menerima request upload. Kode sapaan terlalu percaya pada input pengguna, dan jalur upload lebih parah lagi karena memakai ukuran yang dikirim klien.

Dua petunjuk: "kode sapaan terlalu percaya pada input pengguna" (format string di `leaker`) dan "jalur upload memakai ukuran yang dikirim klien" (stack overflow di `main`).

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/Starved/peserta/chall` | 12.856 B | `a9bf480c6deded80a4400715e92ad7d1c4d795aadafc2a6ba72b5e1b3a4c6a0e` |
| `pwn/Starved/peserta/libc.so.6` | 2.220.400 B | `b2cf6c33b74d2f22543b7a469a75b538911e690f769d0b238843a49465b83793` |
| `pwn/Starved/peserta/ld-linux-x86-64.so.2` | 240.936 B | loader Ubuntu 22.04 |

Service asli: `NFX/Starved` (TCP 41825), saat penulisan berstatus stopped. Analisis pada bundle peserta.

### 1.3 Environment

- Linux x86-64; libc bawaan challenge = Ubuntu GLIBC 2.35.
- Menjalankan dengan loader + libc challenge:
  ```bash
  cd pwn/Starved/peserta
  ./ld-linux-x86-64.so.2 --library-path . ./chall
  ```
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `pwntools`, `ROP`.

### 1.4 Triage awal

```text
$ file chall
chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=982714e3c63ad8562fde9381f959c19a31adbf02,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools)
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
Stripped:   No
```

`strings` memperlihatkan **decoy flag** yang sengaja dipasang di `.data`:

```text
flag.txt
DECOY{jangan_yang_ini_ya}
DECOY{union_gede_kecil_bebas_wkwk}
DECOY{fd0_trick_doang_kok_bisa}
```

Decoy ini bukan flag kompetisi; flag asli ada di `flags/pwn/Starved.txt`. String `DECOY{fd0_trick...}` justru menjadi petunjuk teknik exploit.

Symbol:

```text
0000000000000ba9 t setup_seccomp
0000000000000dea t leaker
0000000000000ecc T main
```
