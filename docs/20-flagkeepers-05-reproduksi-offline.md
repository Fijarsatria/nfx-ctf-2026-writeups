# FlagKeepers — Reproduksi offline

[← Overview](20-flagkeepers.md) · [Index](index.md)

## 3.4 Reproduksi offline

Karena oracle sudah tidak selalu hidup, serangan juga direproduksi offline
dengan `app.py` semantics dan flag placeholder. Script:
`writeups/assets/flagkeepers/offline_sim.py`.

```text
$ python3 offline_sim.py
[*] collected 14 RECOVERY samples, len = 51
[*] recovered H_b       = 0x7ab223f587d44702d189c082bdb1b954
[*] E_K(J0) candidates  = 1 (must be 1)
[*] forged CT           = eb63a256c554cf85437af70ccc63ccab1c2961ee28535c5741802cf9b5b5d5ca401e2cfd8a45214f55a7943ce6e62059d9b75b
[*] forged TAG          = 031cd464820d4c2688dfa5b8fd030492
[*] server-side check:
    decrypt_and_verify  = OK
    plaintext           = b'admin = True                                       '
    admin = True in msg[:idx] -> True
    flag (offline demo) = NFX{placeholder_offline_demo}
```

`H` dan CT berbeda dari run live karena key/nonce acak, tetapi alurnya sama
dan `decrypt_and_verify` membuktikan tag forgery valid.
