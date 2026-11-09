# Access Remains — Analisis

[← Overview](24-access-remains.md) · [Index](index.md)

### 2.1 SAM + SYSTEM + SECURITY → NTLM

```bash
$ impacket-secretsdump -sam SAM -system SYSTEM -security SECURITY local
Impacket v0.11.0

[*] Target system bootKey: 0xebb2a56259f7159e9212f18404916d75
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:649d3cf918fa4e6d37b562401cfddc8d:::
aria:1002:aad3b435b51404eeaad3b435b51404ee:250a19ea48a88bbc7532f08ecb072844:::
ariaf:1005:aad3b435b51404eeaad3b435b51404ee:f545ff727c989c387b9d1be6db74ea1c:::
...
[*] DPAPI_SYSTEM
dpapi_machinekey:0xbdfcaa5114510b901fba51f5e66fc738cb195a73
dpapi_userkey:0x04a0a4b6579654f373df1293c429b33f5c7450b9
```

NTLM adalah MD4 dari UTF-16LE password. Verifikasi kandidat:

```python
from Crypto.Hash import MD4
for user, h in {'aria':'250a19ea48a88bbc7532f08ecb072844',
                'ariaf':'f545ff727c989c387b9d1be6db74ea1c'}.items():
    for p in ['aria','ariafe006']:
        m = MD4.new(); m.update(p.encode('utf-16le'))
        print(user, p, m.hexdigest() == h)
```

Output:

```text
aria   candidate=aria         NT=250a19ea48a88bbc7532f08ecb072844  match=True
aria   candidate=ariafe006    NT=f545ff727c989c387b9d1be6db74ea1c  match=False
ariaf  candidate=aria         NT=250a19ea48a88bbc7532f08ecb072844  match=False
ariaf  candidate=ariafe006    NT=f545ff727c989c387b9d1be6db74ea1c  match=True
```

Jadi:

| User | Password |
|---|---|
| `aria` | `aria` |
| `ariaf` | `ariafe006` |

### 2.2 DPAPI masterkey

Masterkey user `ariaf`:

```text
AppData/Roaming/Microsoft/Protect/S-1-5-21-3304503823-3980900213-1333018566-1005/bb24f650-d046-439c-a88b-ab8f89ba61a4
```

Dekripsi dengan password `ariafe006`:

```bash
$ python3 /usr/share/doc/python3-impacket/examples/dpapi.py masterkey \
    -file bb24f650-d046-439c-a88b-ab8f89ba61a4 \
    -sid S-1-5-21-3304503823-3980900213-1333018566-1005 \
    -password 'ariafe006'
Impacket v0.11.0

[MASTERKEYFILE]
Version     :        2 (2)
Guid        : bb24f650-d046-439c-a88b-ab8f89ba61a4
Flags       :        5 (5)
Policy      :        0 (0)
MasterKeyLen: 000000b0 (176)
BackupKeyLen: 00000090 (144)
CredHistLen : 00000014 (20)
DomainKeyLen: 00000000 (0)

Decrypted key with User Key (SHA1)
Decrypted key: 0x2cbc5b2e483dae00c5593617eb517b8cabec639f354ca8f75b4296e82f3c8d2e83f2ce9a6ae64e3f1f849098f985b2d64e74e81affd37021392b7ba7b4635b55
```

### 2.3 Credential Manager

Dua file credential:

- Local: `AppData/Local/Microsoft/Credentials/DFBE70A7E5CC19A398EBF1B96859CE5D`
- Roaming: `AppData/Roaming/Microsoft/Credentials/B0294E9651990C1435CA6300E4BB2378`

Dekripsi dengan masterkey:

```bash
MK=0x2cbc5b2e483dae00c5593617eb517b8cabec639f354ca8f75b4296e82f3c8d2e83f2ce9a6ae64e3f1f849098f985b2d64e74e81affd37021392b7ba7b4635b55
python3 /usr/share/doc/python3-impacket/examples/dpapi.py credential \
  -file B0294E9651990C1435CA6300E4BB2378 -key $MK
```

Output penting:

```text
[CREDENTIAL]
LastWritten : 2026-08-18 16:49:31
Flags       : 0x00000030 (CRED_FLAGS_REQUIRE_CONFIRMATION|CRED_FLAGS_WILDCARD_MATCH)
Persist     : 0x00000003 (CRED_PERSIST_ENTERPRISE)
Type        : 0x00000001 (CRED_TYPE_GENERIC)
Target      : LegacyGeneric:target=AccessRemains:WaifuVault
Username    : ariaf@access-remains.local
Unknown     : KumikoOumae2107!@
```

Credential lokal adalah `WindowsLive:target=virtualapp/didlogical` (tidak relevan). Credential roaming memberi password **`KumikoOumae2107!@`** untuk target `AccessRemains:WaifuVault`.

### 2.4 Membuka Kumiko.zip

```bash
$ 7z x -y -p'KumikoOumae2107!@' Kumiko.zip
...
Everything is Ok

Files: 6
Size:       531182
Compressed: 530710
```

Isi:

```text
kumiko01.jpg
kumiko02.jpg
kumiko03.jpg
kumiko04.jpg
kumiko05.jpg
note.txt
```

`note.txt`:

```text
Ariaf said this archive only contained photos of Kumiko.

There was no report, no document, and no obvious message.
Only a few pictures, preserved like quiet memories from a performance
that had already ended.

But some sounds do not disappear completely.

Even if the sound fades, the truth still resonates somewhere.

It may no longer be heard by the ear,
but it can still be found by those willing to look carefully.

A photograph can hold more than a face.
A memory can carry more than a feeling.
And sometimes, what remains is not written in plain sight.

Among these images, one still carries the echo.

Find the one that remembers.
```

Petunjuk: “one still carries the echo” / “one that remembers” → satu gambar menyimpan pesan. `kumiko03.jpg` adalah yang berbeda: 387×755, baseline JPEG, memiliki ICC profile, dan pada bagian bawah terdapat overlay teks.

### 2.5 Ekstraksi teks dari `kumiko03.jpg`

`exiftool` tidak menemukan flag di metadata. Secara visual, bagian bawah gambar memuat teks:

```text
{3E2D6090E7EEB47D5
38FC27AC2789C02}
```

Penggabungan:

```text
3E2D6090E7EEB47D5 + 38FC27AC2789C02
= 3E2D6090E7EEB47D538FC27AC2789C02
```

32 karakter hex, dapat dikelompokkan menjadi 4 grup 8:

```text
3E2D6090  E7EEB47D  538FC27A  C2789C02
```
