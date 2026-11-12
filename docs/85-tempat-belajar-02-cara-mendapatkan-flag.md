# Tempat Belajar — Cara Mendapatkan Flag

[← Overview](85-tempat-belajar.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.**
>
> **Kandidat:** `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}`
> **Status:** `OPEN / CANDIDATE — ditolak platform`

## 1. Metadata poster

```bash
exiftool -a -u -g1 office.png
```

```text
Author  : Kada
Title   : Dih Office
Comment : 3%4TD'aPBA*Z,QPN
```

`Comment` terlihat seperti password acak. Diuji sebagai password Gmail
`dihlearn.id@gmail.com` → **wrong password**; sebagai password Instagram
`@dihlearn.id` login diarahkan ke reCAPTCHA (belum berhasil ditembus).

## 2. Akun Instagram

- `@dihlearn.id` — poster “Digital Hour Learning”, 3 post, bio
  “DIHLEARN - Pembelajaran Digital | Belajar teruss | interaktif platform belajar”.
- `@career.dihlearn.id` — akun karier, 2 post, masing-masing menyembunyikan
  base64 di bagian atas gambar.

Fragmen base64:

```text
Post 1: TkZYe09wM25fUzB1cmMzX
Post 2: 1BsNHRGMG1fRDFoTDNybl9KNFIhfQ
```

Gabung dan decode:

```bash
printf '%s%s' 'TkZYe09wM25fUzB1cmMzX' '1BsNHRGMG1fRDFoTDNybl9KNFIhfQ' | base64 -d
```

```text
NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}
```

## 3. Submit ke platform

Kandidat di atas **ditolak**. Varian corrected yang juga dicoba dan ditolak:

```text
NFX{Op3n_S0urc3_Pl4tF0rm_D1hL34rn_J4R!}
NFX{Op3n_S0urc3_Pl4tF0m_D1hL34rn_J4R!}
NFX{Op3n_S0urc3_Pl4tF0rm_D1hL3rn_J4R!}
NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R}
```

Screenshot `assets/tempat-belajar/00b-terminal-evidence.png` justru menampilkan
**`INCORRECT FLAG`** untuk kandidat `D1hL34Rn` — bukan `CORRECT`.

## 4. Langkah berikutnya (belum selesai)

- Login Instagram `@dihlearn.id` untuk membaca DM. Password kandidat:
  `3%4TD'aPBA*Z,QPN`; login dijegal reCAPTCHA (perlu IP residential/Azure VM
  atau penyelesaian reCAPTCHA).
- Cek apakah flag ada di DM, arsip, atau story akun.
- `total_solves = 1` (Kaens), jadi flag accepted memang ada.

> **Jangan** mengklaim flag ini valid sebelum submit asli berhasil.
