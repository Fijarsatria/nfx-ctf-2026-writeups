# Medium RC4 — Flag & Verifikasi

[← Overview](46-medium-rc4.md) · [Index](index.md)

```text
NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}
```

Cek file flag lokal:

```text
$ cat flags/reverse/Medium_01_RC4.txt
NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}
```

Verifikasi:

1. Flag di `flags/reverse/Medium_01_RC4.txt` isinya identik.
2. Menjalankan binary dengan flag tersebut:

```text
$ ./reverse/Medium_01_RC4/medium_rc4 'NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}'
Correct! RC4 memang simetris.
rc=0
```

3. Input salah menghasilkan `Wrong!` dan `rc=1`:

```text
$ ./reverse/Medium_01_RC4/medium_rc4 'NFX{wrong}'
Wrong!
rc=1
```

**Status: `verified local`.** Flag tidak disubmit ke platform; verifikasi dilakukan sepenuhnya terhadap binary dan file flag lokal.

## Flag

`NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}`

**Status:** `VERIFIED`
