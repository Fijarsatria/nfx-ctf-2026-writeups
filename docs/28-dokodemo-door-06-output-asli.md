# Dokodemo Door — Output asli

[← Overview](28-dokodemo-door.md) · [Index](index.md)

## 3.3 Output asli

```text
$ python3 solve_dokodemo.py
ciphertext bytes      : 8672
candidate key length  : 16
recovered key         : b'nfx_k3tuk_p1ntu!'
crib-unknown positions: [9] filled with (95,)
decrypted header      : b'%PDF-1.4\n%\x93\x8c\x8b\x9e Repor'
decrypted trailer     : b'>>\nstartxref\n8239\n%%EOF\n'
score                 : 1213
written               : /tmp/opencode/dokodemo_decrypted.pdf
```

Ekstraksi teks:

```text
$ python3 extract_text.py
PDF bytes: 8672
[ NFX PROTOCOL // RESTRICTED ACCESS ]
DOKODEMO DOOR
Sandi Rahasia Gerbang Masuk Sektor Barat
Di balik pintu ini terdapat akses langsung menuju jaringan rahasia NFX.
Hanya mereka yang memiliki otentikasi sah yang diperkenankan masuk.
Ketuk tiga kali pada pintu dan bisikkan kode otorisasi:
Flag: NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}
Gunakan flag di atas untuk melakukan submission pada platform CTF.
NFX CLASSIFIED ARCHIVE // STRICTLY CONFIDENTIAL // DO NOT DISTRIBUTE
```

### Evidence langkah ini

![term-02-extracted-text.png](assets/dokodemo-door/term-02-extracted-text.png)

*Terminal evidence — `02-extracted-text.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`02-extracted-text.txt`](assets/dokodemo-door/02-extracted-text.txt)
