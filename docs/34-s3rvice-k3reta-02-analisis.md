# S3rvice K3reta — Analisis

[← Overview](34-s3rvice-k3reta.md) · [Index](index.md)

### 2.1 Membaca gambar

Elemen visual utama:

- Foto diambil dari **kereta yang berada di atas viaduk/embankment**;
  terlihat atap rumah dan deretan polybag putih di bawah.
- Latar tengah: **sawah** dan kebun di lembah.
- Latar jauh: **kompleks perumahan** dengan atap gelap dan dinding putih,
  bangunan besar berwarna putih, serta **tower transmisi** dan tower
  telekomunikasi.
- Langit biru dengan awan; matahari rendah (pagi/sore).

Kombinasi “viaduk kereta + sawah + perumahan lereng + tower transmisi” cocok
dengan jalur KRL Bogor Line di petak **Cilebut–Bojong Gede**, Kabupaten
Bogor. Jalur ini berada di atas tebing/embankment, dengan sawah dan
perumahan di sekitarnya.

### 2.2 Menentukan kejadian

Dari konteks lokasi dan Q&A yang sudah diketahui, kejadiannya adalah
**tanah longsor tebingan rel kereta** di:

```text
KM 45+4/5 (piket 400-500)
antara Stasiun Cilebut dan Stasiun Bojong Gede
Rabu, 21 November 2012, sekitar pukul 16.30–17.50 WIB
```

Dampak yang diberitakan:

- Rel sepanjang **±200 meter** amblas/menggantung.
- **4 tiang listrik aliran atas (LAA)** roboh.
- **19–22 rumah** warga tertimbun/rusak.
- **98 perjalanan** KA dari Stasiun Bogor dibatalkan.
- Tidak ada korban jiwa; warga diungsikan.
- Perbaikan diperkirakan **21 hari**.

### 2.3 Q1–Q13: jawaban dan verifikasi

| No | Pertanyaan (inti) | Jawaban | Sumber / status |
|---|---|---|---|
| Q1 | Penyebab kejadian | **longsor** | dephub, investor.id, rmol — kuat |
| Q2 | Kilometer | **45+4/5** | investor.id, rmol — kuat |
| Q3 | Petak / antar stasiun | **Cilebut - Bojong Gede** | dephub, investor.id, rmol — kuat |
| Q4 | Tanggal | **21/11/2012** | dephub, rmol — kuat |
| Q5 | Jumlah perjalanan dibatalkan | **98** | rmol, republika — kuat |
| Q6 | Panjang rel amblas | **200 M** | investor.id, rmol, republika — kuat |
| Q7 | Alat berat / excavator rel | **Atlas** | Q&A benar; sumber publik tentatif |
| Q8 | Nomor kereta / rangkaian | **6007** | Q&A benar; sumber publik tentatif |
| Q9 | Akun media sosial “abang drone” | **fandi_8510** | post TikTok `@fandi_8510` |
| Q10 | Tanggal post | **01/02/2026** | timestamp post |
| Q11 | Tempat servis favorit | **Rofi Servis Drone Bogor** | `@rofi_servis` |
| Q12 | Plus Code tempat servis | **7R73+FM7** | Google Maps Ciburuy/Cigombong |
| Q13 | Nama YouTube | **RofiServis** | channel YouTube tempat servis |

Kutipan sumber penting:

```text
dephub.go.id (12/12/2012):
"berhati-hati pada saat melintasi KM 45 antara Stasiun Cilebut dengan
Stasiun Bojonggede."
"peristiwa longsor terjadi pada Rabu 21 November 2012."

investor.id / Antara (22/11/2012):
"longsor tebing ... di antara Stasiun Cilebut dan Bojonggede tepatnya di
kilometer 45+4/5 (petir 400-500)"
"rel KA sepanjang kurang lebih 200 meter amblas dan empat tiang listrik
aliran atas roboh, dan menimbun 19 rumah warga"

rmol.id (22/11/2012):
"dibatalkannya 98 perjalanan rute KA Bogor-Jakarta."
"rel sepanjang 200 meter 'menggantung'."
```

### 2.4 Q7 “Atlas” dan Q8 “6007”

Dua jawaban ini berasal dari sesi Q&A yang sudah dijawab benar. Padanan
sumber publiknya belum 100% terkonfirmasi:

- **Atlas**: Atlas memproduksi **excavator rel** (mis. Atlas 1604 ZW).
  Foto Tempo 25 November 2012 menampilkan “kereta lokomotif ekskavator”
  saat uji coba jalur pascalongsor, sehingga “Atlas” masuk akal sebagai
  alat berat/excavator rel yang dipakai di lokasi.
- **6007**: `KuMoHa 6007` adalah kereta terakhir dalam formasi 6 kereta
  Tokyo Metro/Toei 6000. Rangkaian khusus wanita yang diuji coba pada
  26 November 2012 menggunakan formasi yang berakhiran `KuMoHa 6007`
  (Wikipedia). Ini kandidat kuat untuk “nomor kereta/rangkaian”, tetapi
  hubungan langsung dengan uji coba 26 November 2012 belum dikonfirmasi
  penuh.

Karena Q7/Q8 sudah dinyatakan benar pada Q&A, writeup ini mencatatnya
sebagai jawaban yang diketahui, bukan sebagai tebakan baru.

### 2.5 Reverse image search

Karena metadata kosong, dilakukan reverse image search:

- **Yandex Images** (upload file) mengembalikan “similar images” generik
  (sawah, desa, Bali, Filipina) dan **tidak ada situs sumber** yang cocok.
- **Google Lens** diblokir dari environment ini (captcha/unusual traffic).
- **Bing Visual Search** menolak URL gambar eksternal.

Kesimpulan sementara: gambar tidak terindeks sebagai foto publik, atau
merupakan screenshot/AI-generated yang tidak punya sumber langsung. Ini
membuat Q9 tidak bisa diselesaikan hanya dengan reverse image search;
harus lewat pencarian kontekstual (video drone di lokasi yang sama) dan
verifikasi akun media sosial.

### 2.6 Q9–Q13: dari post TikTok ke Plus Code

Sumber yang dimaksud ternyata **post TikTok `@fandi_8510`** (display name
`Fandi27`, bio “Bogor | DJI Drone”), dengan caption:

> “longsoran Cilebut … In 2012 there was a big landslide here, the journey of
> the KRL was paralyzed, and now it can be passed at maximum speed.”
> `#commuterline #djidrone #explorebogor #bojonggede #cilebut`

Tanggal post yang terlihat: **1 Februari 2026** (`01/02/2026`).

| No | Pertanyaan | Jawaban | Bukti |
|---|---|---|---|
| Q9 | Nama akun media sosial abang drone? `(xxxxx_xxxx)` | **`fandi_8510`** | handle TikTok `@fandi_8510`; pola 5 huruf + `_` + 4 digit |
| Q10 | Kapan postingan abang itu di-post? `(xx/xx/xxxx)` | **`01/02/2026`** | timestamp post TikTok |
| Q11 | Apa nama tempat servis favoritnya? `(Xxxx Xxxxxx Xxxxx Xxxxx)` | **`Rofi Servis Drone Bogor`** | bio/repost `@rofi_servis`; caption “servis drone Bogor” |
| Q12 | Apa Plus Code tempat tersebut? `(XXXX+XXX)` | **`7R73+FM7`** | Google Maps “Toko Rofi Servis, Servis Drone, Servis HP”, Ciburuy/Cigombong; short code `7R73+FM`, presisi 11 = `7R73+FM7` |
| Q13 | Nama YouTube dia? `(XxxxXxxxxx)` | **`RofiServis`** | channel YouTube tempat servis; pola 4+6 |

**Flag final:**

```text
NFX{Dr0n3_T3rb41k_T3mp4t_S3rv1c3_T3rb41k_J4uh_B4ng3T_BTW_B4ng_R0f1_K3r3n_S3rb4_b1s4}
```

Diverifikasi lewat `submit_sub_challenges` / `get_sub_challenges` (semua
Q1–Q13 `true`) dan disubmit ke platform: **`Correct! +480 points.`**
