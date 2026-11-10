# Fresh Arrival — Analisis Jejak

[← Overview](33-fresh-arrival.md) · [Index](index.md)

## 2.1 Identifikasi pesawat dari gambar

Detail yang bisa dibaca:

- Livery putih di depan, nacelle mesin merah, ekor/pixel biru-warni.
- Registrasi pada pintu/gear door terbaca **PK-ADL**.
- Konfigurasi kargo (737 Classic freighter).

Reverse image search (Yandex) mengembalikan foto-foto **Central Airlines**
Boeing 737, lalu mengarah ke airframe:

```text
PK-ADL / B-2908
Boeing 737-341(SF)
MSN 26854
Line number 2303
```

## 2.2 Menemukan foto asli dan fotografer

JetPhotos photo ID **11925184**:

```text
Title      : PK-ADL | Boeing 737-341(SF) | Aero Nusantara Cargo |
             Raihan Al Faris | JetPhotos
Reg        : PK-ADL
Aircraft   : Boeing 737-341(SF)
Serial #   : 26854
Airline    : Aero Nusantara Cargo
Photo date : Nov 26, 2025
Uploaded   : Dec 09, 2025
Location   : Jakarta Halim Perdanakusuma Int'l - WIHH, Indonesia
Photo by   : Raihan Al Faris
```

URL halaman:

```text
https://www.jetphotos.com/photo/11925184
```

Thumbnail CDN:

```text
https://cdn.jetphotos.com/400/5/477464_1765274878.jpg
```

## 2.3 Membuktikan foto challenge = foto JetPhotos

Thumbnail 400×225 diunduh dan dibandingkan dengan `spotted.jpg`:

```python
from PIL import Image
import numpy as np

a = Image.open("osint/spotted.jpg").convert("RGB")
b = Image.open("jetphotos_11925184.jpg").convert("RGB")
x = np.asarray(a, dtype=np.int16)
y = np.asarray(b, dtype=np.int16)
d = np.abs(x - y)

print("sizes:", a.size, b.size)
print("MAE  :", d.mean())
print("max  :", d.max())
print("identical pixels:", (d.sum(axis=2) == 0).mean() * 100)
```

Output:

```text
sizes: (400, 225) (400, 225)
MAE  : 2.209522222222222
max  : 108
identical pixels: 26.252222222222223
```

**Kesimpulan:** dua gambar identik secara visual; perbedaan kecil berasal
dari re-encoding/resize CDN JetPhotos. Fotografer asli: **Raihan Al Faris**,
nama depan **Raihan**.

### Evidence langkah ini

![term-06-jetphotos-page.png](assets/fresh-arrival/term-06-jetphotos-page.png)

*Terminal evidence — `06-jetphotos-page.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`06-jetphotos-page.txt`](assets/fresh-arrival/06-jetphotos-page.txt)
