#!/usr/bin/env python3
"""Decode Balik — extract the hidden JPEG from waifu.png.

The PNG is a noise image. Its red channel (R=G=B) contains a long Base64
string. Decoding it gives a zlib stream; inflating it gives another Base64
string, which decodes to the final JPEG. The flag is written on that JPEG.

Run from this directory:
    python3 solve_decode_balik.py
"""
import base64
import re
import zlib
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
SRC = HERE / "waifu.png"
OUT = HERE / "10-waifu-decoded.jpg"

im = Image.open(SRC).convert("RGBA")
flat = bytes(px[0] for px in im.getdata())  # red channel

m = re.match(rb"[A-Za-z0-9+/=]+", flat)
if not m:
    raise SystemExit("no base64 prefix found")
b64 = m.group(0)
b64 = b64[: len(b64) // 4 * 4]

zlib_data = base64.b64decode(b64)
inner_b64 = zlib.decompress(zlib_data)
jpeg = base64.b64decode(inner_b64)
OUT.write_bytes(jpeg)

print("base64 chars :", len(b64))
print("zlib bytes   :", len(zlib_data))
print("inner base64 :", len(inner_b64))
print("jpeg bytes   :", len(jpeg))
print("jpeg header  :", jpeg[:4].hex())
print("saved        :", OUT.name)
print("flag ada di gambar JPEG (teks di sebelah kanan).")
