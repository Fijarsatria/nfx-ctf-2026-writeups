# Feistel Differential — Recon

[← Overview](04-feistel-differential.md) · [Index](index.md)

> **Langkah 1/9 — Recon.** flag.enc adalah 104 karakter hex + newline = 52 byte ciphertext (13 blok 4-byte).
>
> **Titik penting:** xxd flag.enc \| head · head -5 pairs.txt · wc -l pairs.txt
>
> **Berikutnya:** [Analisis](04-feistel-differential-02-analisis.md)

### 1.1 Deskripsi challenge

> Author: Illal
>
> Sebuah vendor logistik menggunakan cipher buatan sendiri untuk melindungi
> token gudangnya, dan mengklaim cipher tersebut aman untuk digunakan.
>
> Implementasi cipher, data yang tersedia, dan flag yang telah dienkripsi
> dapat ditemukan pada file lampiran. Buktikan apakah klaim keamanan tersebut
> benar.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `cipher.py` | 1.210 byte | `85b2e086577394a64465c8524382558ac37ad72fcef85d96dd0bf46f864df2a6` |
| `pairs.txt` | 7.560.419 byte | `56f903f2f71a91e7e17d5844dedf74005eefecc7b4e5108b48c9e1d1808a1977` |
| `flag.enc` | 105 byte | `6f6c4c2efbb435f8f78028df63581ed8f6ad9aa976a9026d96a459012c59960b` |

### 1.3 Environment

- Python 3.12
- `z3-solver`
- Tidak perlu Sage. Tidak ada service.

### 1.4 Triage awal

```bash
$ xxd flag.enc | head
00000000: 6337 6539 3733 6537 3732 3965 3135 6535  c7e973e7729e15e5
...
00000060: 3534 6233 3639 6162 0a                   54b369ab.
```

`flag.enc` adalah 104 karakter hex + newline = **52 byte ciphertext**
(13 blok 4-byte).

```bash
$ head -5 pairs.txt
# input difference: 0000000a
889da34b 444d9f47 444b9fe7
715c7236 209611bd 209c115d
...
$ wc -l pairs.txt
280027 pairs.txt      # 27 baris header/komentar + 280000 data
```
