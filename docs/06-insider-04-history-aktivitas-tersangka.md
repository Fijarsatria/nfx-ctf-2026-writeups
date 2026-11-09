# insider — History: aktivitas tersangka

[← Overview](06-insider.md) · [Index](index.md)

## 2.2 History: aktivitas tersangka

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
