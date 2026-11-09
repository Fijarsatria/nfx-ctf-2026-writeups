# Hard Feistel — Flag & Verifikasi

[← Overview](44-hard-feistel.md) · [Index](index.md)

```text
NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}
```

Cek file flag lokal:

```text
$ cat flags/reverse/Hard_02_Feistel.txt
NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}
```

Verifikasi:

```text
$ ./reverse/Hard_02_Feistel/hard_feistel 'NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}'
Correct! Jaringan Feistel berhasil dibalik.
rc=0

$ ./reverse/Hard_02_Feistel/hard_feistel 'NFX{wrong}'
Wrong!
rc=1
```

Isi `flags/reverse/Hard_02_Feistel.txt` identik. **Status: `verified local`.** Flag tidak disubmit ke platform; verifikasi dilakukan sepenuhnya terhadap binary dan file flag lokal.

## Flag

`NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}`

**Status:** `VERIFIED`
