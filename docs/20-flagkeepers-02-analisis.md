# FlagKeepers — Analisis

[← Overview](20-flagkeepers.md) · [Index](index.md)

> **Langkah 2/8 — Analisis.** Untuk nonce 12 byte:
>
> **Titik penting:** Untuk nonce 12 byte:
>
> **Berikutnya:** [Helper GF(2^128) / GHASH](20-flagkeepers-03-helper-gf-2-128-ghash.md)

### 2.1 GCM dalam satu paragraf

Untuk nonce 12 byte:

```text
J0 = nonce || 0x00000001
CT = PT XOR AES_K(J0), AES_K(J0+1), ...
Tag = GHASH_H(AAD, CT) XOR AES_K(J0)
H = AES_K(0^128)
```

`GHASH` memperlakukan ciphertext sebagai polinomial di GF(2^128):

```text
Y_0 = 0
Y_i = (Y_{i-1} XOR C_i) · H
...
Y_n = Σ C_i · H^{n-i+1}
Tag = (Y_n XOR L) · H XOR E_K(J0)
    = Σ C_i · H^{n-i+2} XOR L·H XOR E_K(J0)
```

dengan `L = (len(AAD)·8 || len(CT)·8)`.

### 2.2 Keystream recovery

Pesan RECOVERY selalu 51 byte:

```text
RECOVERY|ts=...|r=xxxxxxxx|t=xxxxxxxxxxxx|OK
```

Service mencetak plaintext-nya (`Log [...]`) dan ciphertext (`CT: ...`).
Karena panjang dan nonce sama, keystream CTR untuk `key_b` identik di semua
sampel:

```text
KS = CT XOR PT     (51 byte)
```

Dengan `KS`, kita bisa membuat ciphertext untuk plaintext apa pun yang
panjangnya 51 byte.

### 2.3 Recover H dari selisih tag

Ambil dua sampel dengan panjang sama. Karena `L` sama dan `E_K(J0)` sama:

```text
tag1 XOR tag2 = Σ (C1_i XOR C2_i) · H^{n-i+2}
```

Untuk 51 byte, `n = 4` blok (blok terakhir di-zero-pad), sehingga hanya ada
monomial `H², H³, H⁴, H⁵`. Dengan cukup banyak pasangan sampel, ini menjadi
sistem linear di GF(2^128) dengan 4 variabel. Solusi yang konsisten memberi
`H`.

Di run live, `H` yang diperoleh:

```text
H_b = 0x26493fa6231e531baf7ba6bf77c84b50
```

### 2.4 Recover E_K(J0) dan forge

Setelah `H` diketahui:

```text
E_K(J0) = tag XOR GHASH(H, CT)
```

Nilai ini harus sama untuk semua sampel (konsistensi check). Lalu untuk
plaintext pilihan:

```text
CT_forge  = P XOR KS
TAG_forge = GHASH(H, CT_forge) XOR E_K(J0)
```

Pilih:

```text
P = b"admin = True" + b" " * 39      # 51 byte
```

Tidak ada `admin = False`, dan `admin = True` ada di 12 byte pertama.

### 2.5 Syarat `idx`

`idx` mulai 0. Setiap opsi `[2]` mengurangi 16:

```text
idx = (0 - 14·16) mod 256 = 32
```

Karena `msg[:32]` sudah mencakup 12 byte pertama, kondisi
`b"admin = True" in msg[:idx]` benar. Jadi cukup 14 kali opsi `[2]`.
