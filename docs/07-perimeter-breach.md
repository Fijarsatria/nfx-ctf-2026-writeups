# Perimeter Breach

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `Ariaf` |
| Tools | gobuster, sqlmap, python3, tshark, git |
| Flag | `NFX{P4th_1nt0_Pr0duct10n}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Tiga log (`access.log` Nginx, `auth.log` syslog, `webapp.log`) merekam satu kampanye serangan dari **185.220.101.47** pada 10 Oktober 2026.
- Rekon: `gobuster/3.6` (13:02), SQL injection `sqlmap/1.7.2` pada `products.php?id=` (13:15), dump tabel `users`.
- Initial access: login admin berhasil pada **13:42:02** dengan password `Aroma#Craft2026`.
- Webshell: upload `cache_thumb.php` (412 byte, MIME `image/jpeg`) ke `/uploads/`, dieksekusi lewat `?c=` untuk `whoami`, `id`, `cat /etc/passwd`, `cat /home/deploy/.env`.
- Lateral movement: SSH password sebagai `deploy` dari IP penyerang (14:20:03).
- Persistence: `deploy` membuat user **`svc_backup`** (UID 1002, group sudo), mengganti password, lalu login SSH publickey sebagai `svc_backup` (14:41:27).
- Flag: `NFX{P4th_1nt0_Pr0duct10n}`.

## Navigasi Halaman

- [Recon](07-perimeter-breach-01-recon.md)
- [Analisis](07-perimeter-breach-02-analisis.md)
- [Eksploitasi / Solver](07-perimeter-breach-03-eksploitasi-solver.md)
- [Flag](07-perimeter-breach-04-flag.md)
- [Bukti / Evidence](07-perimeter-breach-05-bukti-evidence.md)
- [Referensi](07-perimeter-breach-06-referensi.md)
