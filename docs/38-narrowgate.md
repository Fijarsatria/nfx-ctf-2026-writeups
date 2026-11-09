# NarrowGate

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Insane` |
| Poin | `380` |
| Author | `Kesatria Baja Ringan` |
| Solves | `7` |
| Flag | `NFX{ex3cve_d3ni3d_but_0pen_r34d_writ3_s4v3d_th3_day}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `leaker()` memakai `printf(nickname)` → **format string** (canary, PIE, libc).
- `main()` membaca `blocks` (uint32), menghitung `size = blocks * 64`, lalu memvalidasi **hanya 16 bit bawah** dari `size - 1` (`cmp ax, 0x3f`), tetapi `read(0, buf, size)` tetap memakai `size` 32-bit penuh.
- `blocks = 1025` → `size = 65600 = 0x10040`, `(size-1) & 0xffff = 0x003f` → lolos, lalu read besar ke buffer stack `0x50` → **stack overflow** (canary di offset `0x48`).
- Binary memasang **seccomp**: `read/write/open/close/lseek/fstat/newfstatat/brk/exit/exit_group/getrandom`; `execve` dan `openat` diblokir.
- ROP **ORW**: `read(0, path, ...)` → raw `open(path)` → `xchg edi,eax` (fd = rax) → `read(fd, out, ...)` → `write(1, out, ...)`.
- Flag: `NFX{ex3cve_d3ni3d_but_0pen_r34d_writ3_s4v3d_th3_day}`.

## Navigasi Halaman

- [Recon](38-narrowgate-01-recon.md)
- [Analisis](38-narrowgate-02-analisis.md)
- [Eksploitasi](38-narrowgate-03-eksploitasi.md)
- [Flag](38-narrowgate-04-flag.md)
- [Bukti / Evidence](38-narrowgate-05-bukti-evidence.md)
- [Referensi](38-narrowgate-06-referensi.md)
