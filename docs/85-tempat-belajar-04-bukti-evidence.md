# Tempat Belajar — Bukti / Evidence

[← Overview](85-tempat-belajar.md) · [Index](index.md)

> **Langkah 4/5 — Bukti / Evidence.**
>
> **Titik penting:** terminal evidence menunjukkan API response `Incorrect flag`.

## Artefak

- `office.png` — metadata `Author=Kada`, `Title=Dih Office`,
  `Comment=3%4TD'aPBA*Z,QPN`.
- Post `@career.dihlearn.id`:
  - `TkZYe09wM25fUzB1cmMzX`
  - `1BsNHRGMG1fRDFoTDNybl9KNFIhfQ`
- Decode: `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}` (ditolak).

## Terminal evidence (real)

![Terminal evidence (real)](assets/tempat-belajar/00b-terminal-evidence.png)

Terminal evidence di atas menampilkan API response:

```text
$ python3 submit_curl.py 0884fecf... 'NFX{Op3n_S0urc3_Pl4tF0m_D1hL34Rn_J4R!}'
(200, {'success': False, 'message': 'Incorrect flag'})
```

Jadi ini adalah **bukti kegagalan**, bukan bukti `CORRECT`.
Halaman `85-tempat-belajar-03-flag.md` dan index sudah dikoreksi ke `OPEN`.

## Artefak teks

Foto poster dan kedua post karier disimpan di folder evidence challenge.
Tidak ada bukti submit sukses untuk Tempat Belajar.
