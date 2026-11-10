# Dokodemo Door — Ekstraksi teks dari PDF

[← Overview](28-dokodemo-door.md) · [Index](index.md)

## 2.4 Ekstraksi teks dari PDF

PDF dibuat dengan ReportLab. Content stream halaman memakai filter
`[/ASCII85Decode /FlateDecode]`. Setelah decode, operator `Tj` berisi teks:

```text
[ NFX PROTOCOL // RESTRICTED ACCESS ]
DOKODEMO DOOR
Sandi Rahasia Gerbang Masuk Sektor Barat
Di balik pintu ini terdapat akses langsung menuju jaringan rahasia NFX.
Hanya mereka yang memiliki otentikasi sah yang diperkenankan masuk.
Ketuk tiga kali pada pintu dan bisikkan kode otorisasi:
Flag: NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}
Gunakan flag di atas untuk melakukan submission pada platform CTF.
NFX CLASSIFIED ARCHIVE // STRICTLY CONFIDENTIAL // DO NOT DISTRIBUTE
```

Flag muncul sebagai teks biasa di halaman PDF.

### Evidence langkah ini

![term-02-extracted-text.png](assets/dokodemo-door/term-02-extracted-text.png)

*Terminal evidence — `02-extracted-text.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`02-extracted-text.txt`](assets/dokodemo-door/02-extracted-text.txt)
