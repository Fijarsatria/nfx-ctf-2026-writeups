# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh — Eksploitasi / Solver

[← Overview](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh.md) · [Index](index.md)

### 3.1 Strategi

1. Load `A`, `b`, `q` dari `lwe.py`.
2. Bangun basis Kannan 105 dimensi.
3. LLL (`delta=0.99`) lalu BKZ (`block_size=20`, `max_loops=2`).
4. Cari baris dengan koordinat terakhir `±1`; ambil 40 koordinat secret.
5. Hitung ulang `e` dan validasi seluruh 64 persamaan.

### 3.2 Script lengkap

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

### 3.3 Output asli

```text
$ python3 writeups/assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solve_lwe.py lwe.py
s = [1, 0, -1, 1, 0, 0, 0, -1, 1, 1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, -1, 1, -1, 0, 0, 1, -1, -1, -1, 0, 1, 0, -1, 0, 0, -1, -1, 1, 1, -1]
e = [-2, -1, 0, -2, -1, 1, 0, 1, -1, -1, 2, 1, 2, 1, 2, 1, 1, 1, -2, 1, 2, -2, 2, 2, 0, 1, 1, 0, -1, 1, 1, 0, -1, 0, 2, -2, 0, 0, 0, 1, 1, 1, 2, 1, 0, 1, 2, 0, -1, -2, 1, -1, 2, 1, 0, 0, 0, -1, 0, 2, 1, -1, 2, 1]
max|s| = 1  max|e| = 2
check b == A*s + e (mod 257): OK (64/64 rows)
ct = 8c8d8b0001438bf68076c012df3bb170d82e882152d9c13ab813435e7e5ada38a9abfed5eec11cbfb4
```

### 3.4 Dekripsi `ct`

`ct` adalah 41 byte:

```text
8c8d8b0001438bf68076c012df3bb170d82e882152d9c13ab813435e7e5ada38a9abfed5eec11cbfb4
```

Panjang ini **tepat sama** dengan panjang flag yang terverifikasi (41 byte),
jadi `ct` hampir pasti merupakan stream cipher / XOR keystream, bukan
ciphertext blok.

Sayangnya `lwe.py` yang dipublikasikan **hanya berisi data** — tidak ada kode
KDF, nonce, atau fungsi enkripsi. Karena itu langkah dekripsi tidak dapat
direproduksi byte-exact hanya dari lampiran. Yang dapat ditunjukkan adalah
konsistensi:

```text
flag     = NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195}   (41 byte)
ct       = 8c8d8b0001438bf68076c012df3bb170d82e882152d9c13ab813435e7e5ada38a9abfed5eec11cbfb4
keystream = ct XOR flag
          = c2cbd3435505f09ab402b423bc08ee03b51ae44d0daaf259ca203701320d9f679ececcb4def0258ac9
```

Angka di atas bukan tebakan: flag diverifikasi langsung oleh platform
(`work/submit_curl_log.jsonl`). Yang tidak tersedia adalah cara server
menurunkan keystream dari `s`/`e`; ini ditandai sebagai keterbatasan artefak,
bukan sebagai langkah solver yang diklaim berhasil.
