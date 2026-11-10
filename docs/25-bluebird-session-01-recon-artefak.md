# Bluebird Session — Recon Artefak

[← Overview](25-bluebird-session.md) · [Index](index.md)

> **Langkah 1/11 — Recon Artefak.** Attachment: BluebirdSession.zip (password nxctf.id) → Evidence.zip → Evidence/.
>
> **Titik penting:** sha256sum login.keyring 423261422632617826.jpg for_nozomi.zip README.txt
>
> **Berikutnya:** [Triage awal](25-bluebird-session-02-triage-awal.md)

## 1.1 Deskripsi challenge

> Author: Ariaf
>
> Sebuah workstation Linux diamankan setelah sebuah kepergian yang sunyi.
>
> Dua user masih tersisa di dalam sistem. Satu tetap tinggal seperti Liz, sementara yang lain meninggalkan jejak seperti seekor blue bird.
>
> Akses yang terlihat sudah tidak lagi tersedia, tetapi shell masih mengingat semuanya.
> Telusuri kedua user tersebut, pulihkan secret yang tersimpan, dan buka kembali sesuatu yang sengaja dilindungi.
>
> Note: Liz dan blue bird tidak pernah benar-benar terpisah.
>
> pass: nxctf.id

## 1.2 File yang diberikan

Attachment: `Bluebird_Session.zip` (password `nxctf.id`) → `Evidence.zip` → `Evidence/`.

Struktur:

```text
Evidence/
├── etc/
│   ├── passwd, shadow, group
│   ├── hostname
│   ├── ssh/{ssh_config,sshd_config}
│   └── sudoers, sudoers.d/README
├── home/
│   ├── mizore/
│   │   ├── .bash_history
│   │   ├── .local/share/keyrings/{login.keyring,user.keystore}
│   │   └── Documents/Ensemble.mp4
│   └── nozomi/
│       ├── .bash_history
│       └── Documents/for_nozomi.zip
├── root/.bash_history
└── var/log/{auth.log,syslog,kern.log,apt/*,dpkg.log}
```

Hash artefak kunci:

```bash
$ sha256sum login.keyring 423261422632617826.jpg for_nozomi.zip README.txt
9aa5f380bb318e691f624beb2d20266cee09eb9b173af600e650a8dd623e1ee8  login.keyring
30c4e827ef1ea7d9cf469968b8efc2f3ae408cebada98a495704bd8eba12fb1d  423261422632617826.jpg
edf81dc2fa244bf5fd803743579add2d27fd8ff373783a2122d8b5df393cb7e6  for_nozomi.zip
f09319de1b54bdae19a4946dee4317710be2d147630b1519dc770d2a1408e3fb  README.txt
```

## 1.3 Environment

- Linux
- `7z` untuk ZIP
- Python 3 + PyCryptodome (`Crypto.Cipher.AES`) untuk keyring
- `crypt` (glibc) untuk verifikasi SHA-512 crypt
- `exiftool`, `file`, `strings`
- `secret-tool`/`gnome-keyring-daemon` tersedia, tetapi parser manual lebih deterministik
