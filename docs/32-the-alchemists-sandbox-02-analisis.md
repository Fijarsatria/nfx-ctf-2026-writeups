# The Alchemist's Sandbox — Analisis

[← Overview](32-the-alchemists-sandbox.md) · [Index](index.md)

### 2.1 Filter AST

Filter memiliki beberapa lapis:

1. **Karakter:** angka `0-9` dan kutip `"`/`'` tidak boleh muncul di string
   ekspresi.
2. **Panjang:** maksimal 1024 karakter.
3. **Node terlarang:** import, lambda, comprehension, f-string.
4. **Atribut privat:** node `ast.Attribute` dengan `attr.startswith("_")`
   ditolak.
5. **Call:** maksimal 2 argumen posisional, tanpa keyword.

Yang tersedia di environment: `getattr`, `chr`, dan `als`
(`_encrypt_vault`).

### 2.2 Celah: `getattr` + nama dinamis

Akses langsung `als.__globals__` ditolak karena `ast.Attribute` dengan
`attr="_..."`. Tetapi:

```python
getattr(als, "__globals__")
```

tidak memakai node `ast.Attribute` sama sekali. Yang perlu dilakukan
hanyalah membangun string `__globals__` tanpa menulis huruf/angka/kutip.

### 2.3 Membangun angka dan karakter

`True` adalah boolean, bukan literal angka, dan nilainya 1. Dengan assignment
expression `:=` dan bit shift:

```python
a = True          # 1
b = a << a        # 2
d = b << a        # 4
e = d << a        # 8
f = e << a        # 16
h = f << a        # 32
j = h << a        # 64
k = j + h         # 96
u = chr(k - a)    # chr(95) = '_'
```

Dari situ:

```text
chr(k+a+b+d)          = chr(103) = 'g'
chr(k+d+e)            = chr(108) = 'l'
chr(k+a+b+d+e)        = chr(111) = 'o'
chr(k+b)              = chr(98)  = 'b'
chr(k+a)              = chr(97)  = 'a'
chr(k+d+e)            = chr(108) = 'l'
chr(k+a+b+f)          = chr(115) = 's'
u + u                 = '__'
```

Sehingga `u+u+...+u+u` = `__globals__`.

Dengan pola yang sama, key `_VAULT_STATE` dibangun:

```text
'_' 'V' 'A' 'U' 'L' 'T' '_' 'S' 'T' 'A' 'T' 'E'
```

### 2.4 Bentuk payload

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

### 2.5 Skema enkripsi

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
