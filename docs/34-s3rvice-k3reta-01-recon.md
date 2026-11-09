# S3rvice K3reta — Recon

[← Overview](34-s3rvice-k3reta.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Kada**
>
> Sebuah kejadian menjadi titik awal dari rangkaian pencarian ini. Telusuri
> informasi yang tersembunyi di balik dokumentasi tersebut, mulai dari
> lokasi, waktu, hingga berbagai jejak digital yang saling berkaitan.
>
> Format: `OSCAR{flag_you_here}` (usang; platform menerima `NFX{...}`)

Tidak ada attachment resmi di platform; gambar yang dipakai adalah:

```text
https://raw.githubusercontent.com/NFCC-Com/qazwsx/refs/heads/main/osint/from_train.jpeg
```

### 1.2 File / service yang diberikan

| File/Service | Ukuran | Keterangan |
|---|---|---|
| `osint/from_train.jpeg` | 296.759 byte | Foto portrait 1200×1600 dari jendela kereta |
| `flags/wave2/S3rvice_K3reta.NOTES.md` | 5.2 KB | Analisis wave 1 (Whoosh/Padalarang) |
| `flags/wave2/S3rvice_K3reta.txt` | 13 byte | `OSCAR{G1008}` (kandidat wave 1) |

Hash:

```bash
$ sha256sum osint/from_train.jpeg
32c0d073ca43bf42133203cc2e10b331c06b40b3a09fab2d7d142b7da917a8fa  from_train.jpeg
```

### 1.3 Environment

- OS: Linux x86-64.
- Tools: `file`, `exiftool`, `sha256sum`, Python 3 (`Pillow`), `tesseract`,
  `zbarimg`, `curl`.
- Service: tidak ada; challenge berbasis gambar + sumber publik (berita,
  jadwal kereta, media sosial).
- Sumber publik: dephub.go.id, investor.id, rmol.id, republika.co.id,
  antaranews.com, tempo.co, Wikipedia, YouTube.

### 1.4 Triage awal

```bash
$ file osint/from_train.jpeg
JPEG image data, JFIF standard 1.01, aspect ratio, progressive, precision 8,
1200x1600, components 3

$ exiftool osint/from_train.jpeg
File Type       : JPEG
Image Width     : 1200
Image Height    : 1600
Encoding Process: Progressive DCT
Color Components: 3
```

**Temuan:**

- Tidak ada EXIF kamera, GPS, timestamp, atau software.
- Tidak ada trailing data setelah EOI.
- `strings` tidak menemukan URL/teks tersembunyi.
- OCR (`tesseract`) tidak menemukan teks yang bisa dibaca.
- Tidak ada QR/barcode (`zbarimg` kosong).

Jadi lokasi harus dibaca dari **isi visual** dan konteks challenge.
