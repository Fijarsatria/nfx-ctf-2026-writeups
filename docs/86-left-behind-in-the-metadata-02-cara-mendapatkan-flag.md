# Left Behind in the Metadata — Flag & Verifikasi

[← Overview](86-left-behind-in-the-metadata.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.** Cara Mendapatkan Flag
>
> **Titik penting:** NFXCTF{3x1f_gp5_m3t4_tr4c3_9f41c8b2e70d}
>
> **Berikutnya:** [Flag](86-left-behind-in-the-metadata-03-flag.md)

> **Flag:** `NFXCTF{3x1f_gp5_m3t4_tr4c3_9f41c8b2e70d}`
> **Status:** `VERIFIED`

1. Baca EXIF dengan `exiftool drop_point.jpg`.
2. Susun key dari Make|Model|Artist|Serial|GPS.
3. Decrypt UserComment pakai key tersebut.

### Bukti submit di platform

![00b-submit-platform.png](assets/left-behind-in-the-metadata/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Bukti submit:** screenshot form challenge di atas menampilkan `CORRECT, BUT ALREADY SOLVED.`
