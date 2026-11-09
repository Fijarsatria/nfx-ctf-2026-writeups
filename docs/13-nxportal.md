# NXPortal

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `480` |
| Author | `Ariaf` |
| Flag | **OPEN — belum ditemukan** |
| Status | `OPEN` |

[← Kembali ke Index](index.md)

> **Status: OPEN.** Halaman ini dokumentasi analisis/blocker, bukan flag.

## Ringkasan

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

## Navigasi Halaman

- [Recon](13-nxportal-01-recon.md)
- [Analisis](13-nxportal-02-analisis.md)
- [Eksploitasi / Solver (sebagian, belum selesai)](13-nxportal-03-eksploitasi-solver-sebagian-belum-selesa.md)
- [Flag](13-nxportal-04-flag.md)
- [Bukti / Evidence](13-nxportal-05-bukti-evidence.md)
- [Rencana Penyelesaian (OPEN)](13-nxportal-06-rencana-penyelesaian-open.md)
- [Referensi](13-nxportal-07-referensi.md)
