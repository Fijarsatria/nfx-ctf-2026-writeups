# Tragedi 9/11

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Osint</span><span class="nx-chip">Hard</span><span class="nx-chip">380 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Osint` |
| Difficulty | `Hard` |
| Poin (snapshot) | `380` |
| Author | `salep88` |
| Solves | `7` |
| Tools | curl, python3, git |
| Flag | `NFX{OS1NT_DU4R_D34_D0R}` |
| Status | `VERIFIED` |
| Metode | **FULL** — metode utama berhasil direproduksi. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/tragedi-9-11/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. video challenge adalah rekaman 9/11 berdurasi **58,5 detik**, 1920×1080, H.264 + AAC. Ini video “shop owner saves woman's life from wall of dust on 9/11”. Terus, video itu dibagikan di **r/PublicFreakout** oleh **u/PigParkerPt2** pada 11 September 2021. Username ini menjadi pivot. Lalu, di GitHub ada user **PigParkerPt2** dengan repo **`xor-operation`**. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Jejak Awal | sha256sum drive/view.mp4 | [Buka](36-tragedi-9-11-01-jejak-awal.md) |
| 2 | Triage awal | file drive/view.mp4 | [Buka](36-tragedi-9-11-02-triage-awal.md) |
| 3 | Analisis Jejak | https://github.com/PigParkerPt2/xor-operation | [Buka](36-tragedi-9-11-03-analisis-jejak.md) |
| 4 | Analisis Jejak | git log --all --oneline --stat | [Buka](36-tragedi-9-11-04-analisis-jejak-2.md) |
| 5 | Pencarian & Verifikasi | git clone https://github.com/PigParkerPt2/xor-operation.git | [Buka](36-tragedi-9-11-05-pencarian-verifikasi.md) |
| 6 | Flag | NFX{OS1NT_DU4R_D34_D0R} | [Buka](36-tragedi-9-11-06-flag.md) |
| 7 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](36-tragedi-9-11-07-bukti-evidence.md) |
| 8 | Referensi | https://www.reddit.com/r/PublicFreakout/comments/pmgkqi/shop_owner_saves_womans_life_from_wall_of_dust_on/ | [Buka](36-tragedi-9-11-08-referensi.md) |

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
- Flag verified lewat submit web: `NFX{OS1NT_DU4R_D34_D0R}`.

<div class="nx-evidence-preview"><a href="36-tragedi-9-11-07-bukti-evidence.html"><img src="assets/tragedi-9-11/00b-terminal-evidence.png" alt="Pratinjau evidence Tragedi 9/11" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="36-tragedi-9-11-07-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="36-tragedi-9-11-01-jejak-awal.html"><b>Jejak Awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-03-analisis-jejak.html"><b>Analisis Jejak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-04-analisis-jejak-2.html"><b>Analisis Jejak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-05-pencarian-verifikasi.html"><b>Pencarian &amp; Verifikasi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-06-flag.html"><b>Flag</b><span>Flag dan status verifikasi</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-07-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="36-tragedi-9-11-08-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
