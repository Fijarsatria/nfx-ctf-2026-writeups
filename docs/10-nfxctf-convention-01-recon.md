# NFXCTF Convention — Recon

[← Overview](10-nfxctf-convention.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Kada**
>
> Selamat datang di NFXCTF Hacker Convention! Sebagai peserta konvensi, Anda dapat mendaftarkan diri, bermain mini-game untuk meningkatkan level akses (rank), dan meninggalkan pesan rahasia (feedback) kepada panitia. Hanya peserta tingkat "VIP" yang bisa mengakses sistem log umpan balik.
>
> Namun rumornya, sistem registrasi kami masih memiliki beberapa bug. Dapatkah Anda meretas sistem konvensi ini dan mencuri yang anda carii?
>
> Format Flag: `NFX{your_flag_here}`

Metadata platform (`writeups/_challenges.json`) mencatat challenge ini sebagai Pwn Medium, 280 poin, 12 solves, author Kada.

### 1.2 File / service yang diberikan

Platform tidak melampirkan file (`attachments: []`); challenge berupa service TCP dinamis `NFX/NFXCTFConvention`. Namun **source bundle** yang sama tersedia publik di repo upstream yang sudah di-mirror ke workspace:

| File | Ukuran | SHA-256 |
|---|---|---|
| `work/event/pwn/nfxctf-convention/src/peserta/oscar_convention` | 17.000 B | `ff7ff155dd6df34d61c019aee43c7c3fc2fc0863bbdd297db053cd75874fdd88` |
| `.../src/peserta/libc.so.6` | 2.220.400 B | `e01b1ce7be2987f3b8560e26d0df2623f9dd5cec17be923ae28a785bc0d32d50` |
| `.../src/peserta/ld-linux-x86-64.so.2` | 240.936 B | (loader Ubuntu 22.04, lihat `assets/.../01-file-hash-checksec.txt`) |

Bundle zip asli: `work/upstream/qazwsx/pwn/NFXCTFConvention.zip` (berisi `peserta/oscar_convention`, `libc.so.6`, `ld-linux-x86-64.so.2`). Ada juga `oscar_local`, yaitu rebuild lokal untuk uji; writeup ini memakai `oscar_convention` asli.

### 1.3 Environment

- Linux x86-64, glibc host 2.39; untuk reproduksi dipakai loader + libc bawaan challenge (Ubuntu GLIBC 2.35).
- Tools: `file`, `sha256sum`, `objdump`, `strings`, `nm`, `pwntools` (`ELF`, `ROP`, `process`).
- Menjalankan binary:
  ```bash
  work/event/pwn/nfxctf-convention/src/peserta/ld-linux-x86-64.so.2 \
    --library-path work/event/pwn/nfxctf-convention/src/peserta \
    work/event/pwn/nfxctf-convention/src/peserta/oscar_convention
  ```

### 1.4 Triage awal

```text
$ file oscar_convention
oscar_convention: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=d2a472d788b50d7ae1cb2b3489b049f24cf7baa4,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools ELF.checksec)
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
SHSTK:      Enabled
IBT:        Enabled
Stripped:   No
```

`strings` memperlihatkan seluruh alur menu dan pesan validasi:

```text
Welcome to the NFXCTF Hacker Convention!
Enter your name:
[!] You must be at least rank 5 to change your name.
[+] Name updated.
--- USER PROFILE ---
Name: %s
Rank: %d
Score: %d
Quote:
Activity Log:
[ Mini Game - Answer 10 questions to reach rank 5 ]
Correct! You have reached rank 5.
[!] Only VIP members (rank 20+) can leave feedback.
Enter your feedback:
[+] Feedback saved to log.
```

**Temuan:** binary tidak stripped, jadi symbol `register_user`, `edit_name`, `view_profile`, `leave_feedback`, `play_game`, `menu`, `main` langsung terbaca.
