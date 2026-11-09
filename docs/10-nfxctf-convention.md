# NFXCTF Convention

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin | `280` |
| Author | `Kada` |
| Solves | `12` |
| Flag | `NFX{h4ck3r_c0nv3nt10n_m4st3r_pwn3r_9988776655}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Service adalah simulator konvensi: register, main mini-game untuk naik rank, edit nama, dan (hanya VIP rank 20+) meninggalkan feedback.
- Ada **tiga bug yang dirangkai**:
  1. `edit_name()` menyalin `fgets()` ke variabel global `player` dengan `strcpy()` tanpa batas → overflow `score`/`rank`;
  2. `leave_feedback()` memakai `read(0, buf, 0x100)` ke buffer stack `0x70` → stack overflow;
  3. `view_profile()` memanggil `printf(log_buf)` → **format string leak**.
- Rank awalnya 5 setelah mini-game. Overflow nama membuat `rank = 0x00000a14` (2580) sehingga gate VIP (rank > 19) terbuka.
- Format string `%7$p` membocorkan canary dan `%17$p` membocorkan return address libc (`libc+0x29d90`).
- ROP `pop rdi; "/bin/sh"; system` → shell, lalu `cat flag.txt`.

## Navigasi Halaman

- [Recon](10-nfxctf-convention-01-recon.md)
- [Analisis](10-nfxctf-convention-02-analisis.md)
- [Eksploitasi](10-nfxctf-convention-03-eksploitasi.md)
- [Flag](10-nfxctf-convention-04-flag.md)
- [Bukti / Evidence](10-nfxctf-convention-05-bukti-evidence.md)
- [Referensi](10-nfxctf-convention-06-referensi.md)
