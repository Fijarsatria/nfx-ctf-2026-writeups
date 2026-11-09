# Hard Feistel — Eksploitasi / Solver

[← Overview](44-hard-feistel.md) · [Index](index.md)

### 3.1 Strategi

1. Ekstrak 16 round key dari `.rodata` `0x2060`.
2. Ekstrak ciphertext 40 byte dari `.data` `0x4020`.
3. Untuk tiap blok 4 byte, baca `L16` dan `R16` big-endian.
4. Jalankan inverse Feistel 16 ronde.
5. Tulis `L0` dan `R0` big-endian, gabungkan 10 blok.
6. Buang padding `\x00` di akhir, verifikasi dengan binary.
7. Enkripsi ulang untuk memastikan hasilnya sama dengan ciphertext.

### 3.2 Solver lengkap

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

### 3.3 Output asli

```text
$ python3 writeups/assets/hard-feistel/solve_feistel.py
[*] binary     : /home/bocil/ctf/nfx/reverse/Hard_02_Feistel/hard_feistel
[*] round keys : 16 x 16-bit
    0x005a 0x0079 0x0098 0x00b7 0x00d6 0x00f5 0x0014 0x0033 0x0052 0x0071 0x0090 0x00af 0x00ce 0x00ed 0x000c 0x002b
[*] ciphertext : b949ad0bcc2c088063ec6501c0776b744cb390a40840aeb3ff87facc95252c4d11b585907ca91072
[*] blok @00: ct=b949ad0b -> L0=0x4e46 R0=0x587b = b'NFX{'
[*] blok @04: ct=cc2c0880 -> L0=0x6633 R0=0x3135 = b'f315'
[*] blok @08: ct=63ec6501 -> L0=0x7433 R0=0x6c5f = b't3l_'
[*] blok @12: ct=c0776b74 -> L0=0x6e33 R0=0x7477 = b'n3tw'
[*] blok @16: ct=4cb390a4 -> L0=0x3072 R0=0x6b5f = b'0rk_'
[*] blok @20: ct=0840aeb3 -> L0=0x3136 R0=0x5f72 = b'16_r'
[*] blok @24: ct=ff87facc -> L0=0x3075 R0=0x6e64 = b'0und'
[*] blok @28: ct=95252c4d -> L0=0x355f R0=0x7233 = b'5_r3'
[*] blok @32: ct=11b58590 -> L0=0x7633 R0=0x7273 = b'v3rs'
[*] blok @36: ct=7ca91072 -> L0=0x3364 R0=0x7d00 = b'3d}\x00'
[*] enkripsi ulang == ciphertext: True
[+] FLAG       : NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}
[*] verifikasi : stdout='Correct! Jaringan Feistel berhasil dibalik.' rc=0
```

Blok terakhir berisi `3d 7d 00` — `}` diikuti padding nol. Itu sebabnya flag efektif 39 byte, sementara buffer 40 byte.

### 3.4 Verifikasi tambahan dengan gdb

Untuk memastikan pemahaman serialisasi output benar, binary dijalankan di gdb dengan flag yang benar. Breakpoint dipasang tepat sebelum `memcmp` (setelah loop transformasi, `0x11d9`). Buffer hasil transformasi dibandingkan dengan ciphertext di `.data`:

```text
PIE base = 0x555555554000
Breakpoint 1 at 0x5555555551d9
buffer hasil transformasi (r9):
0x7fffffffded0: 0xb9 0x49 0xad 0x0b 0xcc 0x2c 0x08 0x80
0x7fffffffded8: 0x63 0xec 0x65 0x01 0xc0 0x77 0x6b 0x74
...
buffer ciphertext (.data 0x4020):
0x555555558020: 0xb9 0x49 0xad 0x0b 0xcc 0x2c 0x08 0x80
0x555555558028: 0x63 0xec 0x65 0x01 0xc0 0x77 0x6b 0x74
...
input mentah di stack (rsp):
0x7fffffffddd0: 0x4e 0x46 0x58 0x7b 0x66 0x33 0x31 0x35
...
```

Output buffer identik dengan ciphertext, dan input mentah adalah flag. Ini mengonfirmasi model enkripsi/dekripsi.
