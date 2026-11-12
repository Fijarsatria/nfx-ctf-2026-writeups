# THE BROKEN RESOURCE PARSER — Jejak awal

[← Overview](65-the-broken-resource-parser.md) · [Index](index.md)

> **Langkah 1/5.** ELF non-PIE, tanpa canary. Fungsi `win` ada di `0x4012ae`.
>
> **Berikutnya:** [Cara Mendapatkan Flag](65-the-broken-resource-parser-02-cara-mendapatkan-flag.md)

```bash
unzip TheBrokenResourceParser.zip
file peserta/resparser
nm peserta/resparser | grep ' win$'
```

```text
00000000004012ae t win
```

`main` membaca panjang, lalu blob. `parse_resource` menyalin field nama ke buffer di `rbp-0x30`. Panjang nama boleh sampai `0x100`, jadi return address bisa ditimpa.
