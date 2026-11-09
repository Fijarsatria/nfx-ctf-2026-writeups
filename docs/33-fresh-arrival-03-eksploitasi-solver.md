# Fresh Arrival — Eksploitasi / Solver

[← Overview](33-fresh-arrival.md) · [Index](index.md)

### 3.1 Strategi

1. Baca registrasi dari gambar (`PK-ADL`).
2. Reverse image search → JetPhotos photo ID 11925184.
3. Unduh thumbnail, bandingkan dengan gambar challenge (MAE).
4. Baca metadata JetPhotos: fotografer, tanggal, lokasi, MSN.
5. Telusuri riwayat MSN 26854 → operator pertama China Xinhua Airlines.
6. Ambil IATA/ICAO/HQ dari Wikidata/Wikipedia.
7. Susun flag.

### 3.2 Script pembanding gambar

```python
#!/usr/bin/env python3
from PIL import Image
import numpy as np, hashlib

a = Image.open("osint/spotted.jpg").convert("RGB")
b = Image.open("jetphotos_11925184.jpg").convert("RGB")
x = np.asarray(a, dtype=np.int16)
y = np.asarray(b, dtype=np.int16)
d = np.abs(x - y)

print("challenge :", a.size, hashlib.sha256(open("osint/spotted.jpg","rb").read()).hexdigest())
print("jetphotos :", b.size, hashlib.sha256(open("jetphotos_11925184.jpg","rb").read()).hexdigest())
print("MAE       :", float(d.mean()))
print("max diff  :", int(d.max()))
print("identical :", float((d.sum(axis=2) == 0).mean() * 100), "%")
```

### 3.3 Output asli

```text
challenge : (400, 225) 1b74fef0e79aae45c0a5adc275124f2b996b67547f1a39180451ce9750cf4600
jetphotos : (400, 225) 1ac65f4af318778ec95f9c6feaffd776563cb54ac2b71fb96e84198104b3b202
MAE       : 2.209522222222222
max diff  : 108
identical : 26.252222222222223 %
```
