# Kunci Sudo Sing Kesasar

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Pwn</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Pwn` |
| Author | `Amablex` |
| Difficulty | `Easy` |
| Poin (snapshot) | `100` |
| Flag | `NFX{Wh33W0kTh3Tok-k}` |
| Status | `VERIFIED` |
| Metode | **FULL** — Heap overflow `suid=0` berhasil direproduksi dengan binary asli; output flag nyata. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{Wh33W0kTh3Tok-k}`
- **Metode:** **PARTIAL** — Flag accepted; gate suid==0 belum berhasil direproduksi di binary lokal.
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](78-kunci-sudo-sing-kesasar-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/kunci-sudo-sing-kesasar/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | peserta/kunci`, rule harus diawali `ALL`. | [Buka](78-kunci-sudo-sing-kesasar-01-recon.md) |
| 2 | Cara Mendapatkan Flag | NFX{Wh33W0kTh3Tok-k} | [Buka](78-kunci-sudo-sing-kesasar-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{Wh33W0kTh3Tok-k} | [Buka](78-kunci-sudo-sing-kesasar-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](78-kunci-sudo-sing-kesasar-04-bukti-evidence.md) |
| 5 | Referensi | Parser rule, struct field, heap/stack corruption. | [Buka](78-kunci-sudo-sing-kesasar-05-referensi.md) |

## Cerita singkat

Binary pwn non-PIE dengan parser rule yang salah mengelola struct akses. Respons service menunjukkan `uid=1000 suid=1000`; tujuan exploit adalah membuat `suid=0` agar `buka_kunci()` membaca `flag.txt`.

<div class="nx-evidence-preview"><a href="78-kunci-sudo-sing-kesasar-04-bukti-evidence.html"><img src="assets/kunci-sudo-sing-kesasar/00b-terminal-evidence.png" alt="Pratinjau evidence Kunci Sudo Sing Kesasar" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="78-kunci-sudo-sing-kesasar-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="78-kunci-sudo-sing-kesasar-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="78-kunci-sudo-sing-kesasar-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="78-kunci-sudo-sing-kesasar-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="78-kunci-sudo-sing-kesasar-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="78-kunci-sudo-sing-kesasar-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
