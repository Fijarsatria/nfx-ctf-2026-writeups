# NXPortal — Recon

[← Overview](13-nxportal.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> **NXPortal** adalah gerbang identitas utama perusahaan yang mengelola single
> sign-on internal dan tata kelola akses karyawan.
>
> Baru-baru ini, seorang peneliti keamanan menemukan kejanggalan pada sistem
> notifikasi pemulihan akun NXPortal. Data yang dikendalikan pengguna tampaknya
> memengaruhi lebih dari sekadar isi pesan—dan dalam kondisi tertentu, sebuah
> permintaan pemulihan mungkin dapat terkirim ke tujuan yang seharusnya tidak
> menerimanya.

Kalimat kunci:
- “data yang dikendalikan pengguna” → field `email` pada `/forgot`.
- “memengaruhi lebih dari sekadar isi pesan” → header/envelope email.
- “terkirim ke tujuan yang seharusnya tidak menerimanya” → recipient injection
  / header injection.

### 1.2 File / service

Tidak ada source lokal (`umum/Web/nxportal` hanya `BRIEF.md` + `challenge.json`).
Yang tersedia adalah instance live dan catatan investigasi sebelumnya.

| Item | Nilai |
|---|---|
| Instance live (validasi) | `http://s1.nfx.my.id:40001` |
| Stack | Flask + gunicorn (`Server: gunicorn`) |
| Route publik | `/`, `/about`, `/services`, `/blog`, `/blog/<id>`, `/contact`, `/login`, `/forgot`, `/reset` |
| Route auth | `/dashboard` (302 ke `/login` bila belum login) |
| Domain email | `@nxctf.local` |
| Flag file | `flags/web/NXPortal.txt` (catatan investigasi, bukan flag challenge) |

Catatan sebelumnya (`flags/web/NXPortal.txt`) menyebut:
- instance `http://s1.nfx.my.id:40001`;
- dua solver: `akudanil` dan `Broel`;
- percobaan email injection ke yopmail tidak menghasilkan email;
- mailbox/MailHog tidak terekspos;
- session/JWT/itsdangerous forging, SQLi, SSTI, LFI, command injection, Host
  poisoning, default creds: negatif.

### 1.3 Environment

- `curl`, `python3` + `requests`.
- Instance dijalankan ulang dengan:
  ```bash
  cd /home/bocil/ctf/nfx
  python3 nxapi.py nx-up "NFX/NXPortal" "NFXCTF-NFCC-NXCTF-2026"
  ```
- Sink email eksternal untuk uji: **mail.tm** (API gratis).
- Tidak ada submit flag.

### 1.4 Triage awal

```bash
BASE=http://s1.nfx.my.id:40001
curl -sS -i "$BASE/"
curl -sS -i "$BASE/login"
curl -sS -i "$BASE/forgot"
curl -sS -i "$BASE/reset"
```

Temuan:
- `/` → `200`, landing NXPortal.
- `/login` → `200`, form `email` + `password`, `POST /login`.
- `/forgot` → `200`, form “Corporate Account Recovery”, `POST /forgot`.
- `/reset` → `200`, form `token` + `password`, `POST /reset`.
- `/register` → `404` (tidak ada registrasi).
- `/dashboard` tanpa session → `302 /login`.
- `/blog/5` → artikel “Hardening Header Parsing & Mail Notification Engines”.
