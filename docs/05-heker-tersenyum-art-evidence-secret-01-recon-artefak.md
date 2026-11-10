# Heker Tersenyum - Art Evidence Secret — Recon Artefak

[← Overview](05-heker-tersenyum-art-evidence-secret.md) · [Index](index.md)

## 1.1 Deskripsi challenge

> Author: salep88
>
> Dia tampak senyum, namun dia menyembunyikan sesuatu dibalik gambar itu.
> Dia anggota heker dari tim Lampung Siber Brotherhood (LSB).
> Ada secret yang tidak bisa dia beritahu ke siapapun.
> Pakaian dia memakai baju berwarna merah dan celana berwarna biru.
> Perhatikan nama tim dia dan pakaian dia.
>
> Format Flag: NFX{your_flag_here}

Petunjuk yang benar-benar dipakai:

| Petunjuk | Interpretasi |
|---|---|
| “LSB” | Least Significant Bit |
| “baju merah” | kanal **R** (red) |
| “celana biru” | kanal **B** (blue) |
| “The smallest details matter.” | bit paling kecil / LSB |
| `PhotoLocation` base64 | pesan tambahan dan password `Kukuriuk99` |

## 1.2 File yang diberikan

| File | Ukuran | Keterangan |
|---|---:|---|
| `view` (hasil unduhan Google Drive) | 84.783 byte | **HTML** halaman Google Drive, bukan gambar |
| `file` (attachment asli, tersimpan di `work/event/forensics/.../file`) | 774.601 byte | PNG 1495×2424 RGB |
| `assets/heker-tersenyum-art-evidence-secret/00-original.png` | 774.601 byte | salinan artefak untuk analisis |

`file view` pada awalnya menipu:

```bash
$ file view
view: HTML document, ASCII text, with very long lines (63386)
```

HTML tersebut adalah halaman viewer Google Drive. Artefak sebenarnya diunduh sebagai `file`:

```bash
$ file file
file: PNG image data, 1495 x 2424, 8-bit/color RGB, non-interlaced
```

Hash:

```bash
$ sha256sum file
1d349bbff6ba8f9bfd85fbf6980d098b5d810035395f3477d463526b11b2c4a1  file
```

## 1.3 Environment

- OS: Linux
- Tools: `file`, `exiftool`, `zsteg`, `strings`, `xxd`, Python 3 + Pillow
- `binwalk` di mesin ini error karena mismatch capstone (`CS_ARCH_ARM64`), jadi struktur PNG diperiksa manual dengan parser chunk Python.

### Evidence langkah ini

![term-06-file-exiftool.png](assets/heker-tersenyum-art-evidence-secret/term-06-file-exiftool.png)

*Terminal evidence — `06-file-exiftool.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`06-file-exiftool.txt`](assets/heker-tersenyum-art-evidence-secret/06-file-exiftool.txt)
