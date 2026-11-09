# My Lovely Freya

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Hard` |
| Poin | `320` |
| Author | `salep88` |
| Solves | `10` |
| Flag | `NFX{FR3Y4_MY_L0V3LY!}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Attachment `FreyaSayangkuh` adalah **ZIP** berisi `freya_sayangkuh.png`
  dan `surat_untuk_freya.enc`.
- PNG mendeklarasikan tinggi **1200** baris, tetapi IDAT sebenarnya berisi
  **1536** baris. Ada **336 baris tersembunyi** di bawah gambar yang tidak
  pernah ditampilkan viewer PNG normal.
- Baris tersembunyi berisi gambar teks password:
  `<!HayamGoreng45@/>`.
- Metadata PNG `Secret: QXlhbWdHb3Jlbmc0NQ==` adalah **decoy**; decode-nya
  `AyamgGoreng45` dan gagal dipakai untuk dekripsi.
- `surat_untuk_freya.enc` adalah format OpenSSL `Salted__`; dekripsi dengan
  **AES-256-CBC, PBKDF2, 100.000 iterasi, digest SHA-256**, password
  `<!HayamGoreng45@/>` menghasilkan surat:
  `NXCTF{FR3Y4_MY_L0V3LY!}`.
- Flag platform: `NFX{FR3Y4_MY_L0V3LY!}`.

## Navigasi Halaman

- [Recon](29-my-lovely-freya-01-recon.md)
- [Analisis](29-my-lovely-freya-02-analisis.md)
- [Eksploitasi / Solver](29-my-lovely-freya-03-eksploitasi-solver.md)
- [Flag](29-my-lovely-freya-04-flag.md)
- [Bukti / Evidence](29-my-lovely-freya-05-bukti-evidence.md)
- [Referensi](29-my-lovely-freya-06-referensi.md)
