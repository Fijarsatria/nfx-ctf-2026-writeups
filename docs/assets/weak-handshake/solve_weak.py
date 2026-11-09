#!/usr/bin/env python3
"""Weak Handshake solver.

1. Reassemble TCP streams dari wh.pcap (Linux SLL2 / linktype 276).
2. Ambil file FTP clannad.webp (port 42345).
3. Ambil sertifikat RSA dari ServerHello.
4. Fermat factorization (p dan q berselisih 236) -> private key.
5. Decrypt TLS 1.2 RSA + AES-128-CBC-SHA dengan Extended Master Secret.
6. Tulis HTTP response + JPEG hasil dekripsi.
"""
import hashlib
import hmac
import struct
import sys
from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse

PCAP = "wh.pcap"

# ---------- 1. baca pcap + reassemble TCP ----------
d = open(PCAP, "rb").read()
magic, vmaj, vmin, tz, sig, snap, link = struct.unpack("<IHHIIII", d[:24])
assert magic == 0xA1B2C3D4 and link == 276, "butuh pcap linktype LINUX_SLL2"

o = 24
streams = {}
while o + 16 <= len(d):
    ts, tu, incl, orig = struct.unpack("<IIII", d[o:o + 16])
    o += 16
    p = d[o:o + incl]
    o += incl
    ip = p[20:]  # SLL2 header 20 byte
    if len(ip) < 20 or ip[0] >> 4 != 4 or ip[9] != 6:
        continue
    ihl = (ip[0] & 0xF) * 4
    tcp = ip[ihl:]
    if len(tcp) < 20:
        continue
    sport, dport, seq, ack, off_flags = struct.unpack(">HHIIH", tcp[:14])
    doff = (off_flags >> 12) * 4
    pay = tcp[doff:]
    if not pay:
        continue
    key = (ip[12:16], sport, ip[16:20], dport)
    streams.setdefault(key, []).append((seq, pay))

def reassemble(pkts):
    pkts.sort()
    out = b""
    last = None
    for seq, pay in pkts:
        if last is None or seq >= last:
            if last is not None and seq > last:
                out += b"\x00" * (seq - last)
            out += pay
            last = seq + len(pay)
        elif seq + len(pay) > last:
            out += pay[last - seq:]
            last = seq + len(pay)
    return out

streams = {k: reassemble(v) for k, v in streams.items()}

def pick(sport, dport):
    for (s, sp, dd, dp), data in streams.items():
        if sp == sport and dp == dport:
            return data
    raise KeyError((sport, dport))

ftp_data = pick(42345, 44956)
open("clannad.webp", "wb").write(ftp_data)
print(f"[+] FTP data clannad.webp: {len(ftp_data)} byte, magic={ftp_data[:12]!r}")

# ---------- 2. parse TLS record ----------
def parse_records(x):
    o = 0
    out = []
    while o + 5 <= len(x):
        typ = x[o]
        ver = x[o + 1:o + 3]
        ln = int.from_bytes(x[o + 3:o + 5], "big")
        out.append((typ, ver, x[o + 5:o + 5 + ln]))
        o += 5 + ln
    return out

def decrypt_session(cport, tag):
    client = parse_records(pick(cport, 8443))
    server = parse_records(pick(8443, cport))
    ch = client[0][2]
    sh = server[0][2]
    crandom = ch[6:38]
    srandom = sh[6:38]

    cke = client[1][2]
    hslen = int.from_bytes(cke[1:4], "big")
    body = cke[4:4 + hslen]
    elen = int.from_bytes(body[:2], "big")
    enc = body[2:2 + elen]

    # cert dari ServerHello Certificate (handshake header 4 byte + list header 3 byte)
    hs = server[1][2]
    hlen = int.from_bytes(hs[1:4], "big")
    cert_list = hs[4:4 + hlen]
    clen = int.from_bytes(cert_list[3:6], "big")
    der = cert_list[6:6 + clen]
    open("tomoyo_cert.der", "wb").write(der)
    from cryptography import x509
    cert = x509.load_der_x509_certificate(der)
    pubnums = cert.public_key().public_numbers()
    n, e = pubnums.n, pubnums.e
    print(f"[+] cert RSA {n.bit_length()} bit, e={e}")

    # ---------- 3. Fermat ----------
    import math
    a = math.isqrt(n)
    if a * a < n:
        a += 1
    for i in range(2_000_000):
        b2 = a * a - n
        b = math.isqrt(b2)
        if b * b == b2:
            p, q = a - b, a + b
            print(f"[+] Fermat factor i={i}: p-q={q-p}")
            break
        a += 1
    else:
        raise SystemExit("Fermat gagal")
    dpriv = inverse(e, (p - 1) * (q - 1))
    key = RSA.construct((n, e, dpriv, p, q))
    open("tomoyo_priv.pem", "wb").write(key.export_key("PEM"))

    pre = PKCS1_v1_5.new(key).decrypt(enc, None)
    print(f"[+] premaster: {pre.hex()}")

    # ---------- 4. Extended Master Secret ----------
    transcript = ch + sh + server[1][2] + server[2][2] + cke
    sess_hash = hashlib.sha256(transcript).digest()

    def p_hash(secret, seed, length):
        out = b""
        A = seed
        while len(out) < length:
            A = hmac.new(secret, A, hashlib.sha256).digest()
            out += hmac.new(secret, A + seed, hashlib.sha256).digest()
        return out[:length]

    def prf(secret, label, seed, length):
        return p_hash(secret, label + seed, length)

    master = prf(pre, b"extended master secret", sess_hash, 48)
    kb = prf(master, b"key expansion", srandom + crandom, 104)
    sw_mac, sw_key = kb[20:40], kb[56:72]
    print(f"[+] master: {master.hex()}")
    print(f"[+] server_write_key: {sw_key.hex()}")

    idx = next(i for i, r in enumerate(server) if r[0] == 20)
    http = b""
    for typ, ver, body in server[idx + 1:]:
        iv = body[:16]
        ct = body[16:-20]          # 20 byte MAC di luar ciphertext
        pt = AES.new(sw_key, AES.MODE_CBC, iv=iv).decrypt(ct)
        pad = pt[-1]
        if 1 <= pad <= 16 and pt[-pad:] == bytes([pad]) * pad:
            pt = pt[:-pad]
        http += pt
    # buang Finished (16 byte) + sisa 1 byte padding record pertama
    if http.startswith(b"\x14\x00\x00\x0c"):
        http = http[16:]
    out = f"http_{tag}.bin"
    open(out, "wb").write(http)
    print(f"[+] {out}: {len(http)} byte")
    print(http[:300].decode("latin1", "replace"))

    # ambil JPEG
    i = http.find(b"\xff\xd8\xff")
    j = http.find(b"\xff\xd9", i) + 2
    open(f"tomoyo_{tag}.jpg", "wb").write(http[i:j])
    print(f"[+] tomoyo_{tag}.jpg: {j-i} byte")

for cport, tag in [(56410, "s1"), (56422, "s2")]:
    decrypt_session(cport, tag)
