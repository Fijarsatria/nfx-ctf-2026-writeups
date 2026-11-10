# Static IV Offline — Triage awal

[← Overview](22-static-iv-offline.md) · [Index](index.md)

> **Langkah 2/7 — Triage awal.** Panjang ciphertext: 80 byte = 5 blok AES (kelipatan 16).
>
> **Titik penting:** cat challenge.py · cat output.txt
>
> **Berikutnya:** [Analisis](22-static-iv-offline-03-analisis.md)

## 1.4 Triage awal

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
