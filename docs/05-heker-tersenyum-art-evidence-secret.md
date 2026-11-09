# Heker Tersenyum - Art Evidence Secret

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `280` |
| Author | `salep88` |
| Flag | `NFX{LSB_3ASY_OR_H4RD_IDK}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Attachment berupa PNG 1495×2424 yang seluruhnya grayscale, tetapi metadata `tEXt` menyimpan dua petunjuk: komentar “The smallest details matter.” dan `PhotoLocation` berisi base64 bertingkat.
- Decode base64 dua lapis menghasilkan lokasi fiktif dan string `Kukuriuk99` — petunjuk/password, bukan flag.
- Nama tim **LSB** + “baju merah, celana biru” adalah arahan langsung: baca **LSB channel Red dan Blue**.
- Ekstraksi LSB row-major dari kanal R dan B masing-masing menghasilkan container `CTF1` + panjang big-endian + payload biner.
- Container R berisi 108 byte payload, container B berisi 53 byte; keduanya high-entropy (tidak langsung terbaca sebagai teks).
- Flag final yang tercatat untuk challenge ini adalah `NFX{LSB_3ASY_OR_H4RD_IDK}`.

## Navigasi Halaman

- [Recon](05-heker-tersenyum-art-evidence-secret-01-recon.md)
- [Analisis](05-heker-tersenyum-art-evidence-secret-02-analisis.md)
- [Eksploitasi / Solver](05-heker-tersenyum-art-evidence-secret-03-eksploitasi-solver.md)
- [Flag](05-heker-tersenyum-art-evidence-secret-04-flag.md)
- [Bukti / Evidence](05-heker-tersenyum-art-evidence-secret-05-bukti-evidence.md)
- [Referensi](05-heker-tersenyum-art-evidence-secret-06-referensi.md)
