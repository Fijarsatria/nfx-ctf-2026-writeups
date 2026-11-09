#!/usr/bin/env python3
"""Ekstraksi LSB R/B dari PNG Heker Tersenyum.
Format container yang ditemukan: b"CTF1" + uint32 BE panjang + payload.
"""
import struct
from PIL import Image

IMG = "00-original.png"

im = Image.open(IMG).convert("RGB")
w, h = im.size
px = im.load()
print(f"[*] image: {w}x{h} mode=RGB")
print("[*] urutan bit: row-major (y lalu x), LSB tiap channel")

def extract(channel):
    bits = [px[x, y][channel] & 1 for y in range(h) for x in range(w)]
    out = bytearray()
    for i in range(0, len(bits) - 7, 8):
        v = 0
        for b in bits[i:i + 8]:
            v = (v << 1) | b
        out.append(v)
    return bytes(out)

for channel, name, color in [(0, "R", "merah / baju"), (2, "B", "biru / celana")]:
    d = extract(channel)
    print(f"\n=== channel {name} ({color}) ===")
    print("8 byte pertama :", d[:8].hex(), repr(d[:8]))
    if d[:4] == b"CTF1":
        n = struct.unpack(">I", d[4:8])[0]
        print(f"magic          : CTF1")
        print(f"panjang (BE32) : {n}")
        payload = d[8:8 + n]
        print(f"payload[:32]   : {payload[:32].hex()}")
        fn = f"{name}-payload.bin"
        open(fn, "wb").write(payload)
        print(f"disimpan       : {fn} ({len(payload)} byte)")
    else:
        print("tidak ada magic CTF1")
