# Progress Bar (User) — Strategi

[← Overview](15-progress-bar-user.md) · [Index](index.md)

## 3.1 Strategi

1. Fingerprint PHP 8.4.26 mod_php dan form upload.
2. Siapkan script enumerasi (`/out/c`) dan upload lewat `upload.php`.
3. Jalankan PHP2Shell untuk RCE `www-data` dengan command `sh</out/c`.
4. Baca `/out/recon.txt`, `/out/src.txt`, `/out/ucp.txt`.
5. Dari source, ambil kredensial UCP → automation key.
6. Command injection di automation root untuk membaca user flag.

### Evidence langkah ini

![term-03-internal-services.png](assets/progress-bar-user/term-03-internal-services.png)

*Terminal evidence — `03-internal-services.txt` (arsip transkrip sesi solve).*
