# Broken Signature Scheme — Analisis

[← Overview](18-broken-signature-scheme.md) · [Index](index.md)

> **Langkah 3/8 — Analisis.** Karena p+q integer, δ² + 4N harus kuadrat sempurna.
>
> **Titik penting:** Karena p+q integer, δ² + 4N harus kuadrat sempurna.
>
> **Berikutnya:** [Solver](18-broken-signature-scheme-04-solver.md)

## 2.2 Layer 2 — close-prime RSA

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

## 2.3 Layer 3 — AES-GCM

`flag_cipher` berisi `nonce`, `ct`, `tag`. Key diturunkan dari faktor:

```text
key = SHA256( p_bytes || q_bytes )     # big-endian, panjang minimal
```

Karena `p,q` 1024-bit, masing-masing 128 byte. Tag diverifikasi oleh
`decrypt_and_verify`, sehingga keberhasilan dekripsi sekaligus membuktikan
`p` dan `q` benar.
