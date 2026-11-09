# My Lovely Freya — Dekripsi

[← Overview](29-my-lovely-freya.md) · [Index](index.md)

## 2.4 Dekripsi

```bash
$ openssl enc -d -aes-256-cbc -md sha256 -pbkdf2 -iter 100000 \
    -in surat_untuk_freya.enc \
    -pass 'pass:<!HayamGoreng45@/>' \
    -out surat-decrypted.txt
$ cat surat-decrypted.txt
NXCTF{FR3Y4_MY_L0V3LY!}
```

Verifikasi silang: password decoy gagal.

```text
$ openssl enc -d -aes-256-cbc -md sha256 -pbkdf2 -iter 100000 \
    -in surat_untuk_freya.enc -pass 'pass:AyamgGoreng45'
bad decrypt
```
