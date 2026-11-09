# Static IV Offline — Recon

[← Overview](22-static-iv-offline.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: rio
>
> `challenge.py` memperlihatkan bagaimana flag dienkripsi secara offline
> menggunakan AES-256-CBC. IV yang dipakai statis, sedangkan key diturunkan
> dari `SHA256(MASTER || counter)`. Nilai `MASTER` tersedia di
> `challenge.py`, sementara `counter` dan ciphertext ada di `output.txt`.
>
> Dapatkah kamu memulihkan flag dari ciphertext tersebut?

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `challenge.py` | 901 byte | `9db56543f1a9e477b346b4f17c648d3617f959ecae2d04a15b3e95e7d870ae00` |
| `output.txt` | 328 byte | `9b02a67da90ec0ae31f8f7a183a95f9561bc5131c453429a6dc1f002a66eb970` |

### 1.3 Environment

- Python 3.12
- `pycryptodome` (`Crypto.Cipher.AES`, `Crypto.Util.Padding`)
- Tidak perlu service / Sage.

### 1.4 Triage awal

```bash
$ cat challenge.py
```

```python
# ======================= challenge.py =======================
# FILE UNTUK PESERTA
# Skrip ini memperlihatkan bagaimana flag dienkripsi. MASTER terbuka.
import hashlib, json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

MASTER = b"\x13\x37" * 16           # <-- ini bocor, bug kedua
PREFIX = b"user-input-goes-here:"

def get_key(counter):
    return hashlib.sha256(MASTER + counter.to_bytes(4, "little")).digest()[:32]

def encrypt_flag(flag: bytes, iv: bytes, counter: int) -> bytes:
    key = get_key(counter)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(PREFIX + b"|" + flag, 16))

if __name__ == "__main__":
    data = json.load(open("output.txt"))
    print("counter:", data["counter"])
    print("iv_hex :", data["iv_hex"])
    print("ct_hex :", data["ct_hex"][:64], "...")
    print("hint: MASTER ada di file ini. counter ada di output.txt.")
```

```bash
$ cat output.txt
{
  "ct_hex": "7739b21e85a44c8fabc82ed42b5b4f872d94b59578da88e4ec9a258224118b493ab06f1054a0fe6172840762fe21441ada0f0260513b3858dc2ab4dfac6fb61c41df848bf5bbdabe8910b155dd487c33",
  "iv_hex": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "counter": 11,
  "note": "IV statis, key = SHA256(MASTER || counter). MASTER ada di challenge.py."
}
```

Panjang ciphertext: 80 byte = 5 blok AES (kelipatan 16). Prefix
`user-input-goes-here:|` panjangnya 22 byte, sehingga total plaintext
22 + 48 = 70 byte, lalu dipad ke 80.
