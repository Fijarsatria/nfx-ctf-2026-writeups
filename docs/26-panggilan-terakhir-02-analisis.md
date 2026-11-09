# Panggilan Terakhir — Analisis

[← Overview](26-panggilan-terakhir.md) · [Index](index.md)

### 2.1 SIP INVITE dan SDP

```bash
$ tcpdump -nn -r korban.pcap 'udp port 5060' -A
```

Potongan penting:

```text
INVITE sip:231@pbx.cakrawala.internal SIP/2.0
From: <sip:204@pbx.cakrawala.internal>;tag=a204
To: <sip:231@pbx.cakrawala.internal>
Call-ID: c1a84d0e-204@pbx.cakrawala.internal
Content-Type: application/sdp
Content-Length: 138

v=0
o=- 204 1 IN IP4 10.24.8.31
s=Desk phone 204
c=IN IP4 10.24.8.31
m=audio 4000 RTP/AVP 0
a=rtpmap:0 PCMU/8000
a=sendrecv
```

`200 OK` dari Dina:

```text
SIP/2.0 200 OK
From: <sip:204@pbx.cakrawala.internal>;tag=a204
To: <sip:231@pbx.cakrawala.internal>;tag=b231
Call-ID: c1a84d0e-204@pbx.cakrawala.internal

v=0
o=- 204 1 IN IP4 10.24.8.24
s=Desk phone 231
c=IN IP4 10.24.8.24
m=audio 4002 RTP/AVP 0
a=rtpmap:0 PCMU/8000
```

Kesimpulan:

| Arah | Endpoint | Ext | RTP |
|---|---|---|---|
| Raka → Dina | `10.24.8.31:4000` → `10.24.8.24:4002` | 204 | PCMU/8000, SDP `a=sendrecv` |
| Dina → Raka | `10.24.8.24:4002` → `10.24.8.31:4000` | 231 | PCMU/8000 |

### 2.2 Ekstraksi RTP

RTP header 12 byte, payload 160 byte (20 ms @ 8 kHz), total UDP payload 172 byte. Ekstraksi dilakukan per `(sport,dport,ssrc)`, urut sequence, lalu payload μ-law di-decode.

```python
import struct, wave, audioop

d = open('korban.pcap','rb').read()
o = 24
streams = {}
while o + 16 <= len(d):
    ts, tu, incl, orig = struct.unpack('<IIII', d[o:o+16]); o += 16
    p = d[o:o+incl]; o += incl
    ip = p[14:]
    if len(ip) < 20 or ip[0] >> 4 != 4 or ip[9] != 17:
        continue
    ihl = (ip[0] & 0xF) * 4
    udp = ip[ihl:]
    sport, dport, ulen, csum = struct.unpack('>HHHH', udp[:8])
    pay = udp[8:]
    if not (4000 <= sport <= 4002 or 4000 <= dport <= 4002) or len(pay) < 12:
        continue
    b0 = pay[0]; cc = b0 & 0xF
    seq = struct.unpack('>H', pay[2:4])[0]
    ssrc = struct.unpack('>I', pay[8:12])[0]
    off = 12 + 4 * cc
    streams.setdefault((sport, dport, ssrc), []).append((seq, pay[off:]))

for (sp, dp, ssrc), pkts in streams.items():
    pkts.sort()
    raw = b''.join(x[1] for x in pkts)
    pcm = audioop.ulaw2lin(raw, 2)
    w = wave.open(f'pt_{sp}_{dp}_{ssrc:08x}.wav', 'wb')
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000)
    w.writeframes(pcm); w.close()
    print(sp, dp, len(pkts), len(raw)/8000, 'detik')
```

Output:

```text
4000->4002 ssrc=a2040001 pkts=1051 seq=3800..4850 payload=168160 durasi=21.02s
4002->4000 ssrc=b2310001 pkts=2374 seq=3800..6173 payload=379840 durasi=47.48s
```

Artefak audio:

- `assets/panggilan-terakhir/01-Raka-204.wav` (21,02 detik)
- `assets/panggilan-terakhir/02-Dina-231.wav` (47,48 detik)
- Spectrogram: `03-spectrogram-Dina.png`, `04-spectrogram-Raka.png`

### 2.3 Transkripsi

Audio di-upsample ke 16 kHz, lalu ditranskripsi dengan faster-whisper (`tiny`, `language=id`, `vad_filter=True`). Output mentah Dina (stream 4002 → 4000):

```text
[0.00-5.00] Gal, selinanya kamu tinggal di printer, terakhir.
[5.00-8.00] Kodanya masih kelihatan.
[8.00-13.00] NSXGTS, kurung kurawa buka,
[13.00-16.00] Garis bawah, merah, Garis bawah,
[16.00-19.00] 2.4 kurung kurawa tutu.
[19.00-22.00] Kalau besok pagi kamu nggak jelasin,
[22.00-25.00] aku kirim semuanya kekepalah kantor.
[25.00-29.00] Gal, aku udah simpan selinanya.
[30.00-33.00] Kamu kira aku bakal diam aja?
[33.00-36.00] Raka, jangan gila.
[36.00-39.00] Kita bisa ngomong baik baik.
[39.00-42.00] Halo, Raka?
[42.00-44.00] Kamu di depan pintu?
[44.00-47.00] Raka, jangan.
```

Raka (stream 4000 → 4002):

```text
[0.00-3.00] Din, kamu tahu kondidokumen itu dari mana?
[3.00-5.00] Aku simpan sendiri dilachi.
[5.00-7.00] Kamu bukalachi aku?
[7.00-10.00] Dinah, jangan main main.
[10.00-12.00] Hapu salinan itu sekarang.
[12.00-14.00] Dengarin aku.
[14.00-17.00] Kalau kamu bocorinko di itu, aku bunuh kamu.
[17.00-20.00] Aku keruang garsip sekarang.
```

Koreksi berdasarkan konteks dan flag:

| ASR | Koreksi |
|---|---|
| `NSXGTS` | `NFXCTF` (N-F-X-C-T-F) |
| `2.4` | `204` |
| `kurung kurawa buka/tutu` | `{` / `}` |
| `garis bawah` | `_` |
| `merah` | `MERAH` |

Rangkaian yang diucapkan Dina:

```text
NFXCTF { ARSIP _ MERAH _ 204 }
```
