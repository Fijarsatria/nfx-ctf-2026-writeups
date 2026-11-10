# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh — Analisis

[← Overview](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh.md) · [Index](index.md)

> **Langkah 2/7 — Analisis.** Data cocok dengan LWE public key / transkrip satu sisi:
>
> **Titik penting:** Data cocok dengan LWE public key / transkrip satu sisi:
>
> **Berikutnya:** [Solver](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-03-solver.md)

### 2.1 Bentuk matematis

Data cocok dengan LWE *public key* / transkrip satu sisi:

```text
A ∈ Z_q^{m×n}      (64×40)
s ∈ Z_q^n          (40, small secret)
e ∈ Z_q^m          (64, small error)
b = A·s + e  (mod q),  q = 257
```

Parameter yang membuat ini lemah:

- `q = 257` sangat kecil (8 bit + 1).
- `n = 40` jauh di bawah parameter produksi (Kyber memakai `n=256`, `q=3329`,
  module rank sampai 4).
- Secret dan error berada di rentang yang sangat sempit. Dari hasil lattice:
  `s_i ∈ {-1,0,1}` dan `e_i ∈ [-2,2]`.

Dengan `m=64 > n=40`, ada 24 persamaan redundan; itu yang memberi sinyal
cukup bagi lattice untuk memilih vektor pendek yang benar.

### 2.2 Mengapa lattice bisa menang

Persamaan `b = A·s + e mod q` dapat ditulis:

```text
A·s + q·z + e = b
```

dengan `z ∈ Z^m` adalah vektor pembulatan modular. Jika `s` dan `e` kecil,
maka vektor

```text
(e, s, 1)  atau  (-e, s, -1)
```

adalah vektor pendek di dalam lattice yang dibangun dari `A`, `b`, dan `q`.
Ini adalah **Kannan embedding** untuk CVP/uSVP.

### 2.3 Konstruksi lattice yang dipakai

Basis berdimensi `d = m + n + 1 = 105`:

```text
[ q·I_m      0      0 ]   <- m baris
[ A^T        I_n    0 ]   <- n baris
[ b^T        0      1 ]   <- 1 baris penanda (Kannan)
```

Kombinasi integer dengan koefisien terakhir `-1` menghasilkan:

```text
( q·z + A·s - b ,  s ,  -1 )  =  ( -e , s , -1 )
```

yang normanya kecil karena `e` dan `s` kecil. Setelah LLL + BKZ block size 20,
baris dengan koordinat terakhir `±1` dan secret ternary langsung muncul.

### 2.4 Verifikasi relasi

Untuk setiap kandidat `s`, error dihitung ulang dari definisi:

```text
e_i = (b_i - (A·s)_i) mod 257,  lalu dipusatkan ke [-128,128]
```

Hasil nyata: `max|s| = 1`, `max|e| = 2`, dan 64/64 baris memenuhi
`A·s + e ≡ b (mod 257)`.
