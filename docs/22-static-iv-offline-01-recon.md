# Static IV Offline — Recon

[← Overview](22-static-iv-offline.md) · [Index](index.md)

## 1.1 Deskripsi challenge

> Author: rio
>
> `challenge.py` memperlihatkan bagaimana flag dienkripsi secara offline
> menggunakan AES-256-CBC. IV yang dipakai statis, sedangkan key diturunkan
> dari `SHA256(MASTER || counter)`. Nilai `MASTER` tersedia di
> `challenge.py`, sementara `counter` dan ciphertext ada di `output.txt`.
>
> Dapatkah kamu memulihkan flag dari ciphertext tersebut?

## 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `challenge.py` | 901 byte | `9db56543f1a9e477b346b4f17c648d3617f959ecae2d04a15b3e95e7d870ae00` |
| `output.txt` | 328 byte | `9b02a67da90ec0ae31f8f7a183a95f9561bc5131c453429a6dc1f002a66eb970` |

## 1.3 Environment

- Python 3.12
- `pycryptodome` (`Crypto.Cipher.AES`, `Crypto.Util.Padding`)
- Tidak perlu service / Sage.
