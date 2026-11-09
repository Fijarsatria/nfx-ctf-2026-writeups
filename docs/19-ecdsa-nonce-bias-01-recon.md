# ECDSA Nonce Bias — Recon

[← Overview](19-ecdsa-nonce-bias.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: rio
>
> Diberikan 200 signature ECDSA pada kurva secp256k1. Nonce yang dipakai
> tidak acak seragam: 8 bit teratas selalu nol, sehingga `k < 2^248`.
> Terdapat juga ciphertext flag yang dienkripsi dengan AES-GCM menggunakan
> key turunan dari private key ECDSA.
>
> Pulihkan private key dan dekripsi flag.
>
> Format: `NXCTF{...}`

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `challenge.py` | 1.010 byte | `b2df03ad70dd772ef0ddefc44a4cc4bca6461d1f61103e1145b0ab8e64417063` |
| `output.txt` | 69.107 byte | `74f93d9a9c1399cfc2a1e756c273fe476992ad035cb910b5bf370a7823aa73e9` |
| `pubkey.pem` | 174 byte | `500c7aaa3253086496b618836c14c8bbefe5123c2f857563bdaaf84803360212` |

### 1.3 Environment

- Python 3.12
- `fpylll` (LLL/BKZ)
- `pycryptodome` (ECC + AES-GCM)
- Tidak perlu Sage.

### 1.4 Triage awal

```bash
$ python3 challenge.py
kurva        : secp256k1
jumlah sig   : 200
contoh r     : 0xeceab8d52f1aa178 ...
contoh s     : 0xd999ae372497ce11 ...
contoh h     : 0xa16f9f47cab16c05 ...
top8_k       : 0  K_BITS = 248
flag cipher  : nonce=01733cfb..., tag=7e4bc9c1...
```

`output.txt` memuat `n` (orde secp256k1), 200 objek
`{msg, r, s, h, top8_k, K_BITS}`, dan `flag_ciphertext`.
