#!/usr/bin/env python3
"""My Lovely Freya - recover the rows hidden after the declared PNG height.

IHDR declares 1024x1200, but the IDAT stream contains 1536 rows.  The
extra 336 rows were appended after the visible image.  Pillow (and every
normal PNG viewer) stops at the declared height, so the extra rows never
appear on screen.
"""
from pathlib import Path
import struct
import zlib

from PIL import Image

PNG = Path("/tmp/opencode/nfx/freya/freya_sayangkuh.png")
VISIBLE_H = 1200
OUT = Path("/home/bocil/ctf/nfx/writeups/assets/my-lovely-freya/01-hidden-rows.png")


def unfilter(raw: bytes, width: int, height: int, bpp: int = 3) -> bytes:
    stride = width * bpp
    out = bytearray()
    prev = bytearray(stride)
    pos = 0
    for _ in range(height):
        ft = raw[pos]
        pos += 1
        line = bytearray(raw[pos:pos + stride])
        pos += stride
        if ft == 1:
            for x in range(stride):
                a = line[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + a) & 0xFF
        elif ft == 2:
            for x in range(stride):
                line[x] = (line[x] + prev[x]) & 0xFF
        elif ft == 3:
            for x in range(stride):
                a = line[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + ((a + prev[x]) >> 1)) & 0xFF
        elif ft == 4:
            for x in range(stride):
                a = line[x - bpp] if x >= bpp else 0
                b = prev[x]
                c = prev[x - bpp] if x >= bpp else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[x] = (line[x] + pr) & 0xFF
        out += line
        prev = line
    return bytes(out)


def main() -> None:
    data = PNG.read_bytes()
    i = 8
    idat = b""
    width = height = None
    while i < len(data):
        length = struct.unpack(">I", data[i:i + 4])[0]
        ctype = data[i + 4:i + 8]
        chunk = data[i + 8:i + 8 + length]
        if ctype == b"IHDR":
            width, height, depth, color = struct.unpack(">IIBB", chunk[:10])
            print(f"IHDR: {width}x{height}, bit_depth={depth}, color_type={color}")
        elif ctype == b"IDAT":
            idat += chunk
        i += 12 + length

    raw = zlib.decompress(idat)
    stride = width * 3 + 1
    actual_h = len(raw) // stride
    print(f"decompressed IDAT bytes: {len(raw)}")
    print(f"rows actually present  : {actual_h}")
    print(f"declared rows          : {height}")
    print(f"hidden rows            : {actual_h - height}")

    full = unfilter(raw, width, actual_h)
    extra = full[VISIBLE_H * width * 3:]
    img = Image.frombytes("RGB", (width, actual_h - height), extra)
    img.save(OUT)
    print(f"hidden rows written to : {OUT}")


if __name__ == "__main__":
    main()
