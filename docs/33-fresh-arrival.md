# Fresh Arrival

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Osint` |
| Difficulty | `Medium` |
| Poin | `340` |
| Author | `Ariaf` |
| Solves | `9` |
| Tools | curl, python3, exiftool |
| Flag | `NFX{XW_CXH_beijing_raihan}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Foto challenge adalah **Boeing 737-341(SF)**, registrasi **PK-ADL**,
  MSN **26854**, milik **Aero Nusantara Cargo**.
- Foto aslinya ada di JetPhotos, photo ID **11925184**, diambil
  **26 November 2025** di **Jakarta Halim Perdanakusuma (WIHH)** oleh
  **Raihan Al Faris**.
- Thumbnail JetPhotos 400×225 dibandingkan piksel-per-piksel dengan
  `spotted.jpg`: ukuran sama, **MAE ≈ 2,2/255** — hanya re-encoding CDN.
- Riwayat airframe: MSN 26854 pertama diterima oleh **China Xinhua Airlines**
  (B-2908), lalu Yangtze River Express, Suparna Airlines, Central Airlines,
  dan terakhir PK-ADL/Aero Nusantara Cargo.
- China Xinhua Airlines: IATA **XW**, ICAO **CXH**, markas **Beijing**.
- Flag: `NFX{XW_CXH_beijing_raihan}`.

## Navigasi Halaman

- [Recon](33-fresh-arrival-01-recon.md)
- [Analisis](33-fresh-arrival-02-analisis.md)
- [Eksploitasi / Solver](33-fresh-arrival-03-eksploitasi-solver.md)
- [Flag](33-fresh-arrival-04-flag.md)
- [Bukti / Evidence](33-fresh-arrival-05-bukti-evidence.md)
- [Referensi](33-fresh-arrival-06-referensi.md)
