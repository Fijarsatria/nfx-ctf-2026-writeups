# Dokodemo Door — Eksploitasi / Solver

[← Overview](28-dokodemo-door.md) · [Index](index.md)

### 3.1 Strategi

1. Baca ciphertext.
2. Untuk setiap panjang key 1..64, turunkan byte key dari header dan trailer.
3. Tolak panjang key yang menyebabkan konflik.
4. Jika hanya tersisa ≤2 byte key yang belum diketahui, brute-force dan skor.
5. Dekripsi seluruh file, verifikasi magic PDF dan trailer.
6. Decode content stream (`ASCII85` → `Flate`) dan ambil operator `Tj`.

### 3.2 Solver

```python
#!/usr/bin/env python3
# assets/dokodemo-door/solve_dokodemo.py (ringkas)
from pathlib import Path
import itertools

SRC = Path("/home/bocil/ctf/nfx/crypto/Dokodemo_Door/rahasia.pdf")
HEAD = b"%PDF-1.4\n"
TAIL = b"%%EOF\n"

def score(data):
    markers = [b"%PDF", b"%%EOF", b" obj", b"endobj", b"stream",
               b"/Type", b"xref", b"trailer"]
    return sum(data.count(m)*20 for m in markers) + \
           sum(32 <= b < 127 or b in (9,10,13) for b in data)//20

c = SRC.read_bytes()
n = len(c)
best = None

for kl in range(1, 65):
    key = [None]*kl
    ok = True
    for i, p in enumerate(HEAD):                 # known plaintext header
        j = i % kl
        v = c[i] ^ p
        if key[j] is None: key[j] = v
        elif key[j] != v: ok = False; break
    if not ok: continue
    off = n - len(TAIL)
    for i, p in enumerate(TAIL):                 # known plaintext trailer
        j = (off+i) % kl
        v = c[off+i] ^ p
        if key[j] is None: key[j] = v
        elif key[j] != v: ok = False; break
    if not ok: continue

    unknown = [i for i,v in enumerate(key) if v is None]
    if len(unknown) > 2: continue
    for fill in itertools.product(range(256), repeat=len(unknown)):
        kk = key[:]
        for idx,val in zip(unknown, fill): kk[idx] = val
        dec = bytes(b ^ kk[i % kl] for i,b in enumerate(c))
        sc = score(dec)
        if best is None or sc > best[0]:
            best = (sc, kl, bytes(kk), dec)

sc, kl, key, dec = best
print("key length:", kl)
print("key       :", key)
print("header    :", dec[:20])
print("trailer   :", dec[-24:])
Path("/tmp/opencode/dokodemo_decrypted.pdf").write_bytes(dec)
```

### 3.3 Output asli

```text
$ python3 solve_dokodemo.py
ciphertext bytes      : 8672
candidate key length  : 16
recovered key         : b'nfx_k3tuk_p1ntu!'
crib-unknown positions: [9] filled with (95,)
decrypted header      : b'%PDF-1.4\n%\x93\x8c\x8b\x9e Repor'
decrypted trailer     : b'>>\nstartxref\n8239\n%%EOF\n'
score                 : 1213
written               : /tmp/opencode/dokodemo_decrypted.pdf
```

Ekstraksi teks:

```text
$ python3 extract_text.py
PDF bytes: 8672
[ NFX PROTOCOL // RESTRICTED ACCESS ]
DOKODEMO DOOR
Sandi Rahasia Gerbang Masuk Sektor Barat
Di balik pintu ini terdapat akses langsung menuju jaringan rahasia NFX.
Hanya mereka yang memiliki otentikasi sah yang diperkenankan masuk.
Ketuk tiga kali pada pintu dan bisikkan kode otorisasi:
Flag: NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}
Gunakan flag di atas untuk melakukan submission pada platform CTF.
NFX CLASSIFIED ARCHIVE // STRICTLY CONFIDENTIAL // DO NOT DISTRIBUTE
```
