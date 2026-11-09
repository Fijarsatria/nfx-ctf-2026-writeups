# insider — Analisis

[← Overview](06-insider.md) · [Index](index.md)

### 2.1 Struktur profil

```text
ChromeProfile/Default/
├── Bookmarks
├── History
├── Login Data
├── Network/Cookies
├── Preferences
├── Secure Preferences
├── Web Data
└── Extensions/
    ├── ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.92.1_0  (Google Docs Offline)
    └── mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0  (ZenVPN)
```

Profil atas nama **Noah Fox** (`n.fox@nfx-aero.example`), sesuai acquisition note.

### 2.2 History: aktivitas tersangka

Query:

```python
import sqlite3
con = sqlite3.connect('file:ChromeProfile/Default/History?mode=ro', uri=True)
for row in con.execute('select url,title,visit_count,last_visit_time from urls order by last_visit_time'):
    print(row)
```

Output (timestamp dikonversi):

```text
2025-03-11 20:15:00 UTC | YouTube
2025-03-11 20:16:00 UTC | https://www.youtube.com/watch?v=dQw4w9WgXcQ
2025-03-12 07:45:00 UTC | https://news.ycombinator.com/
2025-03-12 07:50:00 UTC | https://www.starlink.com/
2025-03-12 10:05:00 UTC | https://www.nfx-aero.example/projects/helios  (Project Helios)
2025-03-13 11:00:00 UTC | https://github.com/DFIRDiva/DFIR-Challenge-Images
2025-03-14 13:50:00 UTC | https://mail.google.com/mail/u/0/#inbox
2025-03-14 14:05:12 UTC | https://www.google.com/search?q=windows+uac+bypass+2024
2025-03-14 14:08:22 UTC | https://github.com/hfiref0x/UACME
2025-03-14 14:10:05 UTC | https://nvd.nist.gov/vuln/detail/CVE-2024-21412
2025-03-14 14:12:40 UTC | https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21412
2025-03-14 14:16:00 UTC | https://www.virustotal.com/gui/home/upload
2025-03-14 14:17:00 UTC | https://any.run/
2025-03-14 14:19:30 UTC | https://0x00sec.org/
2025-03-14 14:20:10 UTC | https://0x00sec.org/t/windows-uac-bypass-2024/28471
2025-03-15 09:12:00 UTC | https://www.google.com/search?q=singapore+changi+airport+terminal+3+wifi
```

Timeline menunjukkan:

1. Riset UAC bypass (14 Mar 2025, sekitar 14:05–14:12 UTC).
2. Download tool `UACME` dari GitHub.
3. Membaca CVE-2024-21412 di NVD/MSRC.
4. Membuka 0x00sec dan thread “Windows UAC Bypass 2024”.
5. Keesokan harinya mencari WiFi Terminal 3 Changi — sesuai lokasi penyitaan.

Downloads:

```text
C:\Users\nfox\Downloads\uacme.zip  184299 bytes  2025-03-14 14:18:30 UTC  application/zip
URL chain:
  https://github.com/hfiref0x/UACME/releases/download/v3.7.0/uacme.zip
  https://objects.githubusercontent.com/github-production-release-asset/uacme.zip
```

### 2.3 Login Data: username dan password `v10`

```sql
select origin_url, username_value, password_value, date_created, date_last_used from logins;
```

Output:

```text
https://0x00sec.org/ | user=wraithbyte | len=54 | prefix=b'v10' | created=2025-03-13 09:12:44 UTC
  ciphertext: 7631300a2744d840bcd0a797cc692eccd8da86c217b83ba59c2e61c5e06c1393384809e919a1e3f7a75668cdb0801b2b9679fb195ce2
https://mail.google.com/ | user=n.fox@nfx-aero.example | len=54 | prefix=b'v10'
https://github.com/ | user=nfox-aero | len=54 | prefix=b'v10'
https://twitter.com/ | user=n_fox | len=54 | prefix=b'v10'
```

Format `v10` Chrome (Windows) = `v10` + 12-byte nonce + ciphertext + 16-byte GCM tag, dengan key yang dibungkus DPAPI di `Local State`:

```json
"os_crypt": {
  "encrypted_key": "RFBBUEmk5kiTGCMtGDuTQyNxMvzl99cr96fIpe02niGuCDlcG5fO7YxzDYoiP8rG4IfTDCj9hyWsaCa3LX878rBtByUqJ7rISg6AtDl/Zhu4TRdWdA=="
}
```

Base64-decode menghasilkan prefix `DPAPI` + blob. Karena paket evidence **tidak menyertakan master key DPAPI user/SID**, password `v10` tidak dapat didekripsi dari artefak ini. Uji kunci Linux Chrome (`peanuts`, PBKDF2) juga gagal:

```text
peanuts / saltysalt / 1 iter      -> decrypt_and_verify gagal
peanuts / saltysalt / 1003 iter   -> decrypt_and_verify gagal
```

Yang penting untuk flag bukan password, melainkan **username** `wraithbyte`.

### 2.4 Cookies dan Web Data

Cookies menyimpan `xf_user` untuk `.0x00sec.org` (login forum), `NID` Google, dan `logged_in` GitHub. Web Data autofill memberi identitas:

```text
email   n.fox@nfx-aero.example
name    Noah Fox
company NFX Aerospace
address Helios Ring 7, Jurong Island
tel     +65 8123 4471
```

Alamat “Helios Ring 7, Jurong Island” konsisten dengan narasi Project Helios.

### 2.5 Extension ZenVPN 2.7.1

`Preferences` dan `Secure Preferences` mencatat extension non-webstore:

```json
"name": "ZenVPN",
"version": "2.7.1",
"description": "Lightweight VPN proxy. Routes browser traffic through a remote exit node.",
"permissions": ["proxy", "storage", "tabs", "webRequest", "webRequestAuthProvider"],
"host_permissions": ["<all_urls>"],
"from_webstore": false
```

`background.js`:

```js
const PROXY_CONFIG = {
  mode: "fixed_servers",
  rules: {
    singleProxy: { scheme: "http", host: "sg1.zenvpn.example", port: 8899 },
    bypassList: ["localhost", "127.0.0.1"]
  }
};

chrome.runtime.onInstalled.addListener(() => {
  chrome.proxy.settings.set({ value: PROXY_CONFIG, scope: "regular" });
});
```

Extension ini menjadi komponen `zenvpn271` pada flag. Keberadaannya juga menjelaskan bagaimana trafik browser diarahkan ke exit node Singapura.

### 2.6 Menyusun flag

Timestamp `13386435060000000` (bookmark/search tanggal 14 Mar 2025) dikonversi:

```python
from datetime import datetime, timezone, timedelta
dt = datetime(1601,1,1,tzinfo=timezone.utc) + timedelta(microseconds=13386435060000000)
print(dt.strftime('%Y%m%d'))   # 20250314
```

Komponen:

| Komponen | Nilai | Sumber |
|---|---|---|
| Username forum | `wraithbyte` | `Login Data` → `0x00sec.org` |
| CVE | `cve202421412` | History: CVE-2024-21412 |
| Tanggal | `20250314` | Timestamp bookmark/search 14 Mar 2025 |
| Extension | `zenvpn271` | ZenVPN versi 2.7.1 |

Urutan pada flag:

```text
wraithbyte_cve202421412_20250314_zenvpn271
```
