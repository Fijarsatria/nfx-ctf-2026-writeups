# Tempat Belajar — Cara Mendapatkan Flag

[← Overview](85-tempat-belajar.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.**
>
> **Flag final:** `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}`
> **Status:** `VERIFIED`

## 1. Metadata poster

```bash
exiftool -a -u -g1 office.png
```

```text
Author  : Kada
Title   : Dih Office
Comment : 3%4TD'aPBA*Z,QPN
```

`Comment` adalah decoy/password, bukan flag. Dari `Title: Dih Office`, kita
mendapat petunjuk nama **Dihlearn**.

## 2. Instagram

Akun yang terkait:

- `@dihlearn.id` — poster “Digital Hour Learning”.
- `@career.dihlearn.id` — akun karier.

Di Instagram `@dihlearn.id` ada teks **Base64**. Artefak yang berhasil
disimpan (screenshot profil `@career.dihlearn.id`) memuat fragmen Base64 yang
decode ke kandidat lama:

```text
NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}
```

Kandidat ini **ditolak** platform. Flag yang diterima platform berbeda satu
karakter di bagian akhir:

```text
NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}
```

Perbandingan Base64-nya:

| Varian | Base64 | Decode |
|---|---|---|
| Lama | `TkZYe09wM25fUzB1cmMzX1BsNHRGMHJtX0QxaEwzcm5fSjRSIX0=` | `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}` |
| Accepted | `TkZYe09wM25fUzB1cmMzX1BsNHRGMHJtX0QxaEwzcm5fSjRZYX0=` | `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}` |

Fragmen di screenshot dimulai dengan `TkZYe09wM25fUzB1cmMz...`, jadi yang
terbaca dari artefak adalah varian lama. Varian `J4Ya` adalah koreksi yang
diterima platform; respons submit-nya ada di halaman ini.

Perubahan `R!` → `Ya` adalah koreksi yang diterima platform. Flag final yang
dipakai adalah varian accepted; respons submit platform ada di halaman ini.

## 3. Submit ke platform

Flag di-submit lewat form web platform dan diterima:

```text
NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}
CORRECT, BUT ALREADY SOLVED.
```

### Screenshot Instagram

![Profil Instagram @career.dihlearn.id](assets/tempat-belajar/09-instagram-fragments.png)

*Screenshot profil `@career.dihlearn.id` yang memuat fragmen Base64 di bagian atas gambar.*

Fragmen publik di screenshot ini decode ke kandidat lama
`..._J4R!`, dan kandidat itu **ditolak** platform. Flag accepted yang dipakai
di halaman ini adalah `..._J4Ya`; koreksi satu karakter ini dibuktikan oleh
respons platform (`CORRECT, BUT ALREADY SOLVED.`), bukan oleh screenshot
Instagram yang tersimpan.
