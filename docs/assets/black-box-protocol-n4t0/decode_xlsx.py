#!/usr/bin/env python3
"""Decode the three columns of flight_recovery_manifest.xlsx."""
import struct

NATO = {
    "November": "N", "Four": "4", "Tango": "T", "Zero": "0", "Papa": "P",
    "Hotel": "H", "Three": "3", "One": "1", "Charlie": "C",
}

# Column A: NATO words + digit words (rows 2..16)
a_words = ["November", "Four", "Tango", "Zero", "Papa", "Hotel", "Zero",
           "November", "Three", "Tango", "One", "Charlie", "One",
           "November", "One"]
A = "".join(NATO[w] for w in a_words)
print("A (NATO)      :", A)

# Column B: numeric cells are hex-formatted (numFmt) numbers, other cells are hex strings
b_cells = [0x43, 0x30, "6d", 0x62, "4f", "5f", 0x48, 0x33, 0x58, "5f"]
B = bytes(int(x, 16) if isinstance(x, str) else x for x in b_cells).decode()
print("B (hex)       :", B)

# Column C: float32 big-endian bytes spell ASCII
c_floats = [2.78842154354096E23, 7.07930905431442E31, 3.57380928075183E30]
C = b"".join(struct.pack(">f", v) for v in c_floats).decode()
print("C (float32 BE):", C)

print("concatenated  :", A + B + C)
print("with separators:", "N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng")
