# My Lovely Freya — Triage awal

[← Overview](29-my-lovely-freya.md) · [Index](index.md)

## 1.4 Triage awal

```bash
$ file FreyaSayangkuh
FreyaSayangkuh: Zip archive data, at least v2.0 to extract, compression method=deflate

$ file freya_sayangkuh.png
PNG image data, 1024 x 1200, 8-bit/color RGB, non-interlaced

$ exiftool freya_sayangkuh.png
...
Image Width                     : 1024
Image Height                    : 1200
Secret                          : QXlhbWdHb3Jlbmc0NQ==
Image Size                      : 1024x1200
```

Metadata `Secret`:

```bash
$ python3 - <<'EOF'
import base64
print(base64.b64decode("QXlhbWdHb3Jlbmc0NQ==").decode())
EOF
AyamgGoreng45
```

Sekilas ini terlihat seperti password. Namun percobaan dekripsi dengan
`AyamgGoreng45` menghasilkan `bad decrypt`, jadi metadata ini adalah decoy
(perhatikan: hilang huruf `H` di depan dan `@` di akhir).
