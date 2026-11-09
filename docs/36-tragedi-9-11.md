# Tragedi 9/11

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Osint` |
| Difficulty | `Hard` |
| Poin | `380` |
| Author | `salep88` |
| Solves | `7` |
| Tools | curl, python3, git |
| Flag | `NFX{OS1NT_DU4R_D34_D0R}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Video challenge adalah rekaman 9/11 berdurasi **58,5 detik**, 1920×1080,
  H.264 + AAC. Ini video “shop owner saves woman's life from wall of dust
  on 9/11”.
- Video itu dibagikan di **r/PublicFreakout** oleh **u/PigParkerPt2** pada
  11 September 2021. Username ini menjadi pivot.
- Di GitHub ada user **PigParkerPt2** dengan repo **`xor-operation`**.
- Repo saat ini terlihat “bersih”, tetapi **history git** menyimpan
  commit `df34505` yang menambahkan `.env` berisi flag.
- Commit `ea765a9` menghapus `.env`, tetapi objek commit lama tetap ada.
- Flag: `NFX{OS1NT_DU4R_D34_D0R}`.

## Navigasi Halaman

- [Recon](36-tragedi-9-11-01-recon.md)
- [Analisis](36-tragedi-9-11-02-analisis.md)
- [Eksploitasi / Solver](36-tragedi-9-11-03-eksploitasi-solver.md)
- [Flag](36-tragedi-9-11-04-flag.md)
- [Bukti / Evidence](36-tragedi-9-11-05-bukti-evidence.md)
- [Referensi](36-tragedi-9-11-06-referensi.md)
