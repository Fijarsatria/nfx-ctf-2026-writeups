# Twin Prime Lattice — Cara mendapatkan flag

[← Overview](75-twin-prime-lattice.md) · [Index](index.md)

> **Langkah 2/5.** Fermat: `a = isqrt(N)+1`, `b = isqrt(a*a-N)`, lalu `p=a-b` dan `q=a+b`.
>
> **Berikutnya:** [Flag](75-twin-prime-lattice-03-flag.md)

```python
from math import isqrt
from Crypto.Util.number import long_to_bytes, inverse

text = open("output.txt").read()
N = int(text.split("N = ", 1)[1].split()[0])
c = int(text.split("c = ", 1)[1].split()[0])
e = 65537
a = isqrt(N) + 1
b = isqrt(a * a - N)
p, q = a - b, a + b
assert p * q == N
d = inverse(e, (p - 1) * (q - 1))
print(long_to_bytes(pow(c, d, N)).decode())
```

```text
NXCTF{tw1n_pr1m3s_m33t_l4tt1c3_c0pp3r5m1th_af6854ba29a3}
```

Skrip ini dijalankan ulang terhadap `output.txt` asli. Judul menyebut lattice, tetapi faktor yang berdekatan selesai dengan Fermat. Prefix flag adalah `NXCTF`.
