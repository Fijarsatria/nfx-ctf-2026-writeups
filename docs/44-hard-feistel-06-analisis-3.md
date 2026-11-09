# Hard Feistel — Analisis

[← Overview](44-hard-feistel.md) · [Index](index.md)

## 2.5 Serialisasi output

Setelah 16 ronde, register berisi:

- `ebx` = `L16` (karena `new L = old R`, dan `L16 = R15`).
- `eax` = `R16` (hasil ronde terakhir).

Penyimpanan output:

```asm
11b6:  movzx  ecx,bh
11b9:  add    rdi,0x4
11bd:  mov    BYTE PTR [r10+0x1],bl
11c1:  add    r10,0x4
11c5:  mov    BYTE PTR [r10-0x4],cl   ; byte 0 = bh
11c9:  movzx  ecx,ah
11cc:  mov    BYTE PTR [r10-0x2],cl   ; byte 2 = ah
11d0:  mov    BYTE PTR [r10-0x1],al   ; byte 3 = al
```

Urutan byte: `[bh, bl, ah, al]` = `big-endian(L16) || big-endian(R16)`. Ini penting: output menyimpan **kedua half** sehingga transformasi invertibel penuh.

## 2.6 Ciphertext

```asm
11d9:  mov    edx,0x28              ; 40 byte
11de:  lea    rsi,[rip+0x2e3b]      # 4020 (.data)
11e5:  mov    rdi,r9
11e8:  call   10c0 <memcmp@plt>
```

Isi `.data` `0x4020`:

```text
Contents of section .data:
 4020 b949ad0b cc2c0880 63ec6501 c0776b74  .I...,..c.e..wk.
 4030 4cb390a4 0840aeb3 ff87facc 95252c4d  L....@.......%,M
 4040 11b58590 7ca91072                    ....|..r
```

Ciphertext 40 byte:

```text
b9 49 ad 0b cc 2c 08 80 63 ec 65 01 c0 77 6b 74
4c b3 90 a4 08 40 ae b3 ff 87 fa cc 95 25 2c 4d
11 b5 85 90 7c a9 10 72
```

## 2.7 Dekripsi Feistel

Feistel memiliki sifat:

```text
L_{i+1} = R_i
R_{i+1} = L_i XOR F(R_i, K_i)
```

Maka inverse dari state `(L_{i+1}, R_{i+1})`:

```text
R_i = L_{i+1}
L_i = R_{i+1} XOR F(L_{i+1}, K_i)
```

Iterasi `i` dari 15 turun ke 0. Tidak perlu menginversi `F` sama sekali—cukup memanggil `F` yang sama.
