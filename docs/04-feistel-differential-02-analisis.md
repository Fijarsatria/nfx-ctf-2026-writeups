# Feistel Differential — Analisis

[← Overview](04-feistel-differential.md) · [Index](index.md)

### 2.1 Cipher

`cipher.py`:

```python
ROUNDS = 7
MASK16 = 0xFFFF
SBOX = [1,8,14,12,2,0,3,4,11,9,15,13,6,10,7,5]

def permute(m):
    n0 = m & 0xF
    n1 = (m >> 4) & 0xF
    n2 = (m >> 8) & 0xF
    n3 = (m >> 12) & 0xF
    return n1 | (n0 << 4) | (n3 << 8) | (n2 << 12)

def round_f(x, k):
    y = x ^ k
    m = (SBOX[y & 0xF]
         | (SBOX[(y >> 4) & 0xF] << 4)
         | (SBOX[(y >> 8) & 0xF] << 8)
         | (SBOX[(y >> 12) & 0xF] << 12))
    return permute(m)

def key_schedule(master):
    return [(master >> (16 * i)) & MASK16 for i in range(ROUNDS)]

def encrypt_block(block, subkeys):
    L = (block >> 16) & MASK16
    R = block & MASK16
    for k in subkeys:
        L, R = R, L ^ round_f(R, k)
    return (L << 16) | R
```

Karakteristik:

- Blok 32-bit, dua half 16-bit.
- 7 ronde → 7 subkey 16-bit = **112 bit master key**.
- `F` bekerja per nibble: XOR subkey → 4×SBOX → swap nibble pairs.
- Feistel invertible; dekripsi memakai `F` yang sama dengan urutan subkey
  terbalik.

### 2.2 Struktur `pairs.txt`

File berisi 14 blok, masing-masing 20.000 baris, dengan header:

```text
# input difference: 0000000a
# input difference: 00000005
# input difference: 000000a0
# input difference: 00000050
...
# input difference: 0000550000
```

Setiap baris:

```text
p  c1  c2    ->   c1 = E(p),  c2 = E(p XOR Δ)
```

Jadi ada 280.000 known plaintext/ciphertext pairs (dua per baris) di bawah
**satu master key**.

### 2.3 Mengapa 7 pasangan cukup

Total unknown = 7 × 16 = 112 bit. Satu pasangan `(p, c1)` memberi 32 bit
output, dan pasangan keduanya memberi 32 bit tambahan. Secara informasi,
6 pasangan (384 bit observasi) seharusnya sudah lebih dari cukup, tetapi
**tidak semua bit key teramati** karena struktur Feistel: beberapa subkey
hanya memengaruhi output melalui kombinasi tertentu, sehingga model z3 masih
punya beberapa solusi yang cocok pada 6 pasangan.

Hasil empiris:

| Jumlah pasangan | Status z3 | Kecocokan pada blok 0 |
|---:|---|---:|
| 6 | SAT | 11.183 / 20.000 |
| 7 | SAT | 20.000 / 20.000 |

Dengan 7 pasangan, model terpaku ke key yang benar. Ini juga menunjukkan
bahwa "differential" di data sebenarnya tidak wajib dieksploitasi secara
statistik: known-plaintext saja sudah cukup karena key space-nya kecil.

### 2.4 Differential sebagai validasi tambahan

Walaupun solver memakai known-plaintext, struktur diferensial berguna untuk
verifikasi: untuk setiap Δ, ciphertext difference `c1 XOR c2` harus konsisten
dengan key. Solver akhir mengecek **kedua** ciphertext pada semua 280.000
baris, bukan hanya 7 baris yang dipakai menyelesaikan model.
