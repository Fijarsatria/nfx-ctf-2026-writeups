# Twin Prime Lattice — Jejak awal

[← Overview](75-twin-prime-lattice.md) · [Index](index.md)

> **Langkah 1/5.** `output.txt` berisi `N`, `e`, `c`. Dua faktor RSA-nya berdekatan.
>
> **Berikutnya:** [Cara Mendapatkan Flag](75-twin-prime-lattice-02-cara-mendapatkan-flag.md)

```bash
grep -E '^(e|bits|leak_bits) ' output.txt
```

`e = 65537`, modulus 2048-bit, dan ada leak 32 bit. Karena kedua prima hampir sama, `isqrt(N)` sudah cukup dekat. Leak itu hanya konfirmasi, bukan syarat Fermat.
