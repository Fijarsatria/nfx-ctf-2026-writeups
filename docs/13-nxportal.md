# NXPortal

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Web</span><span class="nx-chip">Medium</span><span class="nx-chip">480 poin</span><span class="nx-badge nx-badge-open">OPEN</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `480` |
| Author | `Ariaf` |
| Tools | curl, python3, sage, git, docker |
| Flag | **OPEN — belum ditemukan** |
| Status | `OPEN` |

[← Kembali ke Index](index.md)

> **Status: OPEN.** Halaman ini memuat analisis dan kendala yang ditemui; flag belum ditemukan.

## Ringkasan

> Catatan: `flags/web/NXPortal.txt` **bukan flag**, melainkan catatan investigasi
> (`UNSOLVED — NXPortal ...`). Tidak ada flag placeholder di platform
> (`flag_placeholder=false`). Writeup ini mendokumentasikan seluruh temuan,
> payload yang sudah dicoba, dan rencana penyelesaian. **Tidak ada flag yang
> dikarang dan tidak ada submit ke platform.**
## TL;DR

- **NXPortal** adalah gerbang identitas Flask/gunicorn dengan alur login dan
  **account recovery** (`/forgot` → email berisi token → `/reset`).
- Deskripsi challenge: data yang dikendalikan user memengaruhi lebih dari isi
  pesan, dan dalam kondisi tertentu permintaan recovery bisa terkirim ke tujuan
  yang seharusnya tidak menerimanya.
- Blog internal `/blog/5` memberi hint eksplisit: **“Hardening Header Parsing &
  Mail Notification Engines”**, “RFC822 mail header sanitization”, “preventing
  multi-line payload abuse”, dan “unauthorized header parameter pollution”.
  Ini mengarah ke **email header injection / recipient confusion** pada
  notification dispatcher.
- Filter domain `/forgot` hanya mengecek substring `@nxctf.local`. Payload
  display-name, double-`@`, dan CRLF `Bcc:`/`To:` berhasil melewati filter
  (respons `alert-success`).
- **Blocker:** instance live tidak mengirim email ke inbox eksternal (diuji
  dengan mail.tm), dan tidak ada route mailbox/MailHog/Mailpit yang terekspos.
  Port 1025/8025 dan port mail umum di host tertutup. Tanpa email/token, reset
  admin tidak dapat diselesaikan.
- Rencana penyelesaian ada di §7. Status tetap **OPEN**.

<div class="nx-evidence-preview"><a href="13-nxportal-05-bukti-evidence.html"><img src="assets/nxportal/98-terminal-evidence.png" alt="Pratinjau evidence NXPortal" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="13-nxportal-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="13-nxportal-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="13-nxportal-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="13-nxportal-03-eksploitasi-solver-sebagian-belum-selesa.html"><b>Eksploitasi / Solver (sebagian, belum selesai)</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="13-nxportal-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="13-nxportal-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="13-nxportal-06-rencana-penyelesaian-open.html"><b>Rencana Penyelesaian (OPEN)</b><span>Rencana penyelesaian (OPEN)</span></a>
<a class="nx-page-card" href="13-nxportal-07-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
