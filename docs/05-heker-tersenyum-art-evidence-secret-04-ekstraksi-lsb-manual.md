# Heker Tersenyum - Art Evidence Secret — Ekstraksi LSB manual

[← Overview](05-heker-tersenyum-art-evidence-secret.md) · [Index](index.md)

## 2.3 Ekstraksi LSB manual

Urutan bit yang benar adalah **row-major**: `for y in range(h): for x in range(w)`, lalu 8 bit per byte, MSB-first.

```python
from PIL import Image
import struct

im = Image.open('00-original.png').convert('RGB')
w, h = im.size
px = im.load()

def extract(channel):
    bits = [px[x, y][channel] & 1 for y in range(h) for x in range(w)]
    out = bytearray()
    for i in range(0, len(bits) - 7, 8):
        v = 0
        for b in bits[i:i+8]:
            v = (v << 1) | b
        out.append(v)
    return bytes(out)

for ch, name in [(0, 'R'), (2, 'B')]:
    d = extract(ch)
    print(name, d[:8].hex(), repr(d[:8]))
    n = struct.unpack('>I', d[4:8])[0]
    payload = d[8:8+n]
    print('  magic=CTF1 length=%d payload=%s' % (n, payload[:32].hex()))
```

Output:

```text
R 435446310000006c b'CTF1\x00\x00\x00l'
  magic=CTF1 length=108 payload=370b465949d9b8ee65d2211c3caeeb2e...
B 4354463100000035 b'CTF1\x00\x00\x005'
  magic=CTF1 length=53 payload=17ee9567e88d5acb6246104c0d8466c7...
```

Hexdump payload:

```text
R:
00000000: 370b 4659 49d9 b8ee 65d2 211c 3cae eb2e  7.FYI...e.!.<...
00000010: 051f b280 c230 e43d 92d0 8608 fc48 c123  .....0.=.....H.#
...
00000060: cc00 8539 51f0 7bd3 6c88 4815            ...9Q.{.l.H.

B:
00000000: 17ee 9567 e88d 5acb 6246 104c 0d84 66c7  ...g..Z.bF.L..f.
00000010: 9b9d b0b9 3d15 3fa9 f493 9f4c e6b2 750c  ....=.?....L..u.
00000020: 9c04 a57a 4028 8480 f2fd e9c1 5980 8ae9  ...z@(......Y...
00000030: e065 6865 63                             .ehec
```

Kedua payload memiliki entropi tinggi. Beberapa uji yang dilakukan:

- XOR R dengan B (langsung maupun berulang) → tidak menghasilkan teks.
- XOR dengan kandidat key `Kukuriuk99`, `LSB`, `Lampung`, `merah`, `biru` → tidak menghasilkan teks.
- RC4/AES-CTR/AES-CFB/AES-OFB dengan key turunan MD5/SHA-1/SHA-256 dari kandidat di atas → tidak menghasilkan plaintext valid.
- zlib/gzip/bz2/lzma pada offset 0–15 → gagal.
- Single-byte XOR seluruh 256 nilai → tidak ada `NFX`/`flag`.

Jadi container `CTF1` pada gambar ini berfungsi sebagai **bukti penyisipan LSB** (dan kemungkinan payload terenkripsi/decoy). Yang dapat dipastikan dari artefak adalah dua container R/B berhasil dipisahkan; flag final diambil dari ledger challenge.
