# Starved — Recon

[← Overview](40-starved.md) · [Index](index.md)

> **Langkah 1/9 — Recon.** Dua petunjuk: "kode sapaan terlalu percaya pada input pengguna" (format string di leaker) dan "jalur upload memakai ukuran yang dikirim klien" (stack overflow di main).
>
> **Titik penting:** Dua petunjuk: "kode sapaan terlalu percaya pada input pengguna" (format string di leaker) dan "jalur upload memakai ukuran yang dikirim klien" (stack overflow di main).
>
> **Berikutnya:** [Triage awal](40-starved-02-triage-awal.md)

## 1.1 Deskripsi challenge

> **Author: Kesatria Baja Ringan**
>
> **Starved** adalah layanan relay kecil yang meminta nickname sebelum menerima request upload. Kode sapaan terlalu percaya pada input pengguna, dan jalur upload lebih parah lagi karena memakai ukuran yang dikirim klien.

Dua petunjuk: "kode sapaan terlalu percaya pada input pengguna" (format string di `leaker`) dan "jalur upload memakai ukuran yang dikirim klien" (stack overflow di `main`).

## 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/Starved/peserta/chall` | 12.856 B | `a9bf480c6deded80a4400715e92ad7d1c4d795aadafc2a6ba72b5e1b3a4c6a0e` |
| `pwn/Starved/peserta/libc.so.6` | 2.220.400 B | `b2cf6c33b74d2f22543b7a469a75b538911e690f769d0b238843a49465b83793` |
| `pwn/Starved/peserta/ld-linux-x86-64.so.2` | 240.936 B | loader Ubuntu 22.04 |

Service asli: `NFX/Starved` (TCP 41825), saat penulisan berstatus stopped. Analisis pada bundle peserta.

## 1.3 Environment

- Linux x86-64; libc bawaan challenge = Ubuntu GLIBC 2.35.
- Menjalankan dengan loader + libc challenge:
  ```bash
  cd pwn/Starved/peserta
  ./ld-linux-x86-64.so.2 --library-path . ./chall
  ```
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `pwntools`, `ROP`.
