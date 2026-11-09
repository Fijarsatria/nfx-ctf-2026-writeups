# SymHell — Recon

[← Overview](31-symhell.md) · [Index](index.md)

## 1.1 Deskripsi challenge

> **Author: Ariaf**
>
> Selamat datang di **SymHell**! Ini adalah versi upgrade ekstrem dari
> tantangan Bash Jail. Sistem backend memblokir seluruh Huruf (`a-z`,
> `A-Z`), Angka (`0-9`), karakter Wildcard (`?`, `*`), Hash (`#`), DAN
> Herestrings (`<<<`). Mampukah kamu menyusun perintah Linux dari kombinasi
> simbol murni untuk meloloskan diri dari penjara Bash ini?

## 1.2 File / service

| File/Service | Ukuran/Endpoint | Keterangan |
|---|---|---|
| `forensics/symhell/app.py` | 4.185 byte | Source service |
| Service TCP | `0.0.0.0:1337` (lokal) | Dijalankan dari `app.py` |
| Endpoint publik (referensi) | `s1.nfx.my.id:49501` | Tidak dipakai pada verifikasi ini |

Hash source:

```bash
$ sha256sum forensics/symhell/app.py
392dfcb55a45c00fd61a36b520f31243606fff7d7557711b92d31525e7dd5575  app.py
```

## 1.3 Environment

- OS: Linux x86-64.
- Tools: Python 3, `socket`, `re`, bash.
- Untuk verifikasi lokal, `/flag.txt` dibuat sementara berisi flag yang
  sudah diketahui dari `flags/forensics/symhell.txt`, service dijalankan di
  `127.0.0.1:1337`, lalu `/flag.txt` dihapus kembali. **Tidak ada submit ke
  platform dan tidak ada koneksi ke service remote.**
