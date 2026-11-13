import json, hashlib, math
from pathlib import Path
from Crypto.Cipher import AES

d = json.load(open(Path(__file__).resolve().parent / "output.txt"))
N = int(d["N"], 16)
leak = int(d["leak"], 16)
pos, lb, db = d["leak_pos"], d["leak_bits"], d["delta_bits"]

# q = nextprime(p + 2^db)  =>  delta = q-p = 2^db + small gap
# N = p(p+delta), discriminant (p+q)^2 = delta^2 + 4N must be a perfect square
base = 1 << db
p = q = None
for g in range(200000):
    delta = base + g
    D = delta * delta + 4 * N
    s = math.isqrt(D)
    if s * s != D or (s - delta) % 2:
        continue
    cand = (s - delta) // 2
    if cand * (cand + delta) == N and ((cand >> pos) & ((1 << lb) - 1)) == leak:
        p, q = cand, cand + delta
        break
assert p and q and p * q == N
print("p =", p)
print("q =", q)

bl = (p.bit_length() + 7) // 8
qc = d["flag_cipher"]
ct = bytes.fromhex(qc["ct_hex"])
nonce = bytes.fromhex(qc["nonce_hex"])
tag = bytes.fromhex(qc["tag_hex"])
for enc in (p.to_bytes(bl, "big") + q.to_bytes((q.bit_length() + 7) // 8, "big"),
            p.to_bytes((p.bit_length() + 7) // 8, "big") + q.to_bytes((q.bit_length() + 7) // 8, "big")):
    key = hashlib.sha256(enc).digest()
    try:
        pt = AES.new(key, AES.MODE_GCM, nonce=nonce).decrypt_and_verify(ct, tag)
        print("FLAG =", pt.decode())
        break
    except ValueError:
        pass
