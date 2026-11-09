# Medium TEA — Solver lengkap

[← Overview](47-medium-tea.md) · [Index](index.md)

## 3.2 Solver lengkap

File: `writeups/assets/medium-tea/solve_tea.py`

```python
#!/usr/bin/env python3
# Solver Medium TEA — NFX CTF 2026 (Reverse / Medium)
# Binary memakai varian TEA 32 ronde dengan konstanta kustom:
#   k0=0x1337beef  k1=0xcafebabe  k2=0xdeadc0de  k3=0x0badf00d
#   delta=0x9e3779b9 (direpresentasikan sebagai sub 0x61c88647)
# Ciphertext: 5 blok 64-bit di .rodata 0x2040.
import argparse
import pathlib
import struct
import subprocess
import sys

from elftools.elf.elffile import ELFFile

ROOT = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_BIN = ROOT / "reverse" / "Medium_02_TEA" / "medium_tea"

M32 = 0xFFFFFFFF
DELTA = 0x9E3779B9
K = (0x1337BEEF, 0xCAFEBABE, 0xDEADC0DE, 0x0BADF00D)

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

def tea_encrypt_block(v0: int, v1: int) -> tuple[int, int]:
    s = 0
    for _ in range(32):
        s = (s + DELTA) & M32
        v0 = (v0 + ((((v1 << 4) + K[0]) & M32) ^ ((v1 + s) & M32) ^ ((v1 >> 5) + K[1]))) & M32
        v1 = (v1 + ((((v0 << 4) + K[2]) & M32) ^ ((v0 + s) & M32) ^ ((v0 >> 5) + K[3]))) & M32
    return v0, v1

def tea_decrypt_block(v0: int, v1: int) -> tuple[int, int]:
    s = 0xC6EF3720  # 32 * delta mod 2^32
    for _ in range(32):
        v1 = (v1 - ((((v0 << 4) + K[2]) & M32) ^ ((v0 + s) & M32) ^ ((v0 >> 5) + K[3]))) & M32
        v0 = (v0 - ((((v1 << 4) + K[0]) & M32) ^ ((v1 + s) & M32) ^ ((v1 >> 5) + K[1]))) & M32
        s = (s - DELTA) & M32
    return v0, v1

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bin", default=str(DEFAULT_BIN))
    args = ap.parse_args()
    path = pathlib.Path(args.bin)

    # 0x1140 lea r10,[rip+0xef9] -> ciphertext 0x2040
    # 0x1156..0x11dc loop 5 blok; 0x10f4 cmp rax,0x28 -> 40 byte
    ct = read_vaddr(path, 0x2040, 40)
    print(f"[*] binary     : {path}")
    print(f"[*] ciphertext : {ct.hex()}")
    print(f"[*] key words  : " + " ".join(f"{x:#010x}" for x in K))
    print(f"[*] delta      : {DELTA:#010x}; sum akhir = {0xC6EF3720:#010x}")

    pt = bytearray()
    for off in range(0, len(ct), 8):
        v0, v1 = struct.unpack_from("<II", ct, off)
        a, b = tea_decrypt_block(v0, v1)
        pt += struct.pack("<II", a, b)
        print(f"[*] blok @{off:02d}: {v0:08x} {v1:08x} -> {a:08x} {b:08x} "
              f"({pt[-8:].decode('latin-1')!r})")

    # Verifikasi enkripsi ulang harus identik dengan ciphertext.
    check = bytearray()
    for off in range(0, len(pt), 8):
        v0, v1 = struct.unpack_from("<II", pt, off)
        check += struct.pack("<II", *tea_encrypt_block(v0, v1))
    print(f"[*] enkripsi ulang == ciphertext: {bytes(check) == ct}")

    flag = pt.decode()
    print(f"[+] FLAG       : {flag}")
    proc = subprocess.run([str(path), flag], capture_output=True, text=True)
    print(f"[*] verifikasi : stdout={proc.stdout.strip()!r} rc={proc.returncode}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```
