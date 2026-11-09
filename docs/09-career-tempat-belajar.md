# Career Tempat Belajar

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Osint</span><span class="nx-chip">Medium</span><span class="nx-chip">380 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Osint` |
| Difficulty | `Medium` |
| Poin | `380` |
| Author | `Kada` |
| Tools | curl, python3, exiftool, git |
| Flag | `NFX{Gr4v4t4r_0s1nt_R3cru1t3r_D1hL34Rn}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

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

<div class="nx-evidence-preview"><a href="09-career-tempat-belajar-05-bukti-evidence.html"><img src="assets/career-tempat-belajar/98-terminal-evidence.png" alt="Pratinjau evidence Career Tempat Belajar" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="09-career-tempat-belajar-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="09-career-tempat-belajar-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="09-career-tempat-belajar-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="09-career-tempat-belajar-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="09-career-tempat-belajar-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="09-career-tempat-belajar-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="09-career-tempat-belajar-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
