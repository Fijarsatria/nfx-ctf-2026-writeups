# Dokodemo Door — Analisis

[← Overview](28-dokodemo-door.md) · [Index](index.md)

## 2.1 Sifat repeating-key XOR

Untuk ciphertext `C[i]` dan key `K` dengan panjang `L`:

```text
P[i] = C[i] XOR K[i mod L]
```

Jika panjang key diketahui, key bisa dihitung dari **known plaintext**.
PDF memiliki struktur yang sangat dapat ditebak:

- Header: `%PDF-1.4\n`
- Trailer: `%%EOF\n`

## 2.2 Menemukan panjang key dan key

Crib header memberi 9 byte pertama key. Crib trailer memberi 6 byte terakhir
key. Untuk setiap kandidat panjang key `L = 1..64`, kedua crib harus
konsisten pada posisi yang sama:

```text
header  : K[0..8]  = C[0..8]  XOR "%PDF-1.4\n"
trailer : K[(n-6)..(n-1)] = C[n-6..n-1] XOR "%%EOF\n"
```

Pada `L = 16`, tidak ada konflik dan hanya tersisa satu posisi key yang belum
diketahui (posisi 9). Posisi itu di-brute-force 0..255 dan dipilih berdasarkan
skor PDF (keberadaan `%PDF`, `%%EOF`, ` obj`, `endobj`, `stream`, `/Type`,
`xref`, `trailer`, serta rasio byte printable).

Hasil:

```text
ciphertext bytes      : 8672
candidate key length  : 16
recovered key         : b'nfx_k3tuk_p1ntu!'
crib-unknown positions: [9] filled with (95,)
decrypted header      : b'%PDF-1.4\n%\x93\x8c\x8b\x9e Repor'
decrypted trailer     : b'>>\nstartxref\n8239\n%%EOF\n'
score                 : 1213
```

Byte 95 adalah `_`, sehingga key lengkapnya:

```text
n f x _ k 3 t u k _ p 1 n t u !
```

atau `nfx_k3tuk_p1ntu!` — sesuai tema challenge ("ketuk pintu").

## 2.3 Verifikasi hasil dekripsi

```bash
$ python3 solve_dokodemo.py
...
written               : /tmp/opencode/dokodemo_decrypted.pdf

$ file /tmp/opencode/dokodemo_decrypted.pdf
PDF document, version 1.4, 1 page(s)

$ sha256sum rahasia.pdf /tmp/opencode/dokodemo_decrypted.pdf
44f43727b3de339f94ded1e67ef9cc6620e4d88f8fa707b4a738c35eba4a6df2  rahasia.pdf
6039511dcd291ae1cf2da15be996b9086aaaefad125364893df52f057e8207fb  /tmp/opencode/dokodemo_decrypted.pdf
```

### Evidence langkah ini

![term-02-extracted-text.png](assets/dokodemo-door/term-02-extracted-text.png)

*Terminal evidence — `02-extracted-text.txt` (arsip transkrip sesi solve).*
