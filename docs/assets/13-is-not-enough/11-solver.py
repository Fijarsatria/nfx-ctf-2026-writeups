#!/usr/bin/env python3
"""Solver for NFX CTF 2026 — 13 Is Not Enough.

Layers:
  1. XOR every byte with 0x0D (13)
  2. Reverse the string
  3. ROT13 the letters
  4. Shift every digit back by 3 (mod 10)
"""
import codecs

ciphertext = r"p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L"

step1 = "".join(chr(ord(c) ^ 13) for c in ciphertext)
step2 = step1[::-1]
step3 = codecs.decode(step2, "rot_13")
flag = "".join(str((int(c) - 3) % 10) if c.isdigit() else c for c in step3)

print("[0] ciphertext :", ciphertext)
print("[1] XOR 0x0D   :", step1)
print("[2] reverse    :", step2)
print("[3] ROT13      :", step3)
print("[4] digit -3   :", flag)
print("FLAG           :", flag)
assert flag == "NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}"
