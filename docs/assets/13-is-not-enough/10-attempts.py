"""13 Is Not Enough — percobaan transformasi (tidak ada yang cocok)."""
import codecs, itertools, math, random, string
ct = r'p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L'
pt = 'NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}'

def rot13(s): return codecs.encode(s, 'rot13')
def rot5(s): return ''.join(str((int(c)+5) % 10) if c.isdigit() else c for c in s)
def rot47(s): return ''.join(chr(33+(ord(c)-33+47) % 94) if 33 <= ord(c) <= 126 else c for c in s)
def atbash(s):
    tr = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                       'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba')
    return s.translate(tr)

base = {'id': lambda s: s, 'r13': rot13, 'r5': rot5,
        'r135': lambda s: rot5(rot13(s)), 'r513': lambda s: rot13(rot5(s)),
        'r47': rot47, 'atb': atbash, 'rev': lambda s: s[::-1]}

# cek semua komposisi sampai 4
for L in range(1, 5):
    for names in itertools.product(base, repeat=L):
        s = ct
        for n in names: s = base[n](s)
        if s == pt:
            print('FOUND', names); raise SystemExit
print('tidak ada komposisi ROT/atbash/reverse sampai 4 langkah')

# affine printable ASCII
for a in range(1, 95):
    if math.gcd(a, 95) != 1: continue
    for b in range(95):
        out = ''.join(chr(32+((a*(ord(c)-32)+b) % 95)) if 32 <= ord(c) <= 126 else c for c in ct)
        if out == pt: print('AFFINE', a, b)

# XOR/add dengan key umum
for k in ['13', 'thirteen', 'rot13', 'rot5', 'notenough', 'digits', 'letters', 'NFX', '1337', 'fix', 'key']:
    x = ''.join(chr(ord(c) ^ ord(k[i % len(k)])) for i, c in enumerate(ct))
    if x == pt: print('XOR', k)
    v = ''.join(chr(32+((ord(c)-32+(ord(k[i % len(k)])-32)) % 95)) for i, c in enumerate(ct))
    if v == pt: print('ADD95', k)

# PRNG seed 13
for seed in [13, '13', 1337, 'thirteen']:
    r = random.Random(seed)
    stream = bytes(r.randrange(256) for _ in range(len(ct)))
    x = bytes(a ^ b for a, b in zip(ct.encode(), stream)).decode('latin1')
    if x == pt: print('PRNG XOR', seed)

print('selesai: tidak ada transformasi yang cocok')
