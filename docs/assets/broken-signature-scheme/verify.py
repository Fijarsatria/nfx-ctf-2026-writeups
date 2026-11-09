#!/usr/bin/env python3
"""Three-layer verification for Broken Signature Scheme."""
import json, hashlib, math
from Crypto.Cipher import AES

d = json.load(open("output.txt"))
N, e = int(d["N"], 16), d["e"]
tgt = int(d["target_msg_hex"], 16)

# ---- Layer 1: multiplicative RSA signature forgery ----
msgs = [int(s["msg"], 16) for s in d["valid_sigs"]]
sigs = [int(s["sig"], 16) for s in d["valid_sigs"]]
prod_m = (msgs[0] * msgs[1] * msgs[2]) % N
prod_s = (sigs[0] * sigs[1] * sigs[2]) % N
print("[L1] m0*m1*m2 == target :", prod_m == tgt)
print("[L1] forged sig^e == m   :", pow(prod_s, e, N) == tgt)
print("[L1] target message      :", bytes.fromhex(d["target_msg_hex"]).decode())

# ---- Layer 2: close-prime RSA + partial key leak ----
p = 90291662713827565480510099980052169978757026472994257635201524524901623059176183784023029214624806237433417327527438388766528120528496054964793640966468959559313814603396865910254942140069944258287881295705125931644869356506093912310980430646149995999468750875007630831106806462679175171959178546366955626109
q = 90291662713827565480510099980052169978757026472994257635201524524901623059176183784023029214624806237433417327527438388766528120528496054964793640966468959559313814603396865910254942140069944258287881295705125931644871393542070246797066699091838405377629802343401296767357442603128529553258941883073139025589
print("[L2] p*q == N            :", p * q == N)
print("[L2] q-p                 :", q - p)
print("[L2] leak matches        :", ((p >> d["leak_pos"]) & ((1 << d["leak_bits"]) - 1)) == int(d["leak"], 16))

# ---- Layer 3: AES-GCM ----
fc = d["flag_cipher"]
key = hashlib.sha256(
    p.to_bytes((p.bit_length() + 7) // 8, "big")
    + q.to_bytes((q.bit_length() + 7) // 8, "big")).digest()
pt = AES.new(key, AES.MODE_GCM, nonce=bytes.fromhex(fc["nonce_hex"])).decrypt_and_verify(
    bytes.fromhex(fc["ct_hex"]), bytes.fromhex(fc["tag_hex"]))
print("[L3] AES-GCM tag         : OK")
print("[L3] FLAG                :", pt.decode())
