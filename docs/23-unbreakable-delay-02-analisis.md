# Unbreakable Delay — Analisis

[← Overview](23-unbreakable-delay.md) · [Index](index.md)

> **Langkah 2/8 — Analisis.** Verifiable Delay Function memungkinkan pihak lain memverifikasi bahwa suatu fungsi dievaluasi selama T langkah berurutan yang tidak dapat diparalelkan.
>
> **Titik penting:** Verifiable Delay Function memungkinkan pihak lain memverifikasi bahwa suatu fungsi dievaluasi selama T langkah berurutan yang tidak dapat diparalelkan.
>
> **Berikutnya:** [Analisis](23-unbreakable-delay-03-analisis-2.md)

## 2.1 Apa itu VDF

Verifiable Delay Function memungkinkan pihak lain memverifikasi bahwa suatu
fungsi dievaluasi selama `T` langkah **berurutan** yang tidak dapat
diparalelkan. Konstruksi klasik (Wesolowski / Pietrzak):

```text
Input : N (RSA modulus), x, T
Output: y = x^(2^T) mod N
```

Untuk `x=2`, `T=2^256`:

```text
y = 2^(2^256) mod N
```

Evaluasi naif membutuhkan `T` squaring:

```text
x_0 = x
x_{i+1} = x_i^2 mod N
y = x_T
```

Jumlah langkahnya `2^256` — jauh melampaui usia alam semesta.

## 2.2 Fiat–Shamir proof

Agar verifier tidak perlu mengulang `T` langkah, prover mengirim `y` dan
bukti `π`. Varian Wesolowski:

```text
l  = H(N, x, y)             # challenge prime (Fiat-Shamir)
π  = x^(⌊2^T / l⌋) mod N
verifikasi: π^l · x^(2^T mod l) ≡ y (mod N)
```

Verifikasi hanya butuh satu eksponensial `π^l` dan satu eksponensial kecil
`x^(T mod l)`, jadi cepat. Keamanannya bergantung pada asumsi bahwa prover
**tidak tahu φ(N)** dan tidak dapat memfaktorkan `N`.

## 2.3 Bug: `N` dapat difaktorkan karena relasi XOR

**[REKONSTRUKSI]** Nama challenge dan flag menunjukkan modulus dibangkitkan
dengan relasi XOR yang lemah antara `p` dan `q`, misalnya:

```text
q = p XOR K        # K kecil / hanya beberapa bit
```

atau

```text
p XOR q = 2^k      # satu bit berbeda
```

Jika `p XOR q = 2^k`, maka `|p-q| = 2^k` (karena hanya bit ke-`k` yang
berbeda). Faktorisasi menjadi persamaan kuadrat:

```text
N = p(p ± 2^k)
(p+q)^2 = 2^(2k) + 4N
```

Cukup cek apakah diskriminan kuadrat sempurna, lalu:

```text
p = (-δ + sqrt(δ² + 4N)) / 2,   δ = ±2^k
```

Jika `K` lebih besar tetapi hanya mengenai beberapa bit rendah, `q` tetap
dekat dengan `p`; kandidat `δ` dapat dienumerasi, atau diserang dengan
Fermat/Coppersmith. Intinya: **relasi XOR menghapus entropi faktorisasi**.

### Evidence langkah ini

![00-challenge-platform.png](assets/unbreakable-delay/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*
