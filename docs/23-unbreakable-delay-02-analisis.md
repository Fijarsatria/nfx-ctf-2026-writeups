# Unbreakable Delay — Analisis

[← Overview](23-unbreakable-delay.md) · [Index](index.md)

### 2.1 Apa itu VDF

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

### 2.2 Fiat–Shamir proof

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

### 2.3 Bug: `N` dapat difaktorkan karena relasi XOR

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

### 2.4 Bug: `φ(N)` membunuh delay

Setelah `p,q` diketahui:

```text
φ(N) = (p-1)(q-1)
```

Karena `gcd(2,N)=1`, eksponen raksasa dapat direduksi:

```text
2^T mod N = 2^(T mod φ(N)) mod N
```

Jadi `y` dapat dihitung tanpa `T` squaring:

```text
e = pow(2, 256, φ(N))       # 2^256 mod φ(N)
y = pow(2, e, N)
```

Proof juga dapat dihitung cepat:

```text
π = pow(2, (T // l) mod φ(N), N)
```

Verifikasi tetap lolos karena semua eksponen bekerja modulo `φ(N)`.

### 2.5 Mengapa ini "fast VDF bypass"

VDF mengasumsikan prover tidak tahu orde grup. Begitu `φ(N)` diketahui,
seluruh "delay" hilang: baik evaluasi `y` maupun pembuatan `π` menjadi
beberapa eksponensial modular biasa. Ini bukan sekadar speedup — ini
menghancurkan properti **sequentiality** yang menjadi definisi VDF.
