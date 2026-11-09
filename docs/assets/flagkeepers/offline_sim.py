#!/usr/bin/env python3
"""Offline reproduction of the FlagKeepers forbidden attack.

This mirrors app.py exactly but with local random keys/flag, so the whole
attack can be re-run without the remote oracle.  The real run against
s1.nfx.my.id:43210 is preserved in live_run.log.
"""
import os, time
from Crypto.Cipher import AES
from gcmtool import ghash, recover_H_general, hkey, ekj0, blocks16

FLAG = b"NFX{placeholder_offline_demo}"
key_a, key_b, nonce = os.urandom(16), os.urandom(16), os.urandom(12)

def encrypt(key, pt):
    c = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return c.encrypt_and_digest(pt)

# The service prints the Recovery plaintext verbatim (51 bytes each time).
samples = []
for _ in range(14):
    msg = f"RECOVERY|ts={int(time.time())}|r={os.urandom(4).hex()}|t={os.urandom(6).hex()}|OK".encode()
    assert len(msg) == 51
    ct, tag = encrypt(key_b, msg)
    samples.append((msg, ct, int.from_bytes(tag, "big")))

print("[*] collected", len(samples), "RECOVERY samples, len =", len(samples[0][1]))
H = recover_H_general([(ct, t) for _, ct, t in samples], (len(samples[0][1]) + 15) // 16)
print("[*] recovered H_b       =", hex(H))
Es = {t ^ ghash(H, ct) for _, ct, t in samples}
print("[*] E_K(J0) candidates  =", len(Es), "(must be 1)")
E0 = next(iter(Es))

P0, C0, _ = samples[0]
KS = bytes(a ^ b for a, b in zip(P0, C0))
P = b"admin = True" + b" " * 39
CT = bytes(a ^ b for a, b in zip(P, KS))
TAG = ghash(H, CT) ^ E0
print("[*] forged CT           =", CT.hex())
print("[*] forged TAG          =", TAG.to_bytes(16, "big").hex())
print("[*] server-side check:")
try:
    pt = AES.new(key_b, AES.MODE_GCM, nonce=nonce).decrypt_and_verify(
        CT, TAG.to_bytes(16, "big"))
    print("    decrypt_and_verify  = OK")
    print("    plaintext           =", pt)
    print("    admin = True in msg[:idx] ->", b"admin = True" in pt[:32])
    print("    flag (offline demo) =", FLAG.decode())
except Exception as e:
    print("    FAILED:", e)
