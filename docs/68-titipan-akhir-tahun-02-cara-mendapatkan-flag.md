# Titipan Akhir Tahun — Cara mendapatkan flag

[← Overview](68-titipan-akhir-tahun.md) · [Index](index.md)

> **Langkah 2/5.** `doksli.txt` adalah base64 satu lapis.
>
> **Berikutnya:** [Flag](68-titipan-akhir-tahun-03-flag.md)

```bash
pdfdetach -saveall laporan_kegiatan_bulan_desember.pdf
base64 -d doksli.txt
```

Isi file: `TkZYe0QzQzBEM19ENE5EM0MwRDNfTDRHMX0=`

```text
NFX{D3C0D3_D4ND3C0D3_L4G1}
```
