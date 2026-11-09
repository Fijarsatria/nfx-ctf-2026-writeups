# Progress Bar (Root) — Strategi

[← Overview](14-progress-bar-root.md) · [Index](index.md)

## 3.1 Strategi

1. Dapatkan RCE `www-data` lewat PHP2Shell.
2. Upload script enumerasi ke `/out/c`, jalankan `sh</out/c`.
3. Baca source `/opt` dan konfigurasi loopback.
4. Ambil kredensial UCP dari watchtower.
5. Ambil automation key dari inbox UCP.
6. Kirim payload command injection ke automation root.
7. Baca `/root/root.txt`.

### Evidence langkah ini

![term-03-privesc.png](assets/progress-bar-root/term-03-privesc.png)

*Terminal evidence — `03-privesc.txt` (arsip transkrip sesi solve).*
