# Career Tempat Belajar

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Osint` |
| Difficulty | `Medium` |
| Poin | `380` |
| Author | `Kada` |
| Flag | `NFX{Gr4v4t4r_0s1nt_R3cru1t3r_D1hL34Rn}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## Ringkasan

> Catatan metadata: `writeups/_manifest.json` mencatat 380 poin / 7 solves,
> sedangkan `umum/Osint/career-tempat-belajar/challenge.json` mencatat
> 480 poin / 2 solves (snapshot saat challenge baru dibuat). Angka platform
> terbaru yang dipakai di tabel; perbedaannya dicatat agar tidak menyesatkan.
## TL;DR

- Challenge memberi sebuah poster AI berjudul **“DIGITAL HOUR LEARNING”**.
  Metadata PNG-nya membocorkan nama perusahaan: `Title: Dih Office`,
  `Author: Kada`, dan `Comment: 3%4TD'aPBA*Z,QPN` (decoy, bukan password).
- Nama perusahaan adalah **Digital Hour Learning / Dihlearn**. Jejak publiknya
  ada di Instagram `@dihlearn.id` dan akun karier `@career.dihlearn.id`.
- Jejak publik akun karier mengarah ke alamat email rekrutmen
  **`dihlearn.id@gmail.com`**.
- “Platform G-R” pada deskripsi adalah **Gravatar**. Gravatar mencari profil
  berdasarkan **MD5 dari email**:
  `md5("dihlearn.id@gmail.com") = 7149a84591149f4933058779e485a3c9`.
- Profil Gravatar live tersebut memuat flag di field `aboutMe`:
  `NFX{Gr4v4t4r_0s1nt_R3cru1t3r_D1hL34Rn}`.

## Navigasi Halaman

- [Recon](09-career-tempat-belajar-01-recon.md)
- [Analisis](09-career-tempat-belajar-02-analisis.md)
- [Eksploitasi / Solver](09-career-tempat-belajar-03-eksploitasi-solver.md)
- [Flag](09-career-tempat-belajar-04-flag.md)
- [Bukti / Evidence](09-career-tempat-belajar-05-bukti-evidence.md)
- [Referensi](09-career-tempat-belajar-06-referensi.md)
