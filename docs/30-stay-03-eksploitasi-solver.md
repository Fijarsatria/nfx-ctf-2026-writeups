# Stay — Eksploitasi / Solver

[← Overview](30-stay.md) · [Index](index.md)

### 3.1 Strategi

1. Ambil code block lirik dari deskripsi.
2. Filter hanya empat code point zero-width.
3. Petakan tiap code point ke 2 bit.
4. Kelompokkan 8 bit menjadi byte.
5. Decode Base64.
6. XOR dengan `falling`.
7. Verifikasi hasil sama dengan flag.

### 3.2 Solver

```python
#!/usr/bin/env python3
# assets/stay/solve_stay.py (ringkas)
from pathlib import Path
import base64
import re

DESC = Path("/tmp/opencode/nfx/stay.desc.txt")
MAPPING = {
    "\u200c": "00",
    "\u2060": "01",
    "\u200b": "10",
    "\u200d": "11",
}

text = DESC.read_text(encoding="utf-8")
block = re.search(r"```\n(.*?)\n```", text, re.S).group(1)
hidden = [c for c in block if c in MAPPING]
bits = "".join(MAPPING[c] for c in hidden)

encoded = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
raw = base64.b64decode(encoded, validate=True)

key = b"falling"
plain = bytes(v ^ key[i % len(key)] for i, v in enumerate(raw))

print("zero-width characters :", len(hidden))
print("bit length            :", len(bits))
print("base64 text           :", encoded.decode())
print("after base64 (hex)    :", raw.hex())
print("plaintext             :", plain.decode())
assert plain == b"NXCTF{st4y_w1th_m3_1n_th3_d4rk}"
print("assertion             : PASS")
```

### 3.3 Output asli

```text
$ python3 solve_stay.py
zero-width characters : 176
  '\u200c' -> 00 : 39
  '\u2060' -> 01 : 79
  '\u200b' -> 10 : 32
  '\u200d' -> 11 : 26
bit length            : 352
base64 text           : KDkvOC8VFBJVFTMeXxMOPgFfNl8JORUEXzYKUxQKEQ==
after base64 (hex)    : 28392f382f1514125515331e5f130e3e015f365f093915045f360a53140a11
xor key               : b'falling'
plaintext             : NXCTF{st4y_w1th_m3_1n_th3_d4rk}
assertion             : PASS
```
