# Feistel Differential — Script lengkap

[← Overview](04-feistel-differential.md) · [Index](index.md)

> **Langkah 5/9 — Script lengkap.** Tersimpan di docs/assets/feistel-differential/solve.py:
>
> **Titik penting:** Tersimpan di docs/assets/feistel-differential/solve.py:
>
> **Berikutnya:** [Solver](04-feistel-differential-06-solver.md)

## 3.2 Script lengkap

Tersimpan di `docs/assets/feistel-differential/solve.py`:

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

### Evidence langkah ini

![term-solver-output.png](assets/feistel-differential/term-solver-output.png)

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`solver-output.txt`](assets/feistel-differential/solver-output.txt)
