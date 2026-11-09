# Broken Signature Scheme — Analisis

[← Overview](18-broken-signature-scheme.md) · [Index](index.md)

### 2.1 Layer 1 — RSA signature multiplicatif

Skema menandatangani pesan mentah:

```text
sig(m) = m^d mod N
```

Karena fungsi RSA homomorfik multiplikatif:

```text
sig(m1) · sig(m2) ≡ (m1·m2)^d ≡ sig(m1·m2)  (mod N)
```

Target:

```text
target = 0x676976652d6d652d7468652d666c6167 = b"give-me-the-flag"
```

Enam pesan yang ditandatangani (sebagai integer hex):

```text
m0 = 0x51
m1 = 0x11b
m2 = 0x127a6a3b60a4ff3d22bfbb9863b15
m3 = 0xc161f7b3fe326517
m4 = 0xe2931d8da4fca785
m5 = 0xb1d824c70d64b4d9
```

Ternyata:

```text
m0 · m1 · m2 = 0x676976652d6d652d7468652d666c6167 = target
```

Jadi signature target dapat dipalsukan tanpa private key:

```text
sig_forge = (sig0 · sig1 · sig2) mod N
```

Verifikasi: `sig_forge^e mod N == target`. Ini lolos karena tidak ada hashing
dan tidak ada padding pada pesan.

### 2.2 Layer 2 — close-prime RSA

Diketahui:

```text
q = nextprime(p + 2^300)
δ = q - p = 2^300 + g,   g kecil (selisih ke prima berikutnya)
N = p·q = p·(p+δ)
```

Maka:

```text
(p+q)² = (2p+δ)² = δ² + 4p(p+δ) = δ² + 4N
```

Karena `p+q` integer, `δ² + 4N` harus kuadrat sempurna. Strategi:

1. Untuk `g = 0,1,2,...,199999`, hitung `δ = 2^300 + g`.
2. Hitung `D = δ² + 4N`, `s = isqrt(D)`.
3. Jika `s² == D` dan `(s-δ)` genap, kandidat `p = (s-δ)/2`.
4. Cek `p·(p+δ) == N`.
5. Cek 20 bit bocor: `((p >> 500) & (2^20 - 1)) == 0x69252`.

Nilai yang ditemukan (1024-bit):

```text
p = 90291662713827565480510099980052169978757026472994257635201524524901623059176183784023029214624806237433417327527438388766528120528496054964793640966468959559313814603396865910254942140069944258287881295705125931644869356506093912310980430646149995999468750875007630831106806462679175171959178546366955626109
q = 90291662713827565480510099980052169978757026472994257635201524524901623059176183784023029214624806237433417327527438388766528120528496054964793640966468959559313814603396865910254942140069944258287881295705125931644871393542070246797066699091838405377629802343401296767357442603128529553258941883073139025589
```

Selisih:

```text
q - p = 2037035976334486086268445688409378161051468393665936250636140449354381299763336706183399480
      ≈ 2^300.00...
```

`N` adalah 2047 bit; `p` dan `q` masing-masing 1024 bit.

### 2.3 Layer 3 — AES-GCM

`flag_cipher` berisi `nonce`, `ct`, `tag`. Key diturunkan dari faktor:

```text
key = SHA256( p_bytes || q_bytes )     # big-endian, panjang minimal
```

Karena `p,q` 1024-bit, masing-masing 128 byte. Tag diverifikasi oleh
`decrypt_and_verify`, sehingga keberhasilan dekripsi sekaligus membuktikan
`p` dan `q` benar.
