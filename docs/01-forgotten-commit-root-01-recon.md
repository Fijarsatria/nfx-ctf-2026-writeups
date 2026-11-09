# Forgotten Commit (Root) — Recon

[← Overview](01-forgotten-commit-root.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> Setelah mendapatkan akses user, lanjutkan enumerasi pada mesin target.
> Temukan jalur eskalasi yang tersisa, dapatkan akses root, lalu baca root.txt.
>
> Target: `10.10.20.21`

Challenge ini adalah tahap Root dari rangkaian **Forgotten Commit**. Flag root
berada di `/root/root.txt`; user flag di `/home/leonardo/user.txt` adalah
prasyarat yang harus dilewati lebih dulu.

### 1.2 File / service yang diberikan

| File/Service | Ukuran/Endpoint | Keterangan |
|---|---|---|
| `NFX/b2r/labs/bastion` | TCP, dari platform | Pintu masuk peserta |
| `NFX/b2r/labs/21` | `10.10.20.21` | Target: nginx :80, OpenSSH :22 |
| `umum/Boot To Root/forgotten-commit-root/BRIEF.md` | 26 baris | Deskripsi + service |
| `umum/Boot To Root/forgotten-commit-root/challenge.json` | 44 baris | Metadata platform |

Tidak ada attachment binary. Challenge sepenuhnya berupa live service.

### 1.3 Environment

- Bastion: `10.10.20.10` (SSH), dari situ target `10.10.20.21` diakses.
- Tools: `nmap`, `curl`, `git`, `git-dumper`, `ssh`, `fzf` (di target).
- Tidak ada kredensial awal. Kredensial didapat dari history Git.

### 1.4 Triage awal

`[REKONSTRUKSI]` Perintah yang dijalankan pertama kali:

```bash
nmap -Pn -sV -p- --min-rate 2000 10.10.20.21
curl -sS -i http://10.10.20.21/
curl -sS -i http://10.10.20.21/.git/HEAD
```

Hasil yang terdokumentasi di notes:

```text
22/tcp  open  ssh      OpenSSH 8.9p1
80/tcp  open  http     nginx
```

`http://10.10.20.21/` menyajikan situs statis **"Nexus Developer Platform"**.
Direktori `/.git/` dapat diakses dari webroot.

**Catatan operasional.** Pada percobaan awal, container `NFX/b2r/labs/21`
crash-loop: port 22 hanya hidup sekitar 25–1500 ms lalu container mati, dan MAC
berubah tiap ~60 detik. `nx-up` ulang sekitar 11:01 UTC membuat container
stabil; setelah itu port 80 dan 22 tetap terbuka. Tanpa redeploy, SSH tidak
mungkin diselesaikan dalam jendela hidup selama itu.
