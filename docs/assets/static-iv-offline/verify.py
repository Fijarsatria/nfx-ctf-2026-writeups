#!/usr/bin/env python3
import hashlib, json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

MASTER = b"\x13\x37" * 16
d = json.load(open("output.txt"))
ct = bytes.fromhex(d["ct_hex"])
iv = bytes.fromhex(d["iv_hex"])
counter = d["counter"]

key = hashlib.sha256(MASTER + counter.to_bytes(4, "little")).digest()[:32]
print("key =", key.hex())
pt = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), 16)
print("plaintext =", pt)
print("prefix ok =", pt.startswith(b"user-input-goes-here:|"))
print("FLAG =", pt.split(b"|", 1)[1].decode())
