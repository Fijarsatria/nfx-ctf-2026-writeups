# FlagKeepers — Eksploitasi / Solver

[← Overview](20-flagkeepers.md) · [Index](index.md)

### 3.1 Helper GF(2^128) / GHASH

Tersimpan di `writeups/assets/flagkeepers/gcmtool.py`. Fungsi inti:

```python
MASK = (1 << 128) - 1

def gf_mul(x, y):
    z = 0; v = x & MASK
    for i in range(128):
        if (y >> (127 - i)) & 1:
            z ^= v
        if v & 1:
            v = (v >> 1) ^ (0xE1 << 120)
        else:
            v >>= 1
    return z & MASK

def ghash(h, ct, aad=b""):
    y = 0
    for b in blocks16(aad):
        y = gf_mul(y ^ b, h)
    for b in blocks16(ct):
        y = gf_mul(y ^ b, h)
    L = ((len(aad) * 8) << 64) | (len(ct) * 8)
    return gf_mul(y ^ L, h)

def ekj0(key, nonce):
    return int.from_bytes(
        AES.new(key, AES.MODE_ECB).encrypt(nonce + b"\0\0\0\1"), "big")

def hkey(key):
    return int.from_bytes(AES.new(key, AES.MODE_ECB).encrypt(b"\0" * 16), "big")
```

`recover_H_general()` membangun persamaan dari semua pasangan sampel:

```python
for i in range(n):
    for j in range(i + 1, n):
        c1, t1 = pairs[i]; c2, t2 = pairs[j]
        b1 = blocks16(c1); b2 = blocks16(c2)
        coeff = {}
        for k in range(1, nblocks + 1):
            e = nblocks - k + 2
            d = b1[k-1] ^ b2[k-1]
            if d:
                coeff[e] = coeff.get(e, 0) ^ d
        # coeff[e] adalah koefisien H^e, rhs = t1 ^ t2
```

lalu eliminasi Gaussian di GF(2^128), dan memilih `H` yang membuat
`tag XOR ghash(H, ct)` konstan di semua sampel.

### 3.2 Exploit live

Tersimpan di `writeups/assets/flagkeepers/exploit_live.py` (ringkas):

```python
samples = []
for i in range(14):
    s.sendall(b"2\n")
    txt = recv_until()
    nonce, msg, ct, tag = parse(txt)
    samples.append((msg, ct, int.from_bytes(tag, "big")))

pairs = [(ct, t) for m, ct, t in samples]
H = recover_H_general(pairs, (len(samples[0][1]) + 15) // 16)
assert H is not None

Es = {t ^ ghash(H, ct) for m, ct, t in samples}
assert len(Es) == 1
E0 = next(iter(Es))

P0, C0, _ = samples[0]
KS = bytes(a ^ b for a, b in zip(P0, C0))

P = b"admin = True" + b" " * 39
CT = bytes(a ^ b for a, b in zip(P, KS))
TAG = ghash(H, CT) ^ E0

s.sendall(b"4\n")
s.sendall(CT.hex().encode() + b"\n")
s.sendall(TAG.to_bytes(16, "big").hex().encode() + b"\n")
print(recv_until())
```

### 3.3 Output live asli

Log `writeups/assets/flagkeepers/live_run.log`:

```text
[banner ok] 210
[sample0] msg= b'RECOVERY|ts=1794053560|r=1de81f84|t=fdaef5b11644|OK'
[sample0] ctlen 51 tag 2a0ccbabce92a0e321d862330ad3dc9a
[collected] 14 idx 32
[msg lengths] {51}
[H] 0x26493fa6231e531baf7ba6bf77c84b50
[E_K(J0) consistency] 1
[forged] plaintext= b'admin = True                                       '
[forged] ct= 953f210a7913d6a2e4211f1fe7fa4082716ce1d2bc88c1e8bd712e3becae698a013b4e3d955aef26d4f6983e844488fbb5ed70
[forged] tag= ced4419767ad26b3c4801c6aca6fb644
[final idx] 32
[opt4 ct prompt] CT: 
[opt4 tag prompt] Tag: 
[RESULT] NFX{gcm_f0rb1dd3n_4tt4ck_du4l_t4g_c0ll1s10n_m4st3r}
```

### 3.4 Reproduksi offline

Karena oracle sudah tidak selalu hidup, serangan juga direproduksi offline
dengan `app.py` semantics dan flag placeholder. Script:
`writeups/assets/flagkeepers/offline_sim.py`.

```text
$ python3 offline_sim.py
[*] collected 14 RECOVERY samples, len = 51
[*] recovered H_b       = 0x7ab223f587d44702d189c082bdb1b954
[*] E_K(J0) candidates  = 1 (must be 1)
[*] forged CT           = eb63a256c554cf85437af70ccc63ccab1c2961ee28535c5741802cf9b5b5d5ca401e2cfd8a45214f55a7943ce6e62059d9b75b
[*] forged TAG          = 031cd464820d4c2688dfa5b8fd030492
[*] server-side check:
    decrypt_and_verify  = OK
    plaintext           = b'admin = True                                       '
    admin = True in msg[:idx] -> True
    flag (offline demo) = NFX{placeholder_offline_demo}
```

`H` dan CT berbeda dari run live karena key/nonce acak, tetapi alurnya sama
dan `decrypt_and_verify` membuktikan tag forgery valid.
