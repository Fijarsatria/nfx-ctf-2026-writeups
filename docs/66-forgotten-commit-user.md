# Forgotten Commit (User)

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Boot To Root</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Boot To Root` |
| Author | `Ariaf` |
| Difficulty | `Easy` |
| Poin | `100` |
| Tools | nmap, curl, git |
| Flag | `NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh}` |
| Status | `VERIFIED` |
[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](66-forgotten-commit-user-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/forgotten-commit-user/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | http://10.10.20.21/.git/HEAD | [Buka](66-forgotten-commit-user-01-recon.md) |
| 2 | Cara Mendapatkan Flag | NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh} | [Buka](66-forgotten-commit-user-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh} | [Buka](66-forgotten-commit-user-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](66-forgotten-commit-user-04-bukti-evidence.md) |
| 5 | Referensi | Git exposure, git-dumper, credential leak. | [Buka](66-forgotten-commit-user-05-referensi.md) |

## Cerita singkat

Ini tahap User dari Forgotten Commit. Webroot membocorkan `.git`, history-nya menyimpan kredensial, lalu kita SSH sebagai user dan baca user.txt.

<div class="nx-evidence-preview"><a href="66-forgotten-commit-user-04-bukti-evidence.html"><img src="assets/forgotten-commit-user/00b-terminal-evidence.png" alt="Pratinjau evidence Forgotten Commit (User)" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="66-forgotten-commit-user-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="66-forgotten-commit-user-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="66-forgotten-commit-user-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="66-forgotten-commit-user-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="66-forgotten-commit-user-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="66-forgotten-commit-user-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
