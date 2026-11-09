# The Alchemist's Sandbox — Analisis

[← Overview](32-the-alchemists-sandbox.md) · [Index](index.md)

## 2.4 Bentuk payload

Payload adalah sebuah **tuple** berisi assignment-assignment dan ekspresi
terakhir. `[-a]` = `[-1]` mengambil elemen terakhir tuple, yaitu hasil
`getattr(...)[...]`.

```text
((a:=True),(b:=a<<a),...,(u:=chr(k-a)),
 getattr(als, <"__globals__">)[<"_VAULT_STATE">])[-a]
```

Hasilnya adalah list `_VAULT_STATE`:

```text
[29406, 62193, 3550, 51604, 54474, 58556, 5807, 62536, 3004, 10962,
 33499, 52037, 51010, 45605, 6009, 18571, 21884, 35367, 29761, 57118,
 51549]
```

## 2.5 Skema enkripsi

Plaintext 42 byte di-*pack* big-endian menjadi 21 word 16-bit:

```python
w = list(struct.unpack(">21H", flag_bytes))
```

Untuk setiap ronde `r = 0..31`:

```text
rc = (r * 0x9E37 + 0x7F4A) & 0xFFFF
mix(i) = rol16((w[i-1] * 257 + rc + i*17) & 0xFFFF, (r+i) % 15 + 1)
w[i]   = rol16((w[i] XOR mix(i)) + rc, 5)
w      = [w[(i*4) % 21] for i in range(21)]
```

Dua operasi yang perlu dibalik:

1. **Permutasi** `new[i] = old[(4*i) % 21]`. Inversnya:
   `previous[(4*i) % 21] = new[i]`.
2. **Transformasi per word**:
   - maju: `t = w[i] XOR mix`; `w[i] = rol16((t + rc) & 0xFFFF, 5)`
   - balik: `t = ror16(w[i], 5) - rc`; `w[i] = t XOR mix`

Kunci pembalikan: proses `i` dari **20 turun ke 0**, karena `mix(i)`
bergantung pada `w[i-1]` yang harus sudah dikembalikan ke nilai sebelumnya.
Untuk `i=0`, `w[20]` sudah diproses lebih dulu.
