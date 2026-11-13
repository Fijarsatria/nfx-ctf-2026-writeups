#!/usr/bin/env python3
# Solver Medium RC4 — NFX CTF 2026 (Reverse / Medium)
# Analisis: binary medium_rc4 memakai RC4 dengan key hardcoded di .rodata
#           dan ciphertext 42 byte di 0x2060. RC4 simetris -> dekripsi = enkripsi.
import argparse
import pathlib
import struct
import subprocess
import sys

from elftools.elf.elffile import ELFFile

DEFAULT_BIN = pathlib.Path(__file__).resolve().parent / "medium_rc4"


def read_vaddr(path: pathlib.Path, vaddr: int, size: int) -> bytes:
    """Ambil `size` byte dari alamat virtual `vaddr` memakai program header PT_LOAD."""
    with open(path, "rb") as f:
        elf = ELFFile(f)
        for seg in elf.iter_segments():
            if seg["p_type"] != "PT_LOAD":
                continue
            start, filesz = seg["p_vaddr"], seg["p_filesz"]
            if start <= vaddr and vaddr + size <= start + filesz:
                f.seek(seg["p_offset"] + (vaddr - start))
                return f.read(size)
    raise ValueError(f"vaddr {vaddr:#x} tidak ditemukan di PT_LOAD")


def rc4(key: bytes, data: bytes) -> bytes:
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) & 0xFF
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = bytearray()
    for b in data:
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        out.append(b ^ S[(S[i] + S[j]) & 0xFF])
    return bytes(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bin", default=str(DEFAULT_BIN))
    args = ap.parse_args()
    path = pathlib.Path(args.bin)

    # Alamat dari disassembly:
    #   0x1173  lea r10,[rip+0xea7]  -> key  = 0x2021
    #   0x123e  mov edx,0x2a         -> panjang ciphertext = 42
    #   0x1243  lea rsi,[rip+0xe16]  -> ciphertext = 0x2060
    key = read_vaddr(path, 0x2021, 0x13)       # "n0t_s3cur3_k3y_2026"
    ct = read_vaddr(path, 0x2060, 0x2A)

    print(f"[*] binary      : {path}")
    print(f"[*] key (hex)   : {key.hex()}  ({key!r})")
    print(f"[*] ciphertext  : {ct.hex()}")
    print(f"[*] panjang ct  : {len(ct)} byte")
    pt = rc4(key, ct)
    print(f"[+] plaintext   : {pt!r}")

    try:
        flag = pt.decode()
        print(f"[+] FLAG        : {flag}")
        proc = subprocess.run([str(path), flag], capture_output=True, text=True)
        print(f"[*] verifikasi  : stdout={proc.stdout.strip()!r} rc={proc.returncode}")
    except UnicodeDecodeError:
        print("[!] plaintext bukan teks UTF-8", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
