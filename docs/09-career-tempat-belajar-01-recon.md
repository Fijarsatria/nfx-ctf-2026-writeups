# Career Tempat Belajar — Recon

[← Overview](09-career-tempat-belajar.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Kada**
>
> Tempat Belajar itu sedang sedang membuka beberapa lowongan pekerjaan untuk
> tim teknologi dan keamanan siber.
>
> Bisakah kamu melakukan penelusuran informasi untuk menemukan jejak digital
> dan profil tempat belajar itu hingga menemukan hal yang anda cari di
> platform G-R?
>
> Format: `NFX{your_flag_here}`

Petunjuk penting:

- “Tempat Belajar” bukan nama perusahaan literal; ini adalah frasa yang
  dipakai untuk menyamarkan sebuah platform belajar.
- “platform G-R” hampir pasti **Gravatar** (G-R), platform profil global yang
  di-key oleh hash MD5 email.
- Poster yang diberikan memuat branding yang bisa dicari.

### 1.2 File / service yang diberikan

| File/Service | Ukuran | Keterangan |
|---|---|---|
| `osint/office.png` | 3.186.772 byte | Poster “DIGITAL HOUR LEARNING”, 1824×2346 |
| `umum/Osint/career-tempat-belajar/BRIEF.md` | 1.1 KB | Deskripsi + format flag |
| `umum/Osint/career-tempat-belajar/challenge.json` | 1.5 KB | Metadata challenge |

Hash:

```bash
$ sha256sum osint/office.png
f531e041cff71d858f2215ee97bcb2dd40429cf35e3264818c0fde676e2621f9  osint/office.png
```

### 1.3 Environment

- OS: Linux x86-64.
- Tools: `file`, `exiftool`, `sha256sum`, Python 3, `curl`, `Pillow`.
- Service: tidak ada service jaringan yang diberikan; challenge sepenuhnya
  OSINT dari artefak gambar + sumber publik.
- Endpoint publik yang dipakai: Instagram (login-walled), Gravatar API,
  mesin pencari.

### 1.4 Triage awal

```bash
$ file osint/office.png
PNG image data, 1824 x 2346, 8-bit/color RGB, non-interlaced

$ exiftool osint/office.png
Author      : Kada
Comment     : 3%4TD'aPBA*Z,QPN
Title       : Dih Office
Image Size  : 1824x2346
```

**Temuan:** selain teks visual “DIGITAL HOUR LEARNING”, metadata PNG
mengandung:

- `Author: Kada` — sesuai author challenge.
- `Title: Dih Office` — “Dih” adalah singkatan **Dihlearn**.
- `Comment: 3%4TD'aPBA*Z,QPN` — terlihat seperti password, tetapi sudah diuji
  dan **bukan** password Instagram. Ini decoy.

PNG hanya berisi chunk standar (`IHDR`, `tEXt`, banyak `IDAT`, `IEND`); tidak
ada data trailing atau chunk aneh:

```text
IHDR 13
tEXt 11   Author\0Kada
tEXt 24   Comment\03%4TD'aPBA*Z,QPN
tEXt 16   Title\0Dih Office
IDAT ...  (banyak)
IEND 0
```
