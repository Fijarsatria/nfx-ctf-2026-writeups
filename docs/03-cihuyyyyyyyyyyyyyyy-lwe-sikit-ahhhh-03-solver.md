# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh — Solver

[← Overview](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh.md) · [Index](index.md)

## 3.1 Strategi

1. Load `A`, `b`, `q` dari `lwe.py`.
2. Bangun basis Kannan 105 dimensi.
3. LLL (`delta=0.99`) lalu BKZ (`block_size=20`, `max_loops=2`).
4. Cari baris dengan koordinat terakhir `±1`; ambil 40 koordinat secret.
5. Hitung ulang `e` dan validasi seluruh 64 persamaan.

## 3.2 Script lengkap

Tersimpan di
`writeups/assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solve_lwe.py`:

```python
#!/usr/bin/env python3
"""Recover the ternary LWE secret from lwe.py with a Kannan embedding."""
from fpylll import IntegerMatrix, LLL, BKZ
import sys

ns = {}
exec(open(sys.argv[1] if len(sys.argv) > 1 else "lwe.py").read(), ns)
A, b, q = ns["A"], ns["b"], ns["q"]
m, n = len(A), len(A[0])

d = m + n + 1
B = IntegerMatrix(d, d)
for i in range(m):
    B[i, i] = q
for j in range(n):
    for i in range(m):
        B[m + j, i] = A[i][j]
    B[m + j, m + j] = 1
for i in range(m):
    B[d - 1, i] = b[i]
B[d - 1, d - 1] = 1

LLL.reduction(B, delta=0.99)
BKZ.reduction(B, BKZ.Param(block_size=20, max_loops=2))

for r in range(d):
    row = [int(B[r, j]) for j in range(d)]
    if abs(row[-1]) != 1:
        continue
    s = [row[m + j] for j in range(n)]
    if max(map(abs, s)) > 1:
        continue
    e = [(b[i] - sum(A[i][j] * s[j] for j in range(n))) % q for i in range(m)]
    e = [x if x <= q // 2 else x - q for x in e]
    if max(map(abs, e)) <= 3:
        assert all((sum(A[i][j] * s[j] for j in range(n)) + e[i]) % q == b[i] % q
                   for i in range(m))
        print("s =", s)
        print("e =", e)
        print("max|s| =", max(map(abs, s)), " max|e| =", max(map(abs, e)))
        print("check b == A*s + e (mod %d): OK (64/64 rows)" % q)
        print("ct =", ns["ct"])
        break
else:
    print("no short vector found")
```

### Evidence langkah ini

![term-solver-output.png](assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/term-solver-output.png)

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`solver-output.txt`](assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solver-output.txt)
