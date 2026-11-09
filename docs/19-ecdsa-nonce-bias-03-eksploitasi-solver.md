# ECDSA Nonce Bias — Eksploitasi / Solver

[← Overview](19-ecdsa-nonce-bias.md) · [Index](index.md)

### 3.1 Script lengkap

Tersimpan di `writeups/assets/ecdsa-nonce-bias/solve.py`:

```python
import json, hashlib
from fpylll import IntegerMatrix, LLL, BKZ
from Crypto.Cipher import AES

d = json.load(open("output.txt"))
n = int(d["n"], 16)
sigs = d["signatures"]
B = 1 << 248

def check_d(dd):
    if dd <= 0 or dd >= n:
        return False
    for sig in sigs:
        r = int(sig["r"], 16)
        s = int(sig["s"], 16)
        h = int(sig["h"], 16)
        k = (h + dd * r) * pow(s, -1, n) % n
        if k >= B:
            return False
    return True

def attempt(m, bkz=False):
    aa = []
    bb = []
    for sig in sigs[:m]:
        r = int(sig["r"], 16)
        s = int(sig["s"], 16)
        h = int(sig["h"], 16)
        si = pow(s, -1, n)
        aa.append((h * si) % n)
        bb.append((r * si) % n)
    dim = m + 2
    M = IntegerMatrix(dim, dim)
    n2 = n * n
    for i in range(m):
        M[i, i] = n2
    for i in range(m):
        M[m, i] = bb[i] * n
        M[m + 1, i] = aa[i] * n
    M[m, m] = B
    M[m + 1, m + 1] = n * B
    if bkz:
        BKZ.reduction(M, BKZ.Param(block_size=20))
    else:
        LLL.reduction(M, delta=0.99)
    cands = set()
    for i in range(dim):
        row = [M[i, j] for j in range(dim)]
        if row[m] != 0 and row[m] % B == 0:
            cands.add((row[m] // B) % n)
            cands.add((-(row[m] // B)) % n)
    for dd in cands:
        if check_d(dd):
            return dd
    return None

for m in [50, 60, 80, 100, 120]:
    print("trying m", m, flush=True)
    dd = attempt(m)
    print(" m", m, "->", hex(dd) if dd else None, flush=True)
    if dd:
        print("FOUND d", hex(dd))
        fc = d["flag_ciphertext"]
        key = hashlib.sha256(dd.to_bytes(32, "big")).digest()
        pt = AES.new(key, AES.MODE_GCM,
                     nonce=bytes.fromhex(fc["nonce_hex"])).decrypt_and_verify(
            bytes.fromhex(fc["ct_hex"]), bytes.fromhex(fc["tag_hex"]))
        print("FLAG =", pt.decode())
        break
```

### 3.2 Output asli

```text
$ python3 writeups/assets/ecdsa-nonce-bias/solve.py
trying m 50
 m 50 -> 0xe59b58bbc7a872a170ef684d62f92bbbe511f3bd5d9ec50814435c3666e1fffa
FOUND d 0xe59b58bbc7a872a170ef684d62f92bbbe511f3bd5d9ec50814435c3666e1fffa
FLAG = NXCTF{ecds4_hnp_n0nc3_b14s_8b1t_l4tt1c3_a3d2ae498097}
```

### 3.3 Verifikasi

Script `writeups/assets/ecdsa-nonce-bias/verify.py`:

```text
$ python3 verify.py
d*G.x == pubkey.x : True
d*G.y == pubkey.y : True
nonces < 2^248    : 200 / 200
AES-GCM tag       : OK
FLAG              = NXCTF{ecds4_hnp_n0nc3_b14s_8b1t_l4tt1c3_a3d2ae498097}
```

Private key lengkap:

```text
d = 0xe59b58bbc7a872a170ef684d62f92bbbe511f3bd5d9ec50814435c3666e1fffa
```
