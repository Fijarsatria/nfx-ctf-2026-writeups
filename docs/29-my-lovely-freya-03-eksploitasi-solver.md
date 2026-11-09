# My Lovely Freya — Eksploitasi / Solver

[← Overview](29-my-lovely-freya.md) · [Index](index.md)

### 3.1 Strategi

1. Ekstrak ZIP.
2. Baca `IHDR` dan `IDAT`; hitung jumlah baris nyata.
3. Unfilter 336 baris ekstra dan render sebagai gambar.
4. Baca password dari gambar.
5. Dekripsi `surat_untuk_freya.enc` dengan AES-256-CBC + PBKDF2
   100.000 iterasi.
6. Normalisasi prefix `NXCTF` → `NFX` sesuai flag platform.

### 3.2 Ekstraksi baris tersembunyi

```bash
unzip FreyaSayangkuh -d freya/
# -> freya/freya_sayangkuh.png
# -> freya/surat_untuk_freya.enc
```

```python
#!/usr/bin/env python3
# assets/my-lovely-freya/extract_hidden.py (ringkas)
import struct, zlib
from PIL import Image

data = open("freya_sayangkuh.png", "rb").read()
i, idat, width, height = 8, b"", None, None
while i < len(data):
    length = struct.unpack(">I", data[i:i+4])[0]
    ctype = data[i+4:i+8]
    chunk = data[i+8:i+8+length]
    if ctype == b"IHDR":
        width, height, depth, color = struct.unpack(">IIBB", chunk[:10])
    elif ctype == b"IDAT":
        idat += chunk
    i += 12 + length

raw = zlib.decompress(idat)
stride = width * 3 + 1
actual_h = len(raw) // stride
print("declared", height, "actual", actual_h, "hidden", actual_h - height)

full = unfilter(raw, width, actual_h)          # filter 0..4 per baris
extra = full[height * width * 3:]             # 336 baris terakhir
Image.frombytes("RGB", (width, actual_h - height), extra).save("hidden.png")
```

`unfilter()` mengimplementasikan lima tipe filter PNG (None, Sub, Up,
Average, Paeth), sama seperti decoder PNG standar.

### 3.3 Dekripsi surat

```bash
openssl enc -d -aes-256-cbc -md sha256 -pbkdf2 -iter 100000 \
  -in surat_untuk_freya.enc \
  -pass 'pass:<!HayamGoreng45@/>' \
  -out surat-decrypted.txt
```

### 3.4 Output asli

```text
$ python3 extract_hidden.py
IHDR: 1024x1200, bit_depth=8, color_type=2
decompressed IDAT bytes: 4720128
rows actually present  : 1536
declared rows          : 1200
hidden rows            : 336
hidden rows written to : .../01-hidden-rows.png
```

```text
$ ./decrypt_surat.sh
00000000: 5361 6c74 6564 5f5f d4be 860a 4bb7 cf3a  Salted__....K..:
00000010: 92c5 4dc0 d0ee 5cf0 aeef 80a8 3e7a e8ce  ..M...\.....>z..
00000020: 5a7d 8114 d186 319a 95f4 41f3 5c21 cb0f  Z}....1...A.\!..
--- openssl decrypt ---
exit=0
--- plaintext ---
NXCTF{FR3Y4_MY_L0V3LY!}
--- plaintext hex ---
00000000: 4e58 4354 467b 4652 3359 345f 4d59 5f4c  NXCTF{FR3Y4_MY_L
00000010: 3056 334c 5921 7d0a                      0V3LY!}.
```
