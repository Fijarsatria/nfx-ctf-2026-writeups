# Weak Handshake — Analisis

[← Overview](27-weak-handshake.md) · [Index](index.md)

### 2.1 FTP: “kenangan yang mudah terlihat”

FTP control:

```text
220 pyftpdlib 2.2.0 ready.
USER anonymous
331 Username ok, send password.
PASS ftp@example.com
230 Login successful.
257 "/" is the current directory.
229 Entering extended passive mode (|||42345|.)
TYPE I
200 Type set to: Binary.
SIZE clannad.webp
213 262796
RETR clannad.webp
125 Data connection already open; Transfer starting.
```

Data stream port 42345 di-reassemble menjadi `clannad.webp`:

```bash
$ file clannad.webp
RIFF (little-endian) data, Web/P image

$ sha256sum clannad.webp
bf90425076e330c58a11c997f814172dd31b599534533a2bfd81d3fb4a2652a5  clannad.webp
```

`exiftool`:

```text
File Type      : Extended WEBP
WebP Flags     : EXIF
Image Width    : 1920
Image Height   : 1080
Warning        : [minor] Improper EXIF header
```

Gambar Clannad adalah **decoy/awal cerita**. Flag tidak ada di gambar ini.

### 2.2 TLS handshake

ClientHello (record pertama, port 56410):

```text
16 03 01 00 97
01 00 00 93 03 03
1e ff 90 57 cd 9c b0 06 9a c8 f8 67 66 55 2b ab
ca 7b 97 b0 ce 08 ac 2c a9 1b c3 f9 62 c4 6c 3b
...
00 02 00 2f
```

- Client version: TLS 1.2 (`03 03`)
- Cipher suite: hanya `0x002f` = `TLS_RSA_WITH_AES_128_CBC_SHA`
- Extension `0x0017` = `extended_master_secret`
- Server name: `tomoyo.local`

ServerHello (port 8443):

```text
16 03 03 00 59
02 00 00 55 03 03
76 45 7c 9f e0 81 a3 cb c1 d6 52 a5 5c 0a ea 30
22 be e6 99 b4 a6 df 0f b6 80 be 57 1e 4f 16 e3
...
00 2f
...
00 17 00 00
```

Server memilih `0x002f` dan mengaktifkan `extended_master_secret` (`00 17 00 00`).

### 2.3 Sertifikat RSA 1024-bit

Ambil Certificate handshake:

```bash
$ openssl x509 -inform DER -in tomoyo_cert.der -noout -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            62:7e:63:91:c5:a2:bf:d7:e1:07:81:57:b7:c3:40:50:78:92:a2:e0
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = tomoyo.local
        Validity
            Not Before: Aug 21 06:09:15 2026 GMT
            Not After : Aug 21 06:09:15 2027 GMT
        Subject: CN = tomoyo.local
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (1024 bit)
                Modulus:
                    00:85:34:f8:d6:d3:47:e5:96:05:87:a7:13:aa:11:
                    d4:b0:e5:41:cf:94:b6:5f:a1:62:9a:0d:04:7b:f7:
                    ...
                    08:b6:95:31:11:4f:16:38:45
                Exponent: 65537 (0x10001)
```

Modulus 1024-bit. Ini sudah “lemah” untuk standar modern, tetapi masih terlalu besar untuk factoring umum. Namun key ini punya cacat: **p dan q sangat berdekatan**.

### 2.4 Fermat factorization

```python
import math
n = int('8534F8D6...163845', 16)
a = math.isqrt(n)
if a*a < n: a += 1
for i in range(2_000_000):
    b2 = a*a - n
    b = math.isqrt(b2)
    if b*b == b2:
        p, q = a-b, a+b
        print(i, q-p, p, q)
        break
    a += 1
```

Output:

```text
Fermat factor i=0: p-q=236
p = 9671663854061757801267503507385555068467793967854600233585619689920384829606622498532429734086689244075916698567447356461587231266615301209335653115679383
q = 9671663854061757801267503507385555068467793967854600233585619689920384829606622498532429734086689244075916698567447356461587231266615301209335653115679619
```

Karena `n = p*q`, private exponent:

```python
d = pow(65537, -1, (p-1)*(q-1))
key = RSA.construct((n, 65537, d, p, q))
```

Private key tersimpan di `assets/weak-handshake/04-tomoyo_priv.pem`.

### 2.5 ClientKeyExchange dan premaster

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

### 2.6 Extended Master Secret

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

### 2.7 Format record ciphertext

Setiap record setelah ChangeCipherSpec memiliki bentuk:

```text
body = IV (16 byte) || ciphertext (kelipatan 16) || MAC (20 byte, di luar ciphertext)
```

Ini bukan format TLS standar (TLS biasanya menaruh MAC di dalam enkripsi), tetapi konsisten untuk semua record dan berhasil didekripsi dengan:

```python
iv = body[:16]
ct = body[16:-20]
pt = AES.new(server_key, AES.MODE_CBC, iv=iv).decrypt(ct)
# hapus PKCS#7 padding
```

Record pertama setelah CCS adalah Finished (`14 00 00 0c` + verify_data 12 byte). Record berikutnya adalah application data HTTP.

### 2.8 HTTP response

Sesi 1:

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.10.13
Date: Fri, 21 Aug 2026 11:23:13 GMT
Content-type: image/jpeg
Content-Length: 67649
Last-Modified: Fri, 21 Aug 2026 06:24:15 GMT
```

Sesi 2:

```text
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.10.13
Date: Fri, 21 Aug 2026 11:23:17 GMT
Content-type: image/jpeg
Content-Length: 323692
Last-Modified: Fri, 21 Aug 2026 06:24:15 GMT
```

Keduanya mengirim JPEG. JPEG pertama adalah Tomoyo di koridor sekolah (decoy/awal). JPEG kedua adalah Tomoyo dengan overlay teks:

```text
{D36A64128F80788B60C677EF94FA7157}
```
