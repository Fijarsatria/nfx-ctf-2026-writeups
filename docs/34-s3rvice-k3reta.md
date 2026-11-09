# S3rvice K3reta

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Osint</span><span class="nx-chip">Hard</span><span class="nx-chip">480 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Osint` |
| Difficulty | `Hard` |
| Poin | `480` |
| Author | `Kada` |
| Tools | curl, python3, gdb, strings, exiftool, git |
| Flag | `NFX{Dr0n3_T3rb41k_T3mp4t_S3rv1c3_T3rb41k_J4uh_B4ng3T_BTW_B4ng_R0f1_K3r3n_S3rb4_b1s4}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

> Catatan penting: `flags/wave2/S3rvice_K3reta.NOTES.md` dan
> `flags/wave2/S3rvice_K3reta.txt` (`OSCAR{G1008}`) adalah analisis **wave 1**
> yang mengarah ke Whoosh/Padalarang. Artefak wave 1 lain
> (`flags/extend/from_train.candidate.txt` = `NFX{Padalarang}`) menguatkan
> itu. Untuk wave 2, gambar dan Q&A yang diberikan mengarah ke **longsor
> Cilebut–Bojong Gede 21 November 2012**. Writeup ini memakai jalur wave 2.
## TL;DR

- Gambar `from_train.jpeg` adalah foto dari jendela KRL yang melintas di
  petak **Cilebut–Bojong Gede**, memperlihatkan sawah, atap rumah, kompleks
  perumahan di kejauhan, dan tower transmisi.
- Kejadian yang menjadi titik awal adalah **tanah longsor tebingan rel** di
  **KM 45+4/5**, antara **Stasiun Cilebut dan Bojong Gede**, pada
  **21 November 2012**.
- Q1–Q8 sudah terjawab: `longsor`, `45+4/5`, `Cilebut - Bojong Gede`,
  `21/11/2012`, `98`, `200 M`, `Atlas`, `6007`.
- Q9–Q13 sudah terjawab: `fandi_8510`, `01/02/2026`,
  `Rofi Servis Drone Bogor`, `7R73+FM7`, `RofiServis`.
- Flag valid: `NFX{Dr0n3_T3rb41k_T3mp4t_S3rv1c3_T3rb41k_J4uh_B4ng3T_BTW_B4ng_R0f1_K3r3n_S3rb4_b1s4}`
  (diterima platform, `+480`).

<div class="nx-evidence-preview"><a href="34-s3rvice-k3reta-05-bukti-evidence.html"><img src="assets/s3rvice-k3reta/98-terminal-evidence.png" alt="Pratinjau evidence S3rvice K3reta" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="34-s3rvice-k3reta-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="34-s3rvice-k3reta-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="34-s3rvice-k3reta-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="34-s3rvice-k3reta-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="34-s3rvice-k3reta-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="34-s3rvice-k3reta-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="34-s3rvice-k3reta-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
