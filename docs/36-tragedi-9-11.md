# Tragedi 9/11

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Osint</span><span class="nx-chip">Hard</span><span class="nx-chip">380 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


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

<div class="nx-evidence-preview"><a href="36-tragedi-9-11-05-bukti-evidence.html"><img src="assets/tragedi-9-11/98-terminal-evidence.png" alt="Pratinjau evidence Tragedi 9/11" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="36-tragedi-9-11-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="36-tragedi-9-11-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
