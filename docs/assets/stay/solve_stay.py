#!/usr/bin/env python3
"""Stay - zero-width Unicode -> base64 -> repeating-key XOR.

The challenge gives only the lyric text (no attachment).  The invisible
characters interleaved with the lyrics are four different zero-width code
points, each carrying two bits:

    U+200C ZERO WIDTH NON-JOINER   -> 00
    U+2060 WORD JOINER             -> 01
    U+200B ZERO WIDTH SPACE        -> 10
    U+200D ZERO WIDTH JOINER       -> 11

176 characters * 2 bits = 352 bits = 44 bytes.  Those bytes are Base64;
after decoding, XOR with the song-themed key "falling".
"""
from pathlib import Path
import base64
import re

DESC = Path("/tmp/opencode/nfx/stay.desc.txt")
OUT = Path("/home/bocil/ctf/nfx/writeups/assets/stay")

MAPPING = {
    "\u200c": "00",
    "\u2060": "01",
    "\u200b": "10",
    "\u200d": "11",
}


def main() -> None:
    text = DESC.read_text(encoding="utf-8")
    block = re.search(r"```\n(.*?)\n```", text, re.S).group(1)
    hidden = [c for c in block if c in MAPPING]
    print(f"zero-width characters : {len(hidden)}")
    counts = {repr(k): sum(c == k for c in hidden) for k in MAPPING}
    for k, v in counts.items():
        print(f"  {k} -> {MAPPING[eval(k)]} : {v}")

    bits = "".join(MAPPING[c] for c in hidden)
    print(f"bit length            : {len(bits)}")
    encoded = bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8))
    print(f"base64 text           : {encoded.decode('ascii')}")

    raw = base64.b64decode(encoded, validate=True)
    print(f"after base64 (hex)    : {raw.hex()}")

    key = b"falling"
    plain = bytes(v ^ key[i % len(key)] for i, v in enumerate(raw))
    print(f"xor key               : {key!r}")
    print(f"plaintext             : {plain.decode('ascii')}")

    OUT.joinpath("01-zero-width-sequence.txt").write_text("".join(hidden), encoding="utf-8")
    OUT.joinpath("02-bitstream.txt").write_text(bits, encoding="utf-8")
    OUT.joinpath("03-plaintext.txt").write_text(plain.decode("ascii") + "\n", encoding="utf-8")
    assert plain == b"NXCTF{st4y_w1th_m3_1n_th3_d4rk}", plain
    print("assertion             : PASS")


if __name__ == "__main__":
    main()
