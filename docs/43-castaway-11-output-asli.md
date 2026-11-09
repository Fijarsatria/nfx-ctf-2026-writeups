# Castaway — Output asli

[← Overview](43-castaway.md) · [Index](index.md)

## 3.3 Output asli

```text
$ python3 writeups/assets/castaway/solve_castaway.py
[*] binary        : /home/bocil/ctf/nfx/reverse/Hard_03_Castaway/castaway
[*] sbox256       : 0a dd ef 13 16 8c fb f9 22 08 b9 71 03 9d 27 c3 ... (256 byte)
[*] sbox16        : dc 5a c5 d4 1c d2 bb 6b 82 5c 9a f1 d1 96 76 bd
[*] ciphertext    : d554ada841e3e679f6bf13d01d319dd72db7cd6ea9c8e8a4957bcacbb55f16f0362681c32cfb9b74
[*] ptrace normal : return 0 -> out[0] tidak di-XOR
[*] anti_debug=0: valid -> b'NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}'
[+] FLAG          : NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}
[*] verifikasi    : stdout='flag> Access granted.' rc=0
[*] anti_debug=1: tidak valid -> b'\xfaA\xe7`\xc4K\xfeK\t\xd4\x91\xd0\xda!\x81\xc4\x01/\x9c\xff\x9f\x83>\\~~\\]\xff\x07\xce\x942\xb5f\x11\x1e\x1f$\xda'
[*] Catatan: state 0x32 (output[0]=0xff) adalah dead code karena
    opaque predicate (i*i & 3) == 2 tidak pernah benar untuk integer.
```

`anti_debug=1` menghasilkan byte non-printable, jadi kandidat itu ditolak. Hanya `anti_debug=0` yang menghasilkan flag valid.
