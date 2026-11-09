# Medium RC4 — Analisis

[← Overview](46-medium-rc4.md) · [Index](index.md)

### 2.1 Peta fungsi `main`

Karena binary stripped, kita mulai dari entry point `0x12a0`, yang memanggil `__libc_start_main` dengan `main` di `0x10e0`. Alur `main`:

1. `0x1101` cek `argc > 1`; kalau tidak, cetak `Pemakaian: %s <flag>` dan keluar dengan kode 2.
2. `0x110a–0x111a` ambil `argv[1]`, panggil `strlen`, dan cek hasilnya `== 0x2a` (42).
3. Jika panjang bukan 42, cetak `Wrong!` dan return 1.
4. `0x1153–0x116d` inisialisasi array `S[0..255] = 0..255` di `[rsp+0x100]`.
5. `0x116f–0x11d6` key-scheduling algorithm (KSA) RC4.
6. `0x11d8–0x123c` pseudo-random generation algorithm (PRGA) + XOR dengan input, panjang 42.
7. `0x123e–0x124d` `memcmp(hasil, ciphertext@0x2060, 42)`.
8. Jika sama, cetak `Correct! RC4 memang simetris.`

Potongan disassembly yang relevan (dari `objdump -d -Mintel`):

```asm
; cek panjang = 42
110e:  mov    rdi,rbx
1111:  call   10a0 <strlen@plt>
1116:  cmp    rax,0x2a
111a:  je     1153

; inisialisasi S[i] = i
1153:  xor    eax,eax
1155:  lea    rdi,[rsp+0x100]
1160:  mov    BYTE PTR [rdi+rax*1],al
1163:  add    rax,0x1
1167:  cmp    rax,0x100
116d:  jne    1160

; key = 0x2021, magic modulus 19
1173:  lea    r10,[rip+0xea7]        # 2021
117a:  movabs r9,0xd79435e50d79435f
```

KSA (loop 256 kali) melakukan:

```asm
1188:  mov    rax,rcx                 ; i
118b:  movzx  r8d,BYTE PTR [rdi+rcx*1] ; S[i]
1190:  mul    r9                      ; magic multiply
1193:  shr    rdx,0x4
1197:  lea    rax,[rdx+rdx*8]
119b:  lea    rdx,[rdx+rax*2]         ; rdx = 19 * (i / 19)
119f:  mov    rax,rcx
11a2:  sub    rax,rdx                 ; rax = i % 19
11a5:  movzx  edx,r8b
11a9:  movzx  eax,BYTE PTR [r10+rax*1] ; key[i % 19]
11ae:  add    eax,edx
11b0:  add    eax,esi                 ; + j
11b2:  movzx  eax,al
11b5:  movzx  edx,BYTE PTR [rsp+rax*1+0x100] ; S[(j + ...) & 0xff]
11bd:  mov    rsi,rax                 ; j = ...
11c0:  mov    BYTE PTR [rdi+rcx*1],dl ; swap S[i], S[j]
11c3:  add    rcx,0x1
11c7:  mov    BYTE PTR [rsp+rax*1+0x100],r8b
11cf:  cmp    rcx,0x100
11d6:  jne    1188
```

Magic `0xd79435e50d79435f` adalah trik compiler untuk membagi 64-bit dengan 19 tanpa instruksi `div`. Setelah `mul`, `rdx >> 4`, lalu `rdx*19`, hasilnya `i - 19*(i/19) = i % 19`. Jadi panjang key adalah **19 byte**, cocok dengan string `n0t_s3cur3_k3y_2026`.

PRGA lalu XOR 42 byte:

```asm
11e8:  add    edx,0x1
11eb:  movzx  edi,dl
11ee:  movzx  eax,BYTE PTR [rsp+rdi*1+0x100]
11f9:  add    ecx,eax
11fb:  movzx  r9d,cl
11ff:  movzx  r10d,BYTE PTR [rsp+r9*1+0x100]
120b:  mov    BYTE PTR [rsp+rdi*1+0x100],r10b
1213:  mov    BYTE PTR [rsp+r9*1+0x100],al
121b:  add    al,BYTE PTR [rsp+rdi*1+0x100]
1222:  movzx  eax,al
1225:  movzx  eax,BYTE PTR [rsp+rax*1+0x100]
122d:  xor    al,BYTE PTR [rbx+rsi*1]  ; ^= input[i]
1230:  mov    BYTE PTR [r8+rsi*1],al   ; output[i]
1234:  add    rsi,0x1
1238:  cmp    rsi,0x2a
123c:  jne    11e8
```

Dan perbandingan:

```asm
123e:  mov    edx,0x2a
1243:  lea    rsi,[rip+0xe16]        # 2060
124a:  mov    rdi,r8
124d:  call   10c0 <memcmp@plt>
1252:  mov    r12d,eax
1255:  test   eax,eax
1257:  jne    111c                    ; Wrong!
```

### 2.2 Ekstraksi konstanta

Dari instruksi `lea` di atas:

- Key berada di `.rodata` **`0x2021`**, panjang 19 byte. Isinya persis `n0t_s3cur3_k3y_2026` (0x6e 0x30 0x74 ...).
- Ciphertext berada di **`0x2060`**, panjang `0x2a = 42` byte.

Hex dump `.rodata` (dari `objdump -s -j .rodata`):

```text
Contents of section .rodata:
 2000 01000200 50656d61 6b616961 6e3a2025  ....Pemakaian: %
 2010 73203c66 6c61673e 0a005772 6f6e6721  s <flag>..Wrong!
 2020 006e3074 5f733363 7572335f 6b33795f  .n0t_s3cur3_k3y_
 2030 32303236 00436f72 72656374 21205243  2026.Correct! RC
 2040 34206d65 6d616e67 2073696d 65747269  4 memang simetri
 2050 732e0000 00000000 00000000 00000000  s...............
 2060 ada1e2de 80fab7a4 65572a79 e3ecf825  ........eW*y...%
 2070 690a5cca 49dff6ca a4c29c36 d2485f17  i.\.I......6.H_.
 2080 bb3e29d2 01f7009c 9d31               .>)......1
```

Jadi:

```text
key        = 6e 30 74 5f 73 33 63 75 72 33 5f 6b 33 79 5f 32 30 32 36
           = "n0t_s3cur3_k3y_2026"
ciphertext = ad a1 e2 de 80 fa b7 a4 65 57 2a 79 e3 ec f8 25
             69 0a 5c ca 49 df f6 ca a4 c2 9c 36 d2 48 5f 17
             bb 3e 29 d2 01 f7 00 9c 9d 31
```

### 2.3 Mengapa dekripsi = enkripsi

RC4 adalah stream cipher: keystream `K` dibangkitkan dari key, lalu ciphertext `C = P XOR K`. Karena XOR involutif:

```text
P = C XOR K = (P XOR K) XOR K
```

Binary tidak pernah "mendekripsi" secara eksplisit; ia melakukan PRGA lalu XOR dengan input, kemudian membandingkan hasilnya dengan ciphertext. Artinya, jika kita memasukkan **plaintext yang benar**, hasilnya akan sama dengan ciphertext. Untuk mendapatkan plaintext dari ciphertext, kita menjalankan operasi XOR yang sama dengan ciphertext sebagai input.
