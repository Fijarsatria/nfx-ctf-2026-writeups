# Commit yang kehapus — Cara mendapatkan flag

[← Overview](84-commit-yang-kehapus.md) · [Index](index.md)

> **Langkah 2/5.** Key = email, AWS key, dan fingerprint PGP. Keystream-nya `SHA256(key || counter)`.
>
> **Berikutnya:** [Flag](84-commit-yang-kehapus-03-flag.md)

```bash
git cat-file -p 21d5a194fb6a627b1702cbf74b51589789988b72
```

```text
PGP_FINGERPRINT=4F9E-881C-B204-77A1
ENCRYPTED_FLAG_HEX=2b462d2964457eea57886bb55efb59f72f35c6d87db4b134e0d74cb3b29a83e858800871b4e7bbeb
KEY_FORMAT=<author_email>|<leaked_aws_key_id>|<pgp_fingerprint>
```

```python
import hashlib
ct = bytes.fromhex("2b462d2964457eea57886bb55efb59f72f35c6d87db4b134e0d74cb3b29a83e858800871b4e7bbeb")
ks = "k.vance@ops-shadow-nfx.internal|AKIA-NFX-99204811|4F9E-881C-B204-77A1"
k = hashlib.sha256(ks.encode()).digest()
stream = b"".join(hashlib.sha256(k + i.to_bytes(4, "big")).digest() for i in range(2))
print(bytes(a ^ b for a, b in zip(ct, stream)).decode())
```

```text
NFXCTF{g1t_d4ngl1ng_bl0b_h4v0c_5c8a19d4}
```

XOR langsung dengan `SHA256(key)` tidak cocok. Yang benar adalah keystream `SHA256(key || uint32_be(i))`.
