# NexaDocs — Jejak awal

[← Overview](79-nexadocs.md) · [Index](index.md)

> **Langkah 1/5.** Daftar akun, lalu uji Brand Studio lewat field `company_name`.
>
> **Berikutnya:** [Cara Mendapatkan Flag](79-nexadocs-02-cara-mendapatkan-flag.md)

```bash
curl -sS -c cookies -H 'ngrok-skip-browser-warning: 1' \
  -d 'full_name=Test&company=TestCo&email=test@example.com&password=password123' \
  "$HOST/register"
```

Response: `302` ke `/dashboard`. Field yang masuk template adalah `company_name` di `POST /studio`.
