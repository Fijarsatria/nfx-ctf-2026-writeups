# Hard Feistel — Solver lengkap

[← Overview](44-hard-feistel.md) · [Index](index.md)

## 3.2 Solver lengkap

File: `writeups/assets/hard-feistel/solve_feistel.py`

```python
#!/usr/bin/env python3
# Solver Hard Feistel — NFX CTF 2026 (Reverse / Hard)
# 16 ronde Feistel pada blok 32-bit (L,R 16-bit).
#   F(R,K) = (((R * 0x9e3779b1) mod 2^32) >> 5) XOR ((K * 257) & 0xffff)
#   round: (L,R) = (R, L XOR F(R,K_i))
# 16 round key 16-bit di .rodata 0x2060; ciphertext 40 byte di .data 0x4020.
# Output tiap blok = big-endian(L16) || big-endian(R16) -> invertibel.
import argparse
import pathlib
import struct
import subprocess
import sys

from elftools.elf.elffile import ELFFile

ROOT = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_BIN = ROOT / "reverse" / "Hard_02_Feistel" / "hard_feistel"

M32 = 0xFFFFFFFF
M16 = 0xFFFF
C = 0x9E3779B1

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

def F(r: int, k: int) -> int:
    return ((((r * C) & M32) >> 5) ^ ((k * 257) & M16)) & M16

def encrypt_block(L: int, R: int, keys: list[int]) -> tuple[int, int]:
    for k in keys:
        L, R = R, (L ^ F(R, k)) & M16
    return L, R

def decrypt_block(L: int, R: int, keys: list[int]) -> tuple[int, int]:
    # Feistel invertibel: tidak perlu menginversi F.
    # (L_i, R_i) = (R_{i+1} XOR F(L_{i+1}, K_i), L_{i+1})
    for k in reversed(keys):
        L, R = (R ^ F(L, k)) & M16, L
    return L, R

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bin", default=str(DEFAULT_BIN))
    args = ap.parse_args()
    path = pathlib.Path(args.bin)

    # 0x1156 lea r8,[rip+0xf43] -> round keys 0x2060 (16 x uint32, nilai 16-bit)
    # 0x11de lea rsi,[rip+0x2e3b] -> ciphertext 0x4020 (di .data)
    # 0x11d9 mov edx,0x28          -> 40 byte
    keys_raw = read_vaddr(path, 0x2060, 64)
    keys = list(struct.unpack("<16I", keys_raw))
    ct = read_vaddr(path, 0x4020, 40)

    print(f"[*] binary     : {path}")
    print(f"[*] round keys : {len(keys)} x 16-bit")
    print("    " + " ".join(f"{k:#06x}" for k in keys))
    print(f"[*] ciphertext : {ct.hex()}")

    pt = bytearray()
    for off in range(0, len(ct), 4):
        L = (ct[off] << 8) | ct[off + 1]
        R = (ct[off + 2] << 8) | ct[off + 3]
        L, R = decrypt_block(L, R, keys)
        block = bytes([L >> 8, L & 0xFF, R >> 8, R & 0xFF])
        pt += block
        print(f"[*] blok @{off:02d}: ct={ct[off:off+4].hex()} -> "
              f"L0={L:#06x} R0={R:#06x} = {block!r}")

    # Verifikasi: enkripsi ulang harus menghasilkan ciphertext asli.
    check = bytearray()
    for off in range(0, len(pt), 4):
        L = (pt[off] << 8) | pt[off + 1]
        R = (pt[off + 2] << 8) | pt[off + 3]
        L, R = encrypt_block(L, R, keys)
        check += bytes([L >> 8, L & 0xFF, R >> 8, R & 0xFF])
    print(f"[*] enkripsi ulang == ciphertext: {bytes(check) == ct}")

    flag = bytes(pt).rstrip(b"\x00").decode()
    print(f"[+] FLAG       : {flag}")
    proc = subprocess.run([str(path), flag], capture_output=True, text=True)
    print(f"[*] verifikasi : stdout={proc.stdout.strip()!r} rc={proc.returncode}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```
