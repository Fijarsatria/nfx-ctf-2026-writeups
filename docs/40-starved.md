# Starved

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin | `380` |
| Author | `Kesatria Baja Ringan` |
| Solves | `7` |
| Flag | `NFX{st4rv3d_s3cc0mp_fd0_r3us3_r0p_m4st3r}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `leaker()` mencetak nickname dengan `printf(nickname)` → **format string leak** (canary, PIE, libc).
- `main()` membaca 8 byte: `[len:u32][magic:u32]`; jika magic `0xdead`, ia memanggil `read(0, rbp-0x1a0, len)` dengan `len` 32-bit dari klien → **stack overflow** (offset canary `0x198`).
- Ada **seccomp** yang mengizinkan `write/open/openat/pread64/close/lseek/fstat/newfstatat/brk/exit/exit_group`, tetapi `read` hanya boleh dengan **fd 0**.
- ROP: `close(0)` → `open("flag.txt")` (hasilnya fd 0) → `read(0, bss, 0x100)` → `write(1, bss, 0x100)`.
- Flag: `NFX{st4rv3d_s3cc0mp_fd0_r3us3_r0p_m4st3r}`.

## Navigasi Halaman

- [Recon](40-starved-01-recon.md)
- [Analisis](40-starved-02-analisis.md)
- [Eksploitasi](40-starved-03-eksploitasi.md)
- [Flag](40-starved-04-flag.md)
- [Bukti / Evidence](40-starved-05-bukti-evidence.md)
- [Referensi](40-starved-06-referensi.md)
