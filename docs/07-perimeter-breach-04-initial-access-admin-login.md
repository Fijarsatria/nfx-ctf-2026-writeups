# Perimeter Breach — Initial access — admin login

[← Overview](07-perimeter-breach.md) · [Index](index.md)

## 2.3 Initial access — admin login

`webapp.log`:

```text
[2026-10-10 08:30:21] INFO  auth: login ok user=admin ip=36.80.14.22 pw_attempt="Aroma#Craft2026"
[2026-10-10 13:41:00] WARN  auth: login failed user=admin ip=185.220.101.47 pw_attempt="admin@123"
[2026-10-10 13:41:01] WARN  auth: login failed user=admin ip=185.220.101.47 pw_attempt="aromacraft2024"
...
[2026-10-10 13:42:02] INFO  auth: login ok user=admin ip=185.220.101.47 pw_attempt="Aroma#Craft2026"
[2026-10-10 13:42:55] INFO  upload: file saved name="cache_thumb.php" size=412 by=admin ip=185.220.101.47 mime="image/jpeg"
```

Login admin pertama pukul 08:30 dari `36.80.14.22` adalah admin sah. Penyerang berhasil login pukul **13:42:02** dengan password yang sama, `Aroma#Craft2026` — kemungkinan hasil dump SQLi atau password lemah yang tidak dirotasi.

Nginx mengonfirmasi:

```text
185.220.101.47 - - [10/Oct/2026:13:42:02 +0700] "POST /admin/login.php HTTP/1.1" 302 0 ... "python-requests/2.31.0"
185.220.101.47 - - [10/Oct/2026:13:42:06 +0700] "GET /admin/dashboard.php HTTP/1.1" 200 8841
185.220.101.47 - - [10/Oct/2026:13:42:17 +0700] "GET /admin/upload.php HTTP/1.1" 200 2104
```
