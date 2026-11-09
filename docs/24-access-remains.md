# Access Remains

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Hard` |
| Poin | `360` |
| Author | `Ariaf` |
| Solves | `8` |
| Tools | python3, exiftool, sage |
| Flag | `NFX{The_Real_Access_Was_Kumiko_All_Along}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Evidence Windows: `SAM`, `SYSTEM`, `SECURITY`, `NTUSER.DAT`, DPAPI masterkey, Credential Manager, dan `Kumiko.zip`.
- `secretsdump` menghasilkan NTLM user `aria` dan `ariaf`; NTLM di-crack menjadi `aria` dan `ariafe006`.
- Password `ariaf` membuka DPAPI masterkey `bb24f650-...`; Credential Manager menyimpan `AccessRemains:WaifuVault` dengan password `KumikoOumae2107!@`.
- Password tersebut membuka `Kumiko.zip` (ZipCrypto). Isinya foto-foto Kumiko dan `note.txt`.
- `note.txt` mengarah ke “one that remembers”; `kumiko03.jpg` memuat overlay teks 32 hex:
  `{3E2D6090E7EEB47D5` + `38FC27AC2789C02}`.
- Hex32 `3E2D6090E7EEB47D538FC27AC2789C02` adalah jawaban Q8, **bukan**
  flag akhir.
- Setelah 8/8 Q&A selesai, platform mengembalikan flag final:
  `NFX{The_Real_Access_Was_Kumiko_All_Along}`.

## Navigasi Halaman

- [Recon](24-access-remains-01-recon.md)
- [Analisis](24-access-remains-02-analisis.md)
- [Eksploitasi / Solver](24-access-remains-03-eksploitasi-solver.md)
- [Alur 8 Sub-Challenge Q&A (verified)](24-access-remains-04-alur-8-sub-challenge-q-a-verified.md)
- [Flag](24-access-remains-05-flag.md)
- [Bukti / Evidence](24-access-remains-06-bukti-evidence.md)
- [Referensi](24-access-remains-07-referensi.md)
