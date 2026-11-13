# Easy Config Decoy

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Reverse</span><span class="nx-chip">Easy</span><span class="nx-chip">260 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Reverse` |
| Difficulty | `Easy` |
| Poin (snapshot) | `260` |
| Author | `cypera` |
| Tools | objdump |
| Flag | `NFX{c0nf1g_d3c0y_p4rts_4r3_fun}` |
| Status | `VERIFIED` |
| Metode | **FULL** — metode utama berhasil direproduksi. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{c0nf1g_d3c0y_p4rts_4r3_fun}`
- **Metode:** **FULL** — metode utama berhasil direproduksi.
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](61-easy-config-decoy-04-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/easy-config-decoy/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | file easy_config | [Buka](61-easy-config-decoy-01-recon.md) |
| 2 | Analisis | NFX{c0nf + 1g_ + d3c0y_ + p4rts + _ + 4r3_fun} | [Buka](61-easy-config-decoy-02-analisis.md) |
| 3 | Solver | NFX{c0nf1g_d3c0y_p4rts_4r3_fun} | [Buka](61-easy-config-decoy-03-solver.md) |
| 4 | Flag | NFX{c0nf1g_d3c0y_p4rts_4r3_fun} | [Buka](61-easy-config-decoy-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](61-easy-config-decoy-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](61-easy-config-decoy-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Binary ini menyimpan flag dalam beberapa potongan string di `.rodata`, bukan satu string utuh. Di sebelahnya ada dua flag palsu (decoy). Kita harus lihat potongan mana yang benar-benar dirangkai oleh program.

<div class="nx-evidence-preview"><a href="61-easy-config-decoy-05-bukti-evidence.html"><img src="assets/easy-config-decoy/00b-terminal-evidence.png" alt="Pratinjau evidence Easy Config Decoy" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="61-easy-config-decoy-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="61-easy-config-decoy-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="61-easy-config-decoy-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="61-easy-config-decoy-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="61-easy-config-decoy-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="61-easy-config-decoy-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="61-easy-config-decoy-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
