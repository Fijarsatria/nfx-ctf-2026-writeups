# SymHell

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Medium` |
| Poin | `340` |
| Author | `Ariaf` |
| Solves | `9` |
| Flag | `NFX{5ymH3ll_RUnT1m3_3v4l_53cr3t_PwN!}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Service menjalankan input pengguna dengan `subprocess.run(line, shell=True,
  executable=bash)` setelah memblokir huruf, angka, `?`, `*`, `#`, dan `<<<`.
- Filter hanya memeriksa **karakter mentah input**, bukan hasil ekspansi
  shell.
- Dengan hanya simbol, kita bisa memakai:
  - **command substitution** `$(<file)` yang membaca isi file (pengganti
    `cat`), dan
  - **bracket glob** `[.-~]` — range ASCII `'.'` (0x2E) sampai `'~'`
    (0x7E) — untuk mencocokkan nama file tanpa menulis huruf.
- Payload:
  `$(</[.-~][.-~][.-~][.-~].[.-~][.-~][.-~])`
- Payload membaca `/flag.txt`. Hasilnya menjadi nama command; bash gagal
  mengeksekusinya dan mencetak flag ke **stderr**:
  `bash: line 1: NFX{...}: command not found`.
- Server mengembalikan stderr jika stdout kosong, sehingga flag bocor.

## Navigasi Halaman

- [Recon](31-symhell-01-recon.md)
- [Analisis](31-symhell-02-analisis.md)
- [Eksploitasi / Solver](31-symhell-03-eksploitasi-solver.md)
- [Flag](31-symhell-04-flag.md)
- [Bukti / Evidence](31-symhell-05-bukti-evidence.md)
- [Referensi](31-symhell-06-referensi.md)
