# Cleartext Sniffing

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Baby</span><span class="nx-chip">180 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Baby` |
| Poin (snapshot) | `180` |
| Author | `Candelena` |
| Tools | strings |
| Flag | `NFXCTF{cl34rt3xt_pr0t0c0ls_l34k_s3cr3ts}` |
| Status | `VERIFIED` |
| Metode | **FULL** — metode utama berhasil direproduksi. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFXCTF{cl34rt3xt_pr0t0c0ls_l34k_s3cr3ts}`
- **Metode:** **FULL** — metode utama berhasil direproduksi.
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](58-cleartext-sniffing-04-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/cleartext-sniffing/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | file traffic.pcap | [Buka](58-cleartext-sniffing-01-recon-artefak.md) |
| 2 | Analisis Artefak | strings -a traffic.pcap \| grep -E "PASS\|NFX\|USER" | [Buka](58-cleartext-sniffing-02-analisis-artefak.md) |
| 3 | Pemulihan Artefak | Flag langsung terlihat di baris PASS. | [Buka](58-cleartext-sniffing-03-pemulihan-artefak.md) |
| 4 | Flag | NFXCTF{cl34rt3xt_pr0t0c0ls_l34k_s3cr3ts} | [Buka](58-cleartext-sniffing-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](58-cleartext-sniffing-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](58-cleartext-sniffing-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Kita dikasih file `traffic.pcap`. Di dalamnya ada percakapan protokol lama yang masih mengirim data tanpa enkripsi. Karena plaintext, kita bisa langsung cari string `USER`, `PASS`, atau `NFX` di dalam pcap.

<div class="nx-evidence-preview"><a href="58-cleartext-sniffing-05-bukti-evidence.html"><img src="assets/cleartext-sniffing/00b-terminal-evidence.png" alt="Pratinjau evidence Cleartext Sniffing" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="58-cleartext-sniffing-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="58-cleartext-sniffing-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="58-cleartext-sniffing-02-analisis-artefak.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="58-cleartext-sniffing-03-pemulihan-artefak.html"><b>Pemulihan Artefak</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="58-cleartext-sniffing-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="58-cleartext-sniffing-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="58-cleartext-sniffing-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
