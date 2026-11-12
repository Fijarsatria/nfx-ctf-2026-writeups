# ChangeTrack

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Web</span><span class="nx-chip">Medium</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `300` |
| Author | `Ariaf` |
| Solves | `11` |
| Tools | curl, python3, sage, git |
| Flag | `NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/changetrack/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. **ChangeTrack** adalah Flask/gunicorn yang meniru `changedetection.io`: user membuat watcher, mengedit manifest YAML, dan worker mengirim notifikasi ke `webhook_url`. Terus, login-nya rusak: `admin@changetrack.local` dengan password `anything` (non-trivial) langsung menghasilkan session admin. Password 1 karakter ditolak, tetapi ini tetap auth bypass yang memudahkan. Lalu, field `notification.template` di manifest YAML dirender oleh **Jinja2 tanpa sandbox**. Payload `{{ 7*7 }}` terbukti menghasilkan `49` di body webhook. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | curl -sS -i "$BASE/" | [Buka](48-changetrack-01-recon.md) |
| 2 | Analisis | https://api.github.com/events | [Buka](48-changetrack-02-analisis.md) |
| 3 | Analisis | https://api.github.com/events | [Buka](48-changetrack-03-analisis-2.md) |
| 4 | Analisis | https://api.github.com/zen | [Buka](48-changetrack-04-analisis-3.md) |
| 5 | Eksploitasi / Solver | curl -sS -c cj -X POST \ | [Buka](48-changetrack-05-eksploitasi-solver.md) |
| 6 | Output asli | NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026} | [Buka](48-changetrack-06-output-asli.md) |
| 7 | Flag | NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026} | [Buka](48-changetrack-07-flag.md) |
| 8 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](48-changetrack-08-bukti-evidence.md) |
| 9 | Referensi | — | [Buka](48-changetrack-09-referensi.md) |

## TL;DR

- **ChangeTrack** adalah Flask/gunicorn yang meniru `changedetection.io`: user membuat watcher, mengedit manifest YAML, dan worker mengirim notifikasi ke `webhook_url`.
- Login-nya rusak: `admin@changetrack.local` dengan password `anything` (non-trivial) langsung menghasilkan session admin. Password 1 karakter ditolak, tetapi ini tetap auth bypass yang memudahkan.
- Field `notification.template` di manifest YAML dirender oleh **Jinja2 tanpa sandbox**. Payload `{{ 7*7 }}` terbukti menghasilkan `49` di body webhook.
- Payload RCE `{{ cycler.__init__.__globals__.os.popen('cat /flag.txt').read() }}` mengeksekusi perintah sebagai **root** dan mengirim hasilnya ke webhook eksternal (webhook.site) → **SSTI OOB**.
- Flag: `NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}`. Nama CVE di flag merujuk pada **CVE-2024-32651** (SSTI pada notification template changedetection.io).

<div class="nx-evidence-preview"><a href="48-changetrack-08-bukti-evidence.html"><img src="assets/changetrack/00b-terminal-evidence.png" alt="Pratinjau evidence ChangeTrack" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="48-changetrack-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="48-changetrack-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="48-changetrack-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="48-changetrack-03-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="48-changetrack-04-analisis-3.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="48-changetrack-05-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="48-changetrack-06-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="48-changetrack-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="48-changetrack-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="48-changetrack-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
