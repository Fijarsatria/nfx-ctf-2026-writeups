# Dead Drop

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Baby</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Author | `Ariaf` |
| Difficulty | `Baby` |
| Poin (snapshot) | `100` |
| Tools | git |
| Flag | `NFX{g1t_c0nf1g_h34d3r_l34k_h1dd3n_br4nch_9c1e7a}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{g1t_c0nf1g_h34d3r_l34k_h1dd3n_br4nch_9c1e7a}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](81-dead-drop-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/dead-drop/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | `.git/config` extraheader, bukan commit `main`. | [Buka](81-dead-drop-01-recon-artefak.md) |
| 2 | Cara Mendapatkan Flag | Decode header. Branch remote belum diarsipkan. | [Buka](81-dead-drop-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{g1t_c0nf1g_h34d3r_l34k_h1dd3n_br4nch_9c1e7a} | [Buka](81-dead-drop-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](81-dead-drop-04-bukti-evidence.md) |
| 5 | Referensi | Git hidden branch, config leak. | [Buka](81-dead-drop-05-referensi.md) |

## Cerita singkat

`.git/config` menyimpan `http.extraheader` berisi Authorization basic. Decode-nya adalah token GitHub. Branch tersembunyi ada di remote, bukan di zip, dan transkripnya belum diarsipkan.

<div class="nx-evidence-preview"><a href="81-dead-drop-04-bukti-evidence.html"><img src="assets/dead-drop/00b-terminal-evidence.png" alt="Pratinjau evidence Dead Drop" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="81-dead-drop-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="81-dead-drop-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="81-dead-drop-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="81-dead-drop-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="81-dead-drop-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="81-dead-drop-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
