# Image Metadata — Analisis Artefak

[← Overview](57-image-metadata.md) · [Index](index.md)

> **Langkah 2/6 — Analisis Artefak.** ZIP mulai di offset 31197.
>
> **Titik penting:** ZIP mulai di offset 31197.
>
> **Berikutnya:** [Pemulihan Artefak](57-image-metadata-03-pemulihan-artefak.md)

ZIP mulai di offset 31197. Kita potong dari offset itu, lalu buka isinya:

```bash
dd if=evidence.png of=/tmp/metadata-trailer.zip bs=1 skip=31197 status=none
unzip -l /tmp/metadata-trailer.zip
```

```text
passwords.txt
flag.txt
```

`flag.txt` terenkripsi. `passwords.txt` berisi daftar kandidat password.
