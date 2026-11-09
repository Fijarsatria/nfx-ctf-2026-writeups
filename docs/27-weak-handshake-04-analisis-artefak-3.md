# Weak Handshake — Analisis Artefak

[← Overview](27-weak-handshake.md) · [Index](index.md)

## 2.5 ClientKeyExchange dan premaster

ClientKeyExchange:

```text
16 00 00 82
00 80
70 5a 3c 9b ... (128 byte ciphertext RSA)
```

Decrypt dengan private key (PKCS#1 v1.5):

```text
premaster = 0303a7db81cb42e9cd0156bcb4bd34890a8878ab838684db1fe340b319597ac14
            1a092397cd0ae44aa0529897bf2c729
```

48 byte, diawali versi `0303` — valid.

## 2.6 Extended Master Secret

Karena extension `0x0017` dinegosiasikan, master secret **tidak** memakai `client_random + server_random`, melainkan:

```text
session_hash = SHA256(ClientHello || ServerHello || Certificate || ServerHelloDone || ClientKeyExchange)
master_secret = PRF(pre_master_secret, "extended master secret", session_hash, 48)
key_block     = PRF(master_secret, "key expansion", server_random || client_random, 104)
```

Untuk AES-128-CBC-SHA:

```text
client_write_MAC  = key_block[0:20]
server_write_MAC  = key_block[20:40]
client_write_key  = key_block[40:56]
server_write_key  = key_block[56:72]
client_write_IV   = key_block[72:88]
server_write_IV   = key_block[88:104]
```

Nilai sesi pertama:

```text
session_hash = 4748f65b2bc160cf89c9bf8a79a65db9e34d5859c1570e226a7460f642aa1428
master       = a5238af33e2e13f0e05f9e29259cd9d9fcf2e883b47b1f72cb86f6c45d2d1f31
               2bf40641a17e327b8b634e1f5e838a83
server_key   = 3fda8cda19e2cdd551ca8ff0201946e6
```

Sesi kedua menghasilkan master dan key berbeda:

```text
master       = 151953826976a847c1f4f12e205237f2b575e4d508060e7fa7e3a3c199b9a2b5
               f740c3d31d9fb759dcd402dec43edef1
server_key   = 175295cce7a2ec71273d1191526a5e06
```
