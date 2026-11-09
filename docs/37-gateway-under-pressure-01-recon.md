# Gateway Under Pressure — Recon

[← Overview](37-gateway-under-pressure.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Amablex**
>
> Sebuah perusahaan menggunakan gateway untuk menangani komunikasi antara pengguna eksternal dan infrastruktur internal. Audit menemukan bahwa salah satu komponen memiliki kelemahan saat memproses data masuk. Kamu diberikan binary simulasi komponen tersebut. Analisis bagaimana kesalahan pengelolaan memori dapat memengaruhi alur eksekusi, lalu buktikan bahwa fungsi yang tidak tersedia pada alur normal dapat dicapai.

Petunjuk "fungsi yang tidak tersedia pada alur normal" sangat sesuai dengan fungsi `release_gateway()` yang ada di symbol table tetapi tidak dipanggil dari `main()`.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/GatewayUnderPressure/peserta/gateway` | 16.976 B | `0bd3040af540e9621b12c944bb0d15a3faa74e970022a1083b3def4741d5b35f` |

Tidak ada libc/loader tambahan; binary memakai glibc host. Service asli terdaftar sebagai `NFX/PWNNXCTF-2026/GatewayUnderPressure` (TCP) di `pwn/SERVICES.md`, tetapi pada saat penulisan berstatus **stopped**; analisis dilakukan pada binary yang diberikan.

### 1.3 Environment

- Linux x86-64, glibc 2.39 (host).
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `pwntools`.
- Menjalankan lokal:
  ```bash
  cd pwn/GatewayUnderPressure/peserta
  ./gateway
  ```

### 1.4 Triage awal

```text
$ file gateway
gateway: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=c51a9a9d85c2e464c9d55029307cc32eb2484bae,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools)
RELRO:      Partial RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
SHSTK:      Enabled
IBT:        Enabled
Stripped:   No
```

`strings` langsung menunjukkan fungsi win dan path flag:

```text
=== NX GATEWAY SERVICE ===
node: gw-edge-01  |  build: 2025.11
flag.txt
[!] flag.txt tidak ditemukan di direktori kerja
FLAG: %s
session token :
[+] sesi terdaftar, dispatch diizinkan.
audit length (max %d) :
[!] audit length tidak valid
[+] audit selesai (%ld byte)
dispatch length (max %d) :
dispatch payload :
[+] dispatch diterima (%ld byte)
[1] Register session
[2] Audit memory
[3] Dispatch request
[4] Exit
[!] sesi belum terdaftar, pakai [1] dulu.
```

Symbol table:

```text
00000000000012e1 t release_gateway
00000000000013c9 t read_line
000000000000145f t read_exact
00000000000014d3 t do_register
000000000000151a t do_audit
00000000000015f5 t do_dispatch
000000000000174d T main
```

**Temuan:** `release_gateway()` adalah target ret2win; `do_audit()` dan `do_dispatch()` adalah kandidat bug.
