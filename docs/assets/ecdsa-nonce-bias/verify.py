#!/usr/bin/env python3
"""Verify the recovered ECDSA private key, all nonce bounds and the AES-GCM tag."""
import json, hashlib
from Crypto.PublicKey import ECC
from Crypto.Cipher import AES

d = json.load(open("output.txt"))
n = int(d["n"], 16)
D = 0xe59b58bbc7a872a170ef684d62f92bbbe511f3bd5d9ec50814435c3666e1fffa
B = 1 << 248

# 1) d*G must equal the published public key
pub = ECC.import_key(open("pubkey.pem").read())
P = ECC.construct(curve="secp256k1", d=D).public_key().pointQ
print("d*G.x == pubkey.x :", int(P.x) == int(pub.pointQ.x))
print("d*G.y == pubkey.y :", int(P.y) == int(pub.pointQ.y))

# 2) every nonce k = (h + d*r)/s mod n is < 2^248
ok = 0
for sig in d["signatures"]:
    r, s, h = int(sig["r"], 16), int(sig["s"], 16), int(sig["h"], 16)
    k = (h + D * r) * pow(s, -1, n) % n
    ok += (k < B)
print("nonces < 2^248    :", ok, "/", len(d["signatures"]))

# 3) AES-GCM decryption authenticates
fc = d["flag_ciphertext"]
key = hashlib.sha256(D.to_bytes(32, "big")).digest()
pt = AES.new(key, AES.MODE_GCM, nonce=bytes.fromhex(fc["nonce_hex"])).decrypt_and_verify(
    bytes.fromhex(fc["ct_hex"]), bytes.fromhex(fc["tag_hex"]))
print("AES-GCM tag       : OK")
print("FLAG              =", pt.decode())
