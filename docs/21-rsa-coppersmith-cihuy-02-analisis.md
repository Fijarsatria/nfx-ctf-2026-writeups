# RSA Coppersmith cihuy — Analisis

[← Overview](21-rsa-coppersmith-cihuy.md) · [Index](index.md)

> **Langkah 2/7 — Analisis.** Faktor p dapat ditulis:
>
> **Titik penting:** Faktor p dapat ditulis:
>
> **Berikutnya:** [Script lengkap](21-rsa-coppersmith-cihuy-03-script-lengkap.md)

### 2.1 Persamaan partial key exposure

Faktor `p` dapat ditulis:

```text
p = a + x,   a = p_msb · 2^212,   0 ≤ x < 2^212
```

Karena `p | N`, maka `x` adalah akar kecil dari polinomial:

```text
f(x) = a + x ≡ 0 (mod p)
```

`p` tidak diketahui, tetapi `p ≥ N^0.25 ≈ 2^256` dan `|x| < 2^212 < N^0.25`.
Ini tepat berada di wilayah **Coppersmith small-root** untuk modulus yang
tidak diketahui faktornya.

### 2.2 Batas teori

Coppersmith univariate dapat menemukan akar `|x| < N^{1/d}` untuk polinomial
derajat `d`. Di sini `d=1`, sehingga batasnya `N^{1/1}` secara teori terlalu
longgar; yang dipakai adalah varian Howgrave-Graham dengan `f(x) ≡ 0 mod p`
dan `p ≥ N^β`, `β ≈ 0.5`. Batas praktisnya `|x| < N^{β²} = N^{0.25}`.
Karena `2^212 < 2^256`, kondisi terpenuhi dengan margin besar.

### 2.3 Lattice Howgrave-Graham

Untuk parameter `m` (dan `t=m`), basis polinomial:

```text
g_{i}(x) = N^{m-i} · f(x)^i,          i = 0..m-1
g_{m+j}(x) = x^j · f(x)^m,            j = 0..t-1
```

Setiap polinomial dievaluasi pada `x = X·y` dengan `X = 2^213`, lalu
koefisiennya menjadi baris matriks. LLL mencari kombinasi integer dengan
norma kecil; polinomial hasil reduksi memiliki akar yang sama dengan `f`
mod `p`, dan akarnya dapat dicari dengan `sympy` (`ground_roots`/`nroots`).

Parameter yang berhasil: `m = 4`, dimensi 8. (Percobaan `m=2,3` juga
diperiksa; `m=4` yang menemukan akar.)

### 2.4 Setelah `p` ditemukan

```text
q = N / p
d = e^{-1} mod (p-1)(q-1)
m = c^d mod N
```

Plaintext RSA di sini sengaja di-zero-pad di kiri sampai 128 byte, jadi flag
muncul setelah `lstrip(b"\x00")`.
