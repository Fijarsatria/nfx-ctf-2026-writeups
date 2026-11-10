# Feistel Differential — Strategi

[← Overview](04-feistel-differential.md) · [Index](index.md)

> **Langkah 4/9 — Strategi.** Strategi
>
> **Titik penting:** —
>
> **Berikutnya:** [Script lengkap](04-feistel-differential-05-script-lengkap.md)

## 3.1 Strategi

1. Parse `pairs.txt` menjadi 14 blok `(Δ, [(p,c1,c2), ...])`.
2. Bangun model z3: 7 BitVec 16-bit, SBOX sebagai chain `If`, `permute`
   sebagai konkatenasi extract.
3. Tambahkan constraint untuk 7 pasangan pertama blok Δ=0xa.
4. Ambil model, hitung master key, verifikasi pada seluruh 280.000 baris.
5. Dekripsi `flag.enc` per blok 4-byte big-endian, lalu buang padding PKCS#7.

### Evidence langkah ini

![term-solver-output.png](assets/feistel-differential/term-solver-output.png)

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`solver-output.txt`](assets/feistel-differential/solver-output.txt)
