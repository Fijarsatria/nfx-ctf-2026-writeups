# My Lovely Freya — Flag & Verifikasi

[← Overview](29-my-lovely-freya.md) · [Index](index.md)

Plaintext asli di surat:

```text
NXCTF{FR3Y4_MY_L0V3LY!}
```

Flag platform (file `flags/wave2/My_Lovely_Freya.txt`):

```text
NFX{FR3Y4_MY_L0V3LY!}
```

Verifikasi:

- Dekripsi OpenSSL berhasil (`exit=0`), padding valid, plaintext terbaca.
- Isi surat adalah flag dengan prefix `NXCTF`.
- Prefix dinormalisasi ke `NFX` sesuai format challenge/flag file.
- Metadata decoy `AyamgGoreng45` terbukti gagal (`bad decrypt`).

## Flag

`NFX{FR3Y4_MY_L0V3LY!}`

**Status:** `VERIFIED`

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
