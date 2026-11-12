# Left Behind in the Metadata — Jejak awal

[← Overview](86-left-behind-in-the-metadata.md) · [Index](index.md)

> **Langkah 1/5.** EXIF menyimpan Make, Model, Artist, Serial, GPS, dan `CIPHER:`.
>
> **Berikutnya:** [Cara Mendapatkan Flag](86-left-behind-in-the-metadata-02-cara-mendapatkan-flag.md)

```bash
exiftool drop_point.jpg
```

```text
Make            : NFX-Imaging-Corp
Camera Model    : FieldCam-X9
Artist          : @nfx_courier_07
Serial Number   : NFX-SN-8842109
GPS             : 6 deg 10' 31.08" S, 106 deg 49' 36.84" E
User Comment    : CIPHER:98e8be19...ae22
```

Bentuk desimal koordinat itu adalah `-6.1753,106.8269` (Monas, Jakarta).
