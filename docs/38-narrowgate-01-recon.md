# NarrowGate — Recon

[← Overview](38-narrowgate.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Kesatria Baja Ringan**
>
> **NarrowGate** adalah layanan pembaca block minimal dengan sandbox runtime yang ketat. Tidak semua yang terlihat sudah divalidasi benar-benar aman.
>
> Service meminta nickname, lalu meminta ukuran block, dan membaca block tersebut ke buffer stack berukuran tetap. Format string bug dan bypass validasi 16-bit sudah cukup untuk melewati gate ini.

Deskripsi hampir memberi seluruh solusi: format string, validasi 16-bit, buffer stack tetap, dan sandbox ketat (seccomp).

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/NarrowGate/peserta/narrowgate` | 16.520 B | `4b7efd66b87e6756564eedc3027a0259bb22c96fa1a75082502c29834a0afcdb` |
| `pwn/NarrowGate/peserta/libc.so.6` | 2.220.400 B | `e01b1ce7be2987f3b8560e26d0df2623f9dd5cec17be923ae28a785bc0d32d50` |
| `pwn/NarrowGate/peserta/ld-linux-x86-64.so.2` | 240.936 B | loader Ubuntu 22.04 |

Service asli: `NFX/NarrowGate` (TCP 47736), saat penulisan stopped. Analisis pada bundle peserta.

### 1.3 Environment

- Linux x86-64; libc = Ubuntu GLIBC 2.35.
- Menjalankan:
  ```bash
  cd pwn/NarrowGate/peserta
  ./ld-linux-x86-64.so.2 --library-path . ./narrowgate
  ```
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `pwntools`, `ROP`.

### 1.4 Triage awal

```text
$ file narrowgate
narrowgate: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=6da82fbc56a1760efa23c7a499c1726656314440,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools)
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
Stripped:   No
```

`strings`:

```text
name>
hello,
prctl(NO_NEW_PRIVS)
seccomp
Narrow Gate
blocks(4 bytes)>
rejected
```

Symbol:

```text
00000000000011e9 T leaker
00000000000012bc T setup_seccomp
00000000000014fd T main
```
