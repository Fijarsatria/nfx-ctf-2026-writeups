# Talatah Ti Peuntas — Recon

[← Overview](41-talatah-ti-peuntas.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Amablex**
>
> Dina hiji jaringan komunikasi, aya layanan anu ngagunakeun protokol TIPC pikeun silih tukeur talatah antarbagian sistem. Hiji poé, tim kaamanan manggihan yén layanan éta miboga kalemahan nalika ngolah ukuran data tina talatah anu ditarima. Anjeun dibéri binary simulasi tina layanan komunikasi éta. Analisis kumaha program ngatur data anu asup, kumaha struktur mémori dianggo, sarta naha aya kalepatan dina prosés ngatur ukuran data. Teangan jalan pikeun ngabuktikeun yén kalemahan éta bisa mangaruhan jalanna program sarta meunangkeun flag.

Petunjuk utama: **"calepatan dina prosés ngatur ukuran data"** — panjang TLV vs ukuran alokasi.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/TalatahTiPeuntas/peserta/talatah` | 17.016 B | `1cbab0f8554ac1ec516de90b1fbbdfb957a1aa4ca49319da67499549a2cb6c86` |
| `pwn/TalatahTiPeuntas/peserta/libc.so.6` | 2.190.608 B | `85e64f97e348786a8fb4d9f3d52fec289e2fb86bba20f0731dfe61990525e0f7` |
| `pwn/TalatahTiPeuntas/peserta/ld-linux-x86-64.so.2` | 254.864 B | loader bawaan |

Service asli: `NFX/PWNNXCTF-2026/TalatahTiPeuntas` (TCP), saat penulisan stopped.

### 1.3 Environment

- Linux x86-64; libc challenge (lihat `assets/libc-offsets-and-gadgets.txt`).
- Menjalankan:
  ```bash
  cd pwn/TalatahTiPeuntas/peserta
  ./ld-linux-x86-64.so.2 --library-path . ./talatah
  ```
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `readelf`, `pwntools`.

### 1.4 Triage awal

```text
$ file talatah
talatah: ELF 64-bit LSB executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=194bc712bb4058a285ec96e5ba7850ccc995c63b,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools)
RELRO:      Partial RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        No PIE (0x400000)
FORTIFY:    Enabled
SHSTK:      Enabled
IBT:        Enabled
Stripped:   No
```

Partial RELRO + non-PIE = GOT writable dan alamat statis. `strings` menunjukkan protokol:

```text
panjang pesan :
[-] panjang pesan di luar rentang 24..%d
pesan :
[!] data pesan tidak lengkap
TLT1
[-] magic salah (harus TLT1)
[-] total_len (%u) tidak cocok dengan panjang pesan (%d)
[-] key_size di luar 1..%d
[-] tag tidak dikenal (0x%04x, harus 0x0001)
[-] tlv_len melebihi sisa pesan
msg%d
[+] pesan diparse -> node #%d (key_size=%u, tlv_len=%u)
view[%d] name=%.16s len=%u data:
panjang baru :
data :
[+] node #%d diedit (%d byte)
[+] node #%d dihapus
```

Symbol:

```text
000000000040150d t op_parse
00000000004018a7 t op_view
0000000000401982 t op_edit
0000000000401b3c t op_delete
```
