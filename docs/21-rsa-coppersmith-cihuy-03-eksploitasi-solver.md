# RSA Coppersmith cihuy — Eksploitasi / Solver

[← Overview](21-rsa-coppersmith-cihuy.md) · [Index](index.md)

### 3.1 Script lengkap

Tersimpan di `writeups/assets/rsa-coppersmith-cihuy/solve.py`:

```python
#!/usr/bin/env python3
from sympy import Poly, symbols
from fpylll import IntegerMatrix, LLL

n = 0xE4ABA2D625FEC44D3984056BED4ED632B178E6F5B3893593E736111E9E91A7130F957FD76C48D42724C3423F6D6D8132EF909A8E414E24F6ACE3BA2C0A8059C29BCE292055A9BF9B7008E0788162B568691E85F52C24A9D904DDFFC6EF5DCB177D12243CFE449AB3638E52491247455C1DF12030975D469A933685CF0527421B
e = 65537
c = 0xC5DD7E48FF77FBC1D1AD1130550CDE5FDEC27CDF2D8A890370DEFA7605538EA82945462297449AB9D0F8C01D0FF403283F0B4DA677389289F0D923FE6E24DD6B3AFA02F22534754C0261C87EC7C0E488DC2A764DD327A1EA211AD1025EB231B7E856F4F66333A9FFC3A16189C47E4DE39D55C9ED474AEEAF4F22B997EC706174
p_msb = 0xF13228781AB150BC402DF686354483D5FA1B226BB33DD3AD9E4D3011AC92AD2F2589B571CA3
ubits = 212
X = 1 << (ubits + 1)
a = p_msb << ubits

def polymul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return r

def polypow(p, k):
    r = [1]
    for _ in range(k):
        r = polymul(r, p)
    return r

f = [a, 1]
x = symbols("x")

def try_poly(coeffs, dim):
    poly = sum(coeffs[k] * x**k for k in range(dim))
    P = Poly(poly, x)
    roots = []
    try:
        for r0, mult in P.ground_roots().items():
            roots.append(int(r0))
    except Exception:
        pass
    try:
        for r0 in P.nroots(n=40):
            if abs(r0.as_real_imag()[1]) < 1e-15:
                rr = r0.as_real_imag()[0]
                if abs(rr - round(rr)) < 1e-15:
                    roots.append(int(round(rr)))
    except Exception:
        pass
    for cand in roots:
        for cc in (cand, cand % n):
            if not (0 <= cc < X):
                continue
            p = a + cc
            if 1 < p < n and n % p == 0:
                return p
    return None

for m in range(2, 9):
    t = m
    polys = []
    for i in range(m):
        g = [coef * pow(n, m - i) for coef in polypow(f, i)]
        polys.append(g)
    fm = polypow(f, m)
    for j in range(t):
        polys.append([0] * j + fm)
    dim = len(polys)
    M = IntegerMatrix(dim, dim)
    for r in range(dim):
        g = polys[r]
        for k, coef in enumerate(g):
            M[r, k] = coef * pow(X, k)
    LLL.reduction(M)
    print("m", m, "dim", dim)
    for r in range(dim):
        row = [M[r, k] for k in range(dim)]
        if any(row[k] % pow(X, k) for k in range(dim)):
            continue
        coeffs = [row[k] // pow(X, k) for k in range(dim)]
        p = try_poly(coeffs, dim)
        if p:
            print("FOUND p =", hex(p))
            q = n // p
            d = pow(e, -1, (p - 1) * (q - 1))
            pt = pow(c, d, n).to_bytes((n.bit_length() + 7) // 8, "big")
            print("PT bytes:", pt)
            raise SystemExit
print("not found")
```

### 3.2 Output asli

```text
$ python3 writeups/assets/rsa-coppersmith-cihuy/solve.py
m 2 dim 4
m 3 dim 6
m 4 dim 8
FOUND p = 0xf13228781ab150bc402df686354483d5fa1b226bb33dd3ad9e4d3011ac92ad2f2589b571ca30816efe24517161a24e6c35d3ca04b8c149ae440350586e70e051
PT bytes: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00NFXCTF{C0pp3rsm1th_p4rt14l_k3y_3xp0sur3_9617eda9}'
```

### 3.3 Verifikasi

Script `writeups/assets/rsa-coppersmith-cihuy/verify.py` mengecek ulang:

```text
$ python3 verify.py
p == p_msb*2^212 + x : True
unknown x bits       : 208
N % p == 0           : True
p bits / q bits      : 512 512
plaintext (stripped) : NFXCTF{C0pp3rsm1th_p4rt14l_k3y_3xp0sur3_9617eda9}
```

`unknown x bits = 208` berarti dari 212 bit yang tidak diketahui, 208 bit
benar-benar terpakai; empat bit teratas `x` nol. Ini tetap di bawah batas
`N^{0.25}`.
