#!/usr/bin/env python3
"""Dekripsi GNOME Keyring lama (format GnomeKeyring) + parse item.
Terverifikasi: password login mizore = Bluebirds1927!
"""
import hashlib
import hmac
import struct
import sys
from Crypto.Cipher import AES

PATH = "03-login.keyring"

d = open(PATH, "rb").read()
assert d.startswith(b"GnomeKeyring\n\r\0\n"), "bukan keyring GNOME lama"

o = 16
major, minor, crypto, hash_t = d[o:o + 4]
o += 4
name_len = struct.unpack(">I", d[o:o + 4])[0]
o += 4
name = d[o:o + name_len]
o += name_len
ctime = int.from_bytes(d[o:o + 8], "big")
o += 8
mtime = int.from_bytes(d[o:o + 8], "big")
o += 8
flags, lock_timeout, iterations = struct.unpack(">III", d[o:o + 12])
o += 12
salt = d[o:o + 8]
o += 8
o += 16  # reserved
num_items = struct.unpack(">I", d[o:o + 4])[0]
o += 4

print(f"magic          : GnomeKeyring")
print(f"version/crypto : {major}.{minor} / crypto={crypto} / hash={hash_t}")
print(f"keyring name   : {name.decode()}")
print(f"iterations     : {iterations}")
print(f"salt           : {salt.hex()}")
print(f"num_items      : {num_items}")


def getstr(o):
    n = struct.unpack(">I", d[o:o + 4])[0]
    o += 4
    if n == 0xffffffff:
        return None, o
    return d[o:o + n], o + n


items = []
for _ in range(num_items):
    iid, typ, nattr = struct.unpack(">III", d[o:o + 12])
    o += 12
    attrs = []
    for _ in range(nattr):
        an, o = getstr(o)
        at = struct.unpack(">I", d[o:o + 4])[0]
        o += 4
        if at == 0:
            av, o = getstr(o)
        else:
            av = struct.unpack(">I", d[o:o + 4])[0]
            o += 4
        attrs.append((an.decode(), at, av))
    items.append((iid, typ, attrs))

print("\nPLAINTEXT ITEM HEADER:")
for iid, typ, attrs in items:
    print(f"  id={iid} type={typ}")
    for a in attrs:
        print(f"    {a[0]:10s} type={a[1]} value={a[2]}")

clen = struct.unpack(">I", d[o:o + 4])[0]
o += 4
ct = d[o:o + clen]

# KDF gnome-keyring: SHA256(password || salt), lalu SHA256 berulang iterations-1 kali.
def derive(pw, salt, iterations, need=32):
    dg = hashlib.sha256(pw + salt).digest()
    for _ in range(1, iterations):
        dg = hashlib.sha256(dg).digest()
    out = dg
    while len(out) < need:
        dg = hashlib.sha256(dg).digest()
        out += dg
    return out[:need]

pw = b"Bluebirds1927!"
kv = derive(pw, salt, iterations)
pt = AES.new(kv[:16], AES.MODE_CBC, iv=kv[16:32]).decrypt(ct)
print(f"\nverify MD5     : {hashlib.md5(pt[16:]).hexdigest()} == {pt[:16].hex()} ? {hashlib.md5(pt[16:]).digest() == pt[:16]}")

# Item terdekripsi: display_name, secret, time, time, reserved, 4 int, attrs
def getstr_from(buf, o):
    n = struct.unpack(">I", buf[o:o + 4])[0]
    o += 4
    if n == 0xffffffff:
        return None, o
    return buf[o:o + n], o + n

o = 16
disp, o = getstr_from(pt, o)
secret, o = getstr_from(pt, o)
print(f"\ndisplay_name   : {disp.decode()}")
print("secret         :")
print(secret.decode())
