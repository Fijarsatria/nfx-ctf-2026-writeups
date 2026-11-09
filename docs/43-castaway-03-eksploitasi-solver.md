# Castaway — Eksploitasi / Solver

[← Overview](43-castaway.md) · [Index](index.md)

### 3.1 Strategi

1. Ekstrak `sbox256` (256 byte), `sbox16` (16 byte), dan ciphertext (40 byte) dari `.rodata`.
2. Untuk tiap byte `i`, coba semua 256 nilai plaintext `p`; hitung transformasi forward dengan `key` saat ini; pilih `p` yang menghasilkan ciphertext `target`.
3. Setelah ketemu, update `key` memakai `target` (karena update key memakai output byte).
4. Untuk byte pertama, coba dua kemungkinan: `target = ct[0]` (anti_debug = 0) dan `target = ct[0] ^ 1` (anti_debug = 1). Pilih hasil yang seluruhnya printable.
5. Verifikasi dengan menjalankan binary tanpa debugger.

Karena S-box 256 byte belum tentu permutasi, brute force 256 kandidat lebih aman daripada mencoba menginversi S-box secara langsung. Pada challenge ini setiap byte menghasilkan tepat satu kandidat.

### 3.2 Solver lengkap

File: `writeups/assets/castaway/solve_castaway.py`

```python
#!/usr/bin/env python3
# Solver Castaway — NFX CTF 2026 (Reverse / Hard)
# Binary membaca 40 byte dari stdin, menjalankan "state machine" dengan opaque
# predicate, lalu membandingkan hasil transformasi dengan 40 byte di .rodata
# 0x2140.
#
# Transformasi per byte i (state key bergulir, awal 0xa5):
#   c = p[i] XOR key
#   c = rol8(c, (i % 7) + 1)
#   c = (c + sbox16[i & 0xf]) & 0xff
#   c = sbox256[c]
#   c = c XOR ((i * 0x2f) & 0xff)
#   out[i] = c
#   key = (i + c - 125 * key) & 0xff
#
# Anti-debug: ptrace(PTRACE_TRACEME) == -1 (mis. di bawah gdb/strace) membuat
# out[0] di-XOR 1 sehingga verifikasi gagal. Saat normal, hasilnya 0.
import argparse
import pathlib
import subprocess
import sys

from elftools.elf.elffile import ELFFile

ROOT = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_BIN = ROOT / "reverse" / "Hard_03_Castaway" / "castaway"

def read_vaddr(path: pathlib.Path, vaddr: int, size: int) -> bytes:
    with open(path, "rb") as f:
        elf = ELFFile(f)
        for seg in elf.iter_segments():
            if seg["p_type"] != "PT_LOAD":
                continue
            start, filesz = seg["p_vaddr"], seg["p_filesz"]
            if start <= vaddr and vaddr + size <= start + filesz:
                f.seek(seg["p_offset"] + (vaddr - start))
                return f.read(size)
    raise ValueError(f"vaddr {vaddr:#x} tidak ditemukan")

def rol8(x: int, n: int) -> int:
    n &= 7
    return ((x << n) | (x >> ((8 - n) & 7))) & 0xFF if n else x & 0xFF

def transform(data: bytes, sbox: bytes, sbox16: bytes) -> bytes:
    key = 0xA5
    out = bytearray()
    for i, p in enumerate(data):
        c = p ^ key
        c = rol8(c, (i % 7) + 1)
        c = (c + sbox16[i & 0xF]) & 0xFF
        c = sbox[c]
        c ^= (i * 0x2F) & 0xFF
        out.append(c)
        key = (i + c - 125 * key) & 0xFF
    return bytes(out)

def invert(ct: bytes, sbox: bytes, sbox16: bytes) -> tuple[bytes | None, int]:
    """Inversi brute force 256 kandidat per byte; key state dipulihkan berurutan."""
    key = 0xA5
    pt = bytearray()
    for i, target in enumerate(ct):
        found = []
        for p in range(256):
            c = p ^ key
            c = rol8(c, (i % 7) + 1)
            c = (c + sbox16[i & 0xF]) & 0xFF
            c = sbox[c]
            c ^= (i * 0x2F) & 0xFF
            if c == target:
                found.append(p)
        if len(found) != 1:
            return None, key
        pt.append(found[0])
        key = (i + target - 125 * key) & 0xFF
    return bytes(pt), key

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bin", default=str(DEFAULT_BIN))
    args = ap.parse_args()
    path = pathlib.Path(args.bin)

    # Alamat dari disassembly:
    #   0x137e lea rdx,[rip+0xc9b] -> sbox256 0x2020
    #   0x136a lea rax,[rip+0xdaf] -> sbox16  0x2120
    #   0x1564 lea rcx,[rip+0xbd5] -> ciphertext 0x2140 (40 byte)
    sbox = read_vaddr(path, 0x2020, 256)
    sbox16 = read_vaddr(path, 0x2120, 16)
    ct = read_vaddr(path, 0x2140, 40)

    print(f"[*] binary        : {path}")
    print(f"[*] sbox256       : {sbox[:16].hex(' ')} ... ({len(sbox)} byte)")
    print(f"[*] sbox16        : {sbox16.hex(' ')}")
    print(f"[*] ciphertext    : {ct.hex()}")
    print(f"[*] ptrace normal : return 0 -> out[0] tidak di-XOR")

    # anti_debug=0 -> eksekusi normal; anti_debug=1 -> simulasi ptrace gagal.
    for anti in (0, 1):
        adjusted = bytes([ct[0] ^ anti]) + ct[1:]
        pt, _ = invert(adjusted, sbox, sbox16)
        ok = pt is not None and all(32 <= b < 127 for b in pt)
        print(f"[*] anti_debug={anti}: {'valid' if ok else 'tidak valid'} "
              f"-> {pt!r}")
        if ok:
            flag = pt.decode()
            # Buktikan transformasi forward menghasilkan ciphertext (mode normal).
            assert transform(pt, sbox, sbox16) == adjusted
            print(f"[+] FLAG          : {flag}")
            proc = subprocess.run([str(path)], input=flag + "\n",
                                  capture_output=True, text=True)
            print(f"[*] verifikasi    : stdout={proc.stdout.strip()!r} rc={proc.returncode}")

    print("[*] Catatan: state 0x32 (output[0]=0xff) adalah dead code karena")
    print("    opaque predicate (i*i & 3) == 2 tidak pernah benar untuk integer.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

### 3.3 Output asli

```text
$ python3 writeups/assets/castaway/solve_castaway.py
[*] binary        : /home/bocil/ctf/nfx/reverse/Hard_03_Castaway/castaway
[*] sbox256       : 0a dd ef 13 16 8c fb f9 22 08 b9 71 03 9d 27 c3 ... (256 byte)
[*] sbox16        : dc 5a c5 d4 1c d2 bb 6b 82 5c 9a f1 d1 96 76 bd
[*] ciphertext    : d554ada841e3e679f6bf13d01d319dd72db7cd6ea9c8e8a4957bcacbb55f16f0362681c32cfb9b74
[*] ptrace normal : return 0 -> out[0] tidak di-XOR
[*] anti_debug=0: valid -> b'NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}'
[+] FLAG          : NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}
[*] verifikasi    : stdout='flag> Access granted.' rc=0
[*] anti_debug=1: tidak valid -> b'\xfaA\xe7`\xc4K\xfeK\t\xd4\x91\xd0\xda!\x81\xc4\x01/\x9c\xff\x9f\x83>\\~~\\]\xff\x07\xce\x942\xb5f\x11\x1e\x1f$\xda'
[*] Catatan: state 0x32 (output[0]=0xff) adalah dead code karena
    opaque predicate (i*i & 3) == 2 tidak pernah benar untuk integer.
```

`anti_debug=1` menghasilkan byte non-printable, jadi kandidat itu ditolak. Hanya `anti_debug=0` yang menghasilkan flag valid.
