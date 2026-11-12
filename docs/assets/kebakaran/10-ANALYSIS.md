# Kebakaran — analisis lokasi (2026-11-13)

## Yang ada di file

```text
kebakaran.jpeg
776x1030, JPEG, 30 KB
Date/Time Original: 2026:10:25 03:59:00+07:00
```

`exiftool -a -u -g1` **tidak** menemukan GPS, komentar, XMP, atau
nama tempat. `strings`, `binwalk`, dan `zsteg` juga tidak menemukan payload
tersembunyi. Yang terlihat di foto hanya gang malam, tembok bergrafiti,
lampu, dan api di ujung gang.

## Flag yang diterima

```text
NXCTF{GLORIA_SETIABAKTI_SINARHARAPAN}
```

Dengan aturan brief (urut alfabet, tanpa "Toko", tanpa spasi, kapital,
dipisah `_`), tiga usaha itu adalah:

1. Gloria
2. Setiabakti
3. Sinarharapan

## Pencarian lokasi

Yang dicoba:

- `exiftool -a -u -g1` — tidak ada koordinat.
- Nominatim `Setiabakti` — hasil berupa jalan di Bandar Muadzam Shah,
  Malaysia, bukan cluster toko di Jawa Barat.
- Nominatim `Sinarharapan` — hasil berupa desa di Gorontalo.
- Overpass API query nama `Gloria|Setiabakti|Sinarharapan` — endpoint
  mengembalikan 406/timeout, tidak menghasilkan cluster.
- Bing/DuckDuckGo query nama toko + kebakaran — tidak ada hasil relevan.

## Kesimpulan

Tidak ada bukti Street View, koordinat gang, atau frame papan toko di arsip.
Yang bisa diverifikasi hanya:

- foto malam bertanggal 25 Oktober 2026 03:59 +07:00;
- flag accepted yang memecah menjadi tiga nama usaha.

**Jangan mengarang lokasi atau Street View.** Kalau nanti ada frame Street
View sebelum kejadian, tambahkan koordinat + tiga papan toko ke halaman ini.

## File

- `kebakaran.jpeg` — foto asli
- `ANALYSIS.md` — catatan ini
