# Feistel Differential — Eksploitasi / Solver

[← Overview](04-feistel-differential.md) · [Index](index.md)

### 3.1 Strategi

1. Parse `pairs.txt` menjadi 14 blok `(Δ, [(p,c1,c2), ...])`.
2. Bangun model z3: 7 BitVec 16-bit, SBOX sebagai chain `If`, `permute`
   sebagai konkatenasi extract.
3. Tambahkan constraint untuk 7 pasangan pertama blok Δ=0xa.
4. Ambil model, hitung master key, verifikasi pada seluruh 280.000 baris.
5. Dekripsi `flag.enc` per blok 4-byte big-endian, lalu buang padding PKCS#7.

### 3.2 Script lengkap

Tersimpan di `writeups/assets/feistel-differential/solve.py`:

```python
#!/usr/bin/env python3
import sys
sys.path.insert(0, ".")
from z3 import *
from cipher import encrypt_block, key_schedule, decrypt_block

SBOX = [1, 8, 14, 12, 2, 0, 3, 4, 11, 9, 15, 13, 6, 10, 7, 5]

def sl(n):
    e = BitVecVal(SBOX[15], 4)
    for i in range(14, -1, -1):
        e = If(n == BitVecVal(i, 4), BitVecVal(SBOX[i], 4), e)
    return e

def F(x, k):
    y = x ^ k
    m = Concat(sl(Extract(15, 12, y)), sl(Extract(11, 8, y)),
               sl(Extract(7, 4, y)), sl(Extract(3, 0, y)))
    return Concat(Extract(11, 8, m), Extract(15, 12, m),
                  Extract(3, 0, m), Extract(7, 4, m))

def enc(block, ks):
    L = Extract(31, 16, block); R = Extract(15, 0, block)
    for k in ks:
        L, R = R, L ^ F(R, k)
    return Concat(L, R)

blocks = []; cur = None
for line in open("pairs.txt"):
    line = line.strip()
    if not line:
        continue
    if line.startswith("#"):
        diff = int(line.split(":")[-1].strip(), 16)
        cur = []; blocks.append((diff, cur)); continue
    a, b, c = line.split()
    cur.append((int(a, 16), int(b, 16), int(c, 16)))

d0, b0 = blocks[0]
ks = [BitVec(f"k{i}", 16) for i in range(7)]
for N in [6, 7, 8, 10, 12]:
    s = Solver(); s.set(timeout=120000)
    for p, c1, c2 in b0[:N]:
        s.add(enc(BitVecVal(p, 32), ks) == BitVecVal(c1, 32))
        s.add(enc(BitVecVal(p, 32) ^ BitVecVal(d0, 32), ks) == BitVecVal(c2, 32))
    if s.check() != sat:
        continue
    m = s.model()
    sv = [m.eval(k).as_long() for k in ks]
    kk = key_schedule(sum(sv[i] << (16 * i) for i in range(7)))
    cnt = sum(1 for p, c1, c2 in b0
              if encrypt_block(p, kk) == c1 and encrypt_block(p ^ d0, kk) == c2)
    print("pairs", N, "master", hex(sum(sv[i] << (16 * i) for i in range(7))),
          "block0 matches", cnt, "/", len(b0))
    if cnt == len(b0):
        break

tot = ok = 0
for diff, lst in blocks:
    for p, c1, c2 in lst:
        tot += 1
        ok += (encrypt_block(p, kk) == c1 and encrypt_block(p ^ diff, kk) == c2)
print("VERIFY", ok, "/", tot)
ct = bytes.fromhex(open("flag.enc").read().strip())
pt = b"".join(decrypt_block(int.from_bytes(ct[i:i+4], "big"), kk).to_bytes(4, "big")
              for i in range(0, len(ct), 4))
print("FLAGPT", repr(pt))
```

### 3.3 Output asli

```text
$ python3 writeups/assets/feistel-differential/solve.py
blocks [('0xa', 20000), ('0x5', 20000), ('0xa0', 20000), ('0x50', 20000), ('0xa00', 20000), ('0x500', 20000), ('0xa000', 20000), ('0x5000', 20000), ('0x5000000', 20000), ('0xa000000', 20000), ('0x50000000', 20000), ('0xa0000000', 20000), ('0x770000', 20000), ('0x550000', 20000)]
pairs 6 master 0xfdec721297377228d7783abfa383 block0 matches 11183 / 20000
pairs 7 master 0xfdec721297377222d7283ab5a383 block0 matches 20000 / 20000
VERIFY 280000 / 280000
FLAGPT b'NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}\x03\x03\x03'
```

Catatan: output `pairs 6` adalah model underdetermined yang **salah**; sengaja
ditampilkan untuk menunjukkan mengapa 7 pasangan dipakai. Model 7 pasangan
memenuhi seluruh 280.000 baris.

### 3.4 Padding

`flag.enc` berisi 52 byte. Plaintext hasil dekripsi 52 byte:

```text
NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}   (49 byte)
03 03 03                                           (PKCS#7, 3 byte)
```

Padding 3 byte mengikuti aturan PKCS#7 untuk blok 4-byte (vendor memakai
"blok" 32-bit), sehingga `03 03 03` dibuang.
