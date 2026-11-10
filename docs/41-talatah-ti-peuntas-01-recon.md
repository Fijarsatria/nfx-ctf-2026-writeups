# Talatah Ti Peuntas — Recon

[← Overview](41-talatah-ti-peuntas.md) · [Index](index.md)

## 1.1 Deskripsi challenge

> **Author: Amablex**
>
> Dina hiji jaringan komunikasi, aya layanan anu ngagunakeun protokol TIPC pikeun silih tukeur talatah antarbagian sistem. Hiji poé, tim kaamanan manggihan yén layanan éta miboga kalemahan nalika ngolah ukuran data tina talatah anu ditarima. Anjeun dibéri binary simulasi tina layanan komunikasi éta. Analisis kumaha program ngatur data anu asup, kumaha struktur mémori dianggo, sarta naha aya kalepatan dina prosés ngatur ukuran data. Teangan jalan pikeun ngabuktikeun yén kalemahan éta bisa mangaruhan jalanna program sarta meunangkeun flag.

Petunjuk utama: **"calepatan dina prosés ngatur ukuran data"** — panjang TLV vs ukuran alokasi.

## 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/TalatahTiPeuntas/peserta/talatah` | 17.016 B | `1cbab0f8554ac1ec516de90b1fbbdfb957a1aa4ca49319da67499549a2cb6c86` |
| `pwn/TalatahTiPeuntas/peserta/libc.so.6` | 2.190.608 B | `85e64f97e348786a8fb4d9f3d52fec289e2fb86bba20f0731dfe61990525e0f7` |
| `pwn/TalatahTiPeuntas/peserta/ld-linux-x86-64.so.2` | 254.864 B | loader bawaan |

Service asli: `NFX/PWNNXCTF-2026/TalatahTiPeuntas` (TCP), saat penulisan stopped.

## 1.3 Environment

- Linux x86-64; libc challenge (lihat `assets/libc-offsets-and-gadgets.txt`).
- Menjalankan:
  ```bash
  cd pwn/TalatahTiPeuntas/peserta
  ./ld-linux-x86-64.so.2 --library-path . ./talatah
  ```
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `readelf`, `pwntools`.
