# ChangeTrack

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

## Ringkasan

## TL;DR

- **ChangeTrack** adalah Flask/gunicorn yang meniru `changedetection.io`: user membuat watcher, mengedit manifest YAML, dan worker mengirim notifikasi ke `webhook_url`.
- Login-nya rusak: `admin@changetrack.local` dengan password `anything` (non-trivial) langsung menghasilkan session admin. Password 1 karakter ditolak, tetapi ini tetap auth bypass yang memudahkan.
- Field `notification.template` di manifest YAML dirender oleh **Jinja2 tanpa sandbox**. Payload `{{ 7*7 }}` terbukti menghasilkan `49` di body webhook.
- Payload RCE `{{ cycler.__init__.__globals__.os.popen('cat /flag.txt').read() }}` mengeksekusi perintah sebagai **root** dan mengirim hasilnya ke webhook eksternal (webhook.site) → **SSTI OOB**.
- Flag: `NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}`. Nama CVE di flag merujuk pada **CVE-2024-32651** (SSTI pada notification template changedetection.io).

## Navigasi Halaman

- [Recon](48-changetrack-01-recon.md)
- [Analisis](48-changetrack-02-analisis.md)
- [Eksploitasi / Solver](48-changetrack-03-eksploitasi-solver.md)
- [Flag](48-changetrack-04-flag.md)
- [Bukti / Evidence](48-changetrack-05-bukti-evidence.md)
- [Referensi](48-changetrack-06-referensi.md)
