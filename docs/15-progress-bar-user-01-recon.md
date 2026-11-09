# Progress Bar (User) — Recon

[← Overview](15-progress-bar-user.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> Portal transfer file internal ProgressBar baru saja dipindahkan ke server
> produksi. Service baru belum melalui pengujian keamanan yang memadai.
> Temukan jalan masuk dan baca user.txt.
>
> Target: `10.10.20.22`

Fokus challenge User adalah foothold ke server dan membaca
`/home/deploy/user.txt`. Flag root ada di challenge terpisah.

### 1.2 File / service yang diberikan

| File/Service | Ukuran/Endpoint | Keterangan |
|---|---|---|
| `NFX/b2r/labs/bastion` | TCP, dari platform | Pintu masuk peserta |
| `NFX/b2r/labs/22` | `10.10.20.22` | Target |
| `http://10.10.20.22/` | HTTP | Portal upload |
| `http://10.10.20.22/upload.php` | HTTP | Form upload multipart |
| `http://10.10.20.22/out/` | HTTP | Hasil upload/script, web-served |
| `flags/b2r/ProgressBar.NOTES.md` | notes solve | Sumber langkah |

Tidak ada attachment binary. Target berupa live container.

### 1.3 Environment

- Bastion `10.10.20.10`; target `10.10.20.22`.
- Tools: `nmap`, `curl`, `python3`, `php2shell` (9bie/3em0), `ssh` (tidak
  diperlukan untuk foothold).
- Service internal target yang tidak terekspos langsung:
  - `127.0.0.1:3000` — watchtower
  - `127.0.0.1:8080` — telephony UCP
  - `127.0.0.1:9000` — automation (root)

### 1.4 Triage awal

`[REKONSTRUKSI]` Perintah awal:

```bash
nmap -Pn -sV -p- --min-rate 2000 10.10.20.22
curl -sS -i http://10.10.20.22/
curl -sS -i http://10.10.20.22/upload.php
```

Stack yang terdokumentasi di notes:

```text
Apache prefork + mod_php
PHP 8.4.26
display_errors=On
memory_limit=8M
post_max_size=64M
session.upload_progress.enabled=On
satu worker prefork
```

`/upload.php` adalah form upload multipart. Direktori `/out/` dapat diakses
lewat HTTP dan writable oleh `www-data`; ini penting karena exploit hanya bisa
menjalankan command sangat pendek, sehingga payload panjang harus ditaruh
sebagai file.
