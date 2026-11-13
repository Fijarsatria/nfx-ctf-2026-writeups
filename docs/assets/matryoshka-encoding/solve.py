#!/usr/bin/env python3
"""Matryoshka Encoding solver — run from this directory: python3 solve.py"""
import base64
import zlib
from pathlib import Path

raw = (Path(__file__).resolve().parent / "capsule.dat").read_text().strip()

# 1. swap setiap pasangan karakter Base64, jangan sentuh padding
body = raw.rstrip("=")
pad = raw[len(body):]
swapped = "".join(body[i + 1] + body[i] for i in range(0, len(body) - 1, 2))
if len(body) % 2:
    swapped += body[-1]
swapped += pad

# 2. base64 decode
data = base64.b64decode(swapped)
assert data[:2] == b"\x78\xda", data[:4].hex()

# 3. zlib decompress -> base85
b85 = zlib.decompress(data).decode()
print("base85:", b85)

# 4. RFC1924 base85 decode
raw40 = base64.b85decode(b85)

# 5. XOR dengan key NFX!
flag = bytes(c ^ b"NFX!"[i % 4] for i, c in enumerate(raw40))
print(flag.decode())
