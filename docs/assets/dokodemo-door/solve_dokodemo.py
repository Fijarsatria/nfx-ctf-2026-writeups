#!/usr/bin/env python3
"""Dokodemo Door - repeating-key XOR PDF recovery.

The file is a PDF XOR-ed with a repeating key.  We know two cribs:
  * the file must start with "%PDF-1.4\n"
  * the file must end with   "%%EOF\n"
For every candidate key length we derive the key bytes covered by the
cribs, require that the two derivations agree, brute-force any remaining
key byte(s) if there is only one, and score the result.
"""
from pathlib import Path
import itertools
import re

SRC = Path("/home/bocil/ctf/nfx/crypto/Dokodemo_Door/rahasia.pdf")
OUT = Path("/tmp/opencode/dokodemo_decrypted.pdf")

HEAD = b"%PDF-1.4\n"
TAIL = b"%%EOF\n"


def score(data: bytes) -> int:
    markers = [b"%PDF", b"%%EOF", b" obj", b"endobj", b"stream", b"/Type", b"xref", b"trailer"]
    return sum(data.count(m) * 20 for m in markers) + sum(
        32 <= b < 127 or b in (9, 10, 13) for b in data
    ) // 20


def main() -> None:
    c = SRC.read_bytes()
    n = len(c)
    best = None

    for kl in range(1, 65):
        key = [None] * kl
        ok = True
        # header crib
        for i, p in enumerate(HEAD):
            j = i % kl
            v = c[i] ^ p
            if key[j] is None:
                key[j] = v
            elif key[j] != v:
                ok = False
                break
        if not ok:
            continue
        # trailer crib
        off = n - len(TAIL)
        for i, p in enumerate(TAIL):
            j = (off + i) % kl
            v = c[off + i] ^ p
            if key[j] is None:
                key[j] = v
            elif key[j] != v:
                ok = False
                break
        if not ok:
            continue

        unknown = [i for i, v in enumerate(key) if v is None]
        if len(unknown) > 2:
            continue
        candidates = itertools.product(range(256), repeat=len(unknown))
        for fill in candidates:
            kk = key[:]
            for idx, val in zip(unknown, fill):
                kk[idx] = val
            dec = bytes(b ^ kk[i % kl] for i, b in enumerate(c))
            sc = score(dec)
            if best is None or sc > best[0]:
                best = (sc, kl, bytes(kk), dec, unknown, fill)

    if best is None:
        raise SystemExit("no key found")

    sc, kl, key, dec, unknown, fill = best
    print(f"ciphertext bytes      : {n}")
    print(f"candidate key length  : {kl}")
    print(f"recovered key         : {key!r}")
    print(f"crib-unknown positions: {unknown} filled with {fill}")
    print(f"decrypted header      : {dec[:20]!r}")
    print(f"decrypted trailer     : {dec[-24:]!r}")
    print(f"score                 : {sc}")
    assert dec.startswith(HEAD), "header mismatch"
    assert dec.rstrip(b"\r\n").endswith(b"%%EOF"), "trailer mismatch"
    OUT.write_bytes(dec)
    print(f"written               : {OUT}")


if __name__ == "__main__":
    main()
