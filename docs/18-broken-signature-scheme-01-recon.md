# Broken Signature Scheme — Recon

[← Overview](18-broken-signature-scheme.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: rio
>
> Tantangan kriptografi berlapis tiga. Dimulai dari skema signature RSA yang
> lemah, dilanjutkan dengan RSA modulus yang faktornya berdekatan dan partial
> key exposure, lalu ciphertext flag yang dienkripsi menggunakan AES-GCM.
>
> Dapatkah kamu menembus ketiga layer tersebut?
>
> Format: `NXCTF{...}`

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `challenge.py` | 870 byte | `f5cbd12a4225d139a84e693e2be23b0b827763a716cb440bf8304e03d8093943` |
| `output.txt` | 4.392 byte | `a89d84089e4e67617d57a223474dab7ced37eda40d5b2df31f4b8454c28d4eb7` |

### 1.3 Environment

- Python 3.12
- `pycryptodome`
- Tidak perlu Sage; `math.isqrt` cukup untuk layer 2.

### 1.4 Triage awal

`challenge.py` hanya mencetak ringkasan:

```text
$ python3 challenge.py
N bits     : 2047
e          : 65537
leak       : 0x69252 pos 500 bits 20
delta_bits : 300
valid sigs : 6
target msg : b'give-me-the-flag'

Skema: sig(m) = m^d mod N  (RSA multiplicative, H identitas)
RSA  : q = nextprime(p + 2^300), leak 20 bit tengah p
Flag : AES-GCM, key = SHA256(p||q)
Petunjuk layer 1: produk sig(m_i) menghasilkan sig(prod m_i)
```

Struktur `output.txt`:

```json
{
  "N": "0x4094...c61",
  "e": 65537,
  "leak": "0x69252",
  "leak_pos": 500,
  "leak_bits": 20,
  "delta_bits": 300,
  "valid_sigs": [ {"msg": "...", "sig": "..."} x6 ],
  "target_msg_hex": "676976652d6d652d7468652d666c6167",
  "flag_cipher": {"nonce_hex": "...", "ct_hex": "...", "tag_hex": "..."}
}
```
