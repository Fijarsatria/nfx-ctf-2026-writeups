#!/usr/bin/env python3
"""Recover the ternary LWE secret from lwe.py with a Kannan embedding.

Instance: b = A*s + e (mod q), q=257, A is 64x40, s in {-1,0,1},
e in [-2,2].  The short vector (e, s, 1) is found with LLL+BKZ.
"""
from fpylll import IntegerMatrix, LLL, BKZ
import sys

ns = {}
exec(open(sys.argv[1] if len(sys.argv) > 1 else "lwe.py").read(), ns)
A, b, q = ns["A"], ns["b"], ns["q"]
m, n = len(A), len(A[0])

# Kannan embedding: rows [q I_m | 0 | 0], [A^T | I_n | 0], [b^T | 0 | 1]
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
    sg = row[-1]
    # With the last row builder (b^T|0|1), a vector whose last coordinate is
    # +/-1 carries the secret directly in positions m..m+n-1.
    s = [row[m + j] for j in range(n)]
    if max(map(abs, s)) > 1:
        continue
    # Recompute the error from the definition e = b - A*s (mod q), centered.
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
