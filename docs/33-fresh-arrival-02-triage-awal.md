# Fresh Arrival — Triage awal

[← Overview](33-fresh-arrival.md) · [Index](index.md)

## 1.4 Triage awal

```bash
$ file osint/spotted.jpg
JPEG image data, JFIF standard 1.01, aspect ratio, baseline, precision 8,
400x225, components 3

$ exiftool osint/spotted.jpg
File Type        : JPEG
Image Width      : 400
Image Height     : 225
Encoding Process : Baseline DCT
Color Components : 3
```

**Temuan:** tidak ada EXIF kamera, GPS, atau timestamp. Yang tersisa hanya
profil warna sRGB standar. Jadi jalur yang tersedia adalah **reverse image
search** dan pembacaan livery/registrasi dari gambar.
