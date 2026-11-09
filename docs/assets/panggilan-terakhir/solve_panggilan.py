#!/usr/bin/env python3
"""Ekstrak RTP PCMU/8000 dari korban.pcap menjadi WAV per arah."""
import struct
import wave
import audioop

PCAP = "korban.pcap"

d = open(PCAP, "rb").read()
magic, vmaj, vmin, tz, sig, snap, link = struct.unpack("<IHHIIII", d[:24])
assert magic == 0xA1B2C3D4
print(f"pcap linktype={link} snaplen={snap}")

o = 24
streams = {}
while o + 16 <= len(d):
    ts, tu, incl, orig = struct.unpack("<IIII", d[o:o + 16])
    o += 16
    p = d[o:o + incl]
    o += incl
    ip = p[14:]                      # Ethernet
    if len(ip) < 20 or ip[0] >> 4 != 4 or ip[9] != 17:
        continue
    ihl = (ip[0] & 0xF) * 4
    udp = ip[ihl:]
    sport, dport, ulen, csum = struct.unpack(">HHHH", udp[:8])
    if not (4000 <= sport <= 4002 or 4000 <= dport <= 4002):
        continue
    pay = udp[8:]
    if len(pay) < 12:
        continue
    b0 = pay[0]
    cc = b0 & 0xF
    seq = struct.unpack(">H", pay[2:4])[0]
    tsr = struct.unpack(">I", pay[4:8])[0]
    ssrc = struct.unpack(">I", pay[8:12])[0]
    off = 12 + 4 * cc
    if b0 & 0x10:                    # RTP extension
        extlen = struct.unpack(">H", pay[off + 2:off + 4])[0]
        off += 4 + 4 * extlen
    streams.setdefault((sport, dport, ssrc), []).append((seq, pay[off:]))

for (sp, dp, ssrc), pkts in sorted(streams.items()):
    pkts.sort()
    raw = b"".join(x[1] for x in pkts)
    pcm = audioop.ulaw2lin(raw, 2)
    fn = f"pt_{sp}_{dp}_{ssrc:08x}.wav"
    w = wave.open(fn, "wb")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(8000)
    w.writeframes(pcm)
    w.close()
    print(f"{sp}->{dp} ssrc={ssrc:08x} pkts={len(pkts)} seq={pkts[0][0]}..{pkts[-1][0]} "
          f"payload={len(raw)} durasi={len(raw)/8000:.2f}s -> {fn}")
