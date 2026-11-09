# Castaway — Analisis

[← Overview](43-castaway.md) · [Index](index.md)

### 2.1 Fungsi `main`

Main ada di `0x142d`. Bagian penting:

```asm
144b:  mov    ecx,0x0
1450:  mov    edx,0x1
1455:  mov    esi,0x0
145a:  mov    edi,0x0
145f:  mov    eax,0x0
1464:  call   1150 <ptrace@plt>      ; ptrace(PTRACE_TRACEME, 0, 1, 0)
1469:  mov    QWORD PTR [rbp-0x150],rax
1470:  cmp    QWORD PTR [rbp-0x150],0xffffffffffffffff
1478:  sete   al
147b:  mov    BYTE PTR [rbp-0x151],al ; anti_debug = (ret == -1)

1481:  lea    rax,[rip+0xce0]        # 2168 "flag> "
1490:  call   1100 <printf@plt>
1495:  mov    rax,QWORD PTR [rip+0x2b74] # 4010 stdout
149f:  call   1140 <fflush@plt>
14a4:  mov    rdx,QWORD PTR [rip+0x2b75] # 4020 stdin
14ab:  lea    rax,[rbp-0x110]        ; buffer input
14b2:  mov    esi,0x100             ; fgets(buf, 256, stdin)
14ba:  call   1130 <fgets@plt>
```

Setelah input:

```asm
14ce:  lea    rax,[rbp-0x110]
14d5:  lea    rdx,[rip+0xc93]        # 216f "\r\n"
14e2:  call   1110 <strcspn@plt>     ; cari newline
14e7:  mov    BYTE PTR [rbp+rax*1-0x110],0x0  ; ganti dengan NUL
14ef:  mov    rdi,rax
14f9:  call   10e0 <strlen@plt>
14fe:  mov    QWORD PTR [rbp-0x148],rax
1505:  cmp    QWORD PTR [rbp-0x148],0x28 ; harus 40
150d:  je     1525
150f:  ... "Nope."
```

Lalu transformasi dan perbandingan:

```asm
1525:  lea    rdx,[rbp-0x140]        ; buffer output
152c:  mov    rcx,QWORD PTR [rbp-0x148] ; len
1533:  lea    rax,[rbp-0x110]        ; input
153a:  mov    rsi,rcx
153d:  mov    rdi,rax
1540:  call   1282 <transform>

1545:  movzx  eax,BYTE PTR [rbp-0x140]
154c:  xor    al,BYTE PTR [rbp-0x151] ; output[0] ^= anti_debug
1552:  mov    BYTE PTR [rbp-0x140],al

1558:  lea    rax,[rbp-0x140]
155f:  mov    edx,0x28              ; 40 byte
1564:  lea    rcx,[rip+0xbd5]        # 2140 ciphertext
156b:  mov    rsi,rcx
156e:  mov    rdi,rax
1571:  call   1120 <memcmp@plt>
1576:  test   eax,eax
1578:  jne    158b                   ; "Nope."
157a:  ... "Access granted."
```

### 2.2 Anti-debug

`ptrace(PTRACE_TRACEME, 0, 1, 0)` normalnya mengembalikan `0`. Jika proses sudah di-trace (gdb, strace), syscall gagal dan mengembalikan `-1` (`EPERM`). Bool `anti_debug` menjadi 1, lalu **hanya byte pertama** output di-XOR dengan 1. Akibatnya flag yang benar pun ditolak saat dianalisis dengan debugger.

Ini terlihat pada bukti:

```text
$ strace -f -e trace=ptrace ./reverse/Hard_03_Castaway/castaway < writeups/assets/castaway/castaway_in.txt
ptrace(PTRACE_TRACEME)                  = -1 EPERM (Operation not permitted)
flag> Nope.
```

Sedangkan eksekusi normal:

```text
$ cat writeups/assets/castaway/castaway_in.txt | ./reverse/Hard_03_Castaway/castaway
flag> Access granted.
```

Anti-debug ini mudah dilewati: patch `xor` di `0x154c`, atau paksa bool = 0, atau jalankan tanpa debugger. Untuk solver, kita cukup menganggap `anti_debug = 0`.

### 2.3 Fungsi rotate `0x1249`

Fungsi kecil `rol8(byte, count)`:

```asm
1249:  endbr64
124d:  push   rbp
1251:  mov    eax,edi              ; byte
1253:  mov    DWORD PTR [rbp-0x8],esi ; count
1256:  mov    BYTE PTR [rbp-0x4],al
1259:  and    DWORD PTR [rbp-0x8],0x7 ; count & 7
125d:  movzx  edx,BYTE PTR [rbp-0x4]
1261:  mov    eax,DWORD PTR [rbp-0x8]
1266:  shl    edx,cl              ; byte << count
126a:  mov    esi,eax
126c:  movzx  edx,BYTE PTR [rbp-0x4]
1270:  mov    eax,DWORD PTR [rbp-0x8]
1273:  neg    eax
1275:  and    eax,0x7
127a:  sar    edx,cl              ; byte >> (8-count)
127e:  or     eax,esi
1281:  ret
```

Jadi:

```text
rol8(x, n) = ((x << (n & 7)) | (x >> ((8 - n) & 7))) & 0xff
```

### 2.4 Fungsi transform `0x1282`

Fungsi ini menerima `(input, len, output)` dan menjalankan state machine. Variabel lokal:

- `[rbp-0x18]` = input pointer
- `[rbp-0x20]` = len
- `[rbp-0x28]` = output pointer
- `[rbp-0xe]` = key (awal `0xa5`)
- `[rbp-0x8]` = i
- `[rbp-0xc]` = state (awal 0)

Inisialisasi:

```asm
129a:  mov    BYTE PTR [rbp-0xe],0xa5  ; key = 0xa5
129e:  mov    QWORD PTR [rbp-0x8],0x0  ; i = 0
12a6:  mov    DWORD PTR [rbp-0xc],0x0  ; state = 0
12ad:  jmp    141f
```

Dispatch state:

```asm
12b2:  cmp    DWORD PTR [rbp-0xc],0x32 ; state == 50?
12b6:  je     1407
12bc:  cmp    DWORD PTR [rbp-0xc],0x32
12c0:  jg     1417
12c6:  cmp    DWORD PTR [rbp-0xc],0x2  ; state == 2?
12ca:  je     13e0
12d0:  cmp    DWORD PTR [rbp-0xc],0x2
12d4:  jg     1417
12da:  cmp    DWORD PTR [rbp-0xc],0x0  ; state 0?
12de:  je     12eb
12e0:  cmp    DWORD PTR [rbp-0xc],0x1  ; state 1?
12e4:  je     12f7
12e6:  jmp    1417
```

State machine:

| State | Aksi | Transisi |
|---|---|---|
| `0` | Tidak ada | `1` |
| `1` | Jika `i < len`, proses byte ke-`i`; jika tidak, selesai | `2` setelah proses, `0x63` jika `i >= len` |
| `2` | Opaque predicate `(i*i) & 3 == 2` | `0x32` jika true, `1` jika false |
| `0x32` | `output[0] = 0xff`, selesai | `0x63` |
| `0x63` | Terminasi loop | — |

State `0x32` **tidak pernah tercapai** karena untuk semua integer `i`, `i² mod 4` hanya `0` atau `1`, tidak pernah `2`.

```asm
13e0:  mov    rax,QWORD PTR [rbp-0x8]
13e4:  mov    edx,eax
13ea:  imul   eax,edx             ; i*i
13ed:  and    eax,0x3
13f0:  cmp    eax,0x2
13f3:  jne    13fe                 ; hampir selalu ke sini
13f5:  mov    DWORD PTR [rbp-0xc],0x32
13fc:  jmp    141f
13fe:  mov    DWORD PTR [rbp-0xc],0x1
```

### 2.5 Transformasi per byte

Saat state 1 dan `i < len`:

```asm
12f7:  mov    rax,QWORD PTR [rbp-0x8]
12fb:  cmp    rax,QWORD PTR [rbp-0x20] ; i >= len?
12ff:  jae    13d7
1305:  mov    rdx,QWORD PTR [rbp-0x18]
1309:  mov    rax,QWORD PTR [rbp-0x8]
130d:  add    rax,rdx
1310:  movzx  eax,BYTE PTR [rax]     ; p = input[i]
1313:  xor    al,BYTE PTR [rbp-0xe]  ; p ^= key
1316:  mov    BYTE PTR [rbp-0xd],al ; c

; hitung (i % 7) + 1 dengan magic 0x2492492492492493
1319:  mov    rcx,QWORD PTR [rbp-0x8]
131d:  movabs rdx,0x2492492492492493
132a:  mul    rdx
1330:  sub    rax,rdx
1333:  shr    rax,1
1336:  add    rax,rdx
1339:  shr    rax,0x2
133d:  mov    rdx,rax
1340:  shl    rdx,0x3
1344:  sub    rdx,rax
1347:  mov    rax,rcx
134a:  sub    rax,rdx                ; rax = i % 7
134d:  lea    edx,[rax+0x1]          ; (i % 7) + 1
1350:  movzx  eax,BYTE PTR [rbp-0xd]
1354:  mov    esi,edx
1356:  mov    edi,eax
1358:  call   1249 <rol8>
135d:  mov    BYTE PTR [rbp-0xd],al

; tambah sbox16[i & 0xf]
1360:  mov    rax,QWORD PTR [rbp-0x8]
1364:  and    eax,0xf
136a:  lea    rax,[rip+0xdaf]        # 2120
1371:  movzx  eax,BYTE PTR [rdx+rax*1]
1375:  add    BYTE PTR [rbp-0xd],al

; substitusi sbox256[c]
1378:  movzx  eax,BYTE PTR [rbp-0xd]
137e:  lea    rdx,[rip+0xc9b]        # 2020
1385:  movzx  eax,BYTE PTR [rax+rdx*1]
1389:  mov    BYTE PTR [rbp-0xd],al

; xor (i * 0x2f)
138c:  mov    rax,QWORD PTR [rbp-0x8]
1390:  mov    edx,0x2f
1395:  imul   eax,edx
1398:  xor    BYTE PTR [rbp-0xd],al

; output[i] = c
139b:  mov    rdx,QWORD PTR [rbp-0x28]
139f:  mov    rax,QWORD PTR [rbp-0x8]
13a3:  add    rdx,rax
13a6:  movzx  eax,BYTE PTR [rbp-0xd]
13aa:  mov    BYTE PTR [rdx],al

; key = (i + c - 125*key) & 0xff
13ac:  movzx  eax,BYTE PTR [rbp-0xe]
13b0:  mov    edx,0xffffff83       ; -125
13b5:  imul   eax,edx
13ba:  movzx  eax,BYTE PTR [rbp-0xd]
13be:  add    edx,eax
13c0:  mov    rax,QWORD PTR [rbp-0x8]
13c4:  add    eax,edx
13c6:  mov    BYTE PTR [rbp-0xe],al ; key baru

13c9:  add    QWORD PTR [rbp-0x8],0x1
13ce:  mov    DWORD PTR [rbp-0xc],0x2
```

Rumus lengkap untuk byte ke-`i` (semua modulo 256):

```text
c = p_i XOR key
c = rol8(c, (i % 7) + 1)
c = c + sbox16[i & 0xf]
c = sbox256[c]
c = c XOR ((i * 0x2f) & 0xff)
out[i] = c
key = i + c - 125 * key
```

`key` awal `0xa5`. Perhatikan bahwa update key memakai `c` (output byte), bukan `p`. Artinya urutan key hanya bergantung pada ciphertext, sehingga bisa dipulihkan dari ciphertext saja.

### 2.6 Data di `.rodata`

```text
Contents of section .rodata:
 2020 0addef13 168cfbf9 2208b971 039d27c3  ........"..q..'.
 ...
 2120 dc5ac5d4 1cd2bb6b 825c9af1 d19676bd  .Z.....k.....v.
 2130 00000000 00000000 00000000 00000000
 2140 d554ada8 41e3e679 f6bf13d0 1d319dd7  .T..A..y.....1..
 2150 2db7cd6e a9c8e8a4 957bcacb b55f16f0  -..n.....{..._..
 2160 362681c3 2cfb9b74 666c6167 3e20000d  6&..,..tflag> ..
 2170 0a004e6f 70652e00 41636365 73732067  ..Nope..Access g
 2180 72616e74 65642e00                    ranted..
```

Alamat yang dipakai:

- `0x2020` — S-box 256 byte.
- `0x2120` — S-box 16 byte.
- `0x2140` — ciphertext 40 byte.
- `0x2168` — string `"flag> "`.
- `0x2172` — string `"Nope."`.
- `0x2178` — string `"Access granted."`.

Ciphertext:

```text
d5 54 ad a8 41 e3 e6 79 f6 bf 13 d0 1d 31 9d d7
2d b7 cd 6e a9 c8 e8 a4 95 7b ca cb b5 5f 16 f0
36 26 81 c3 2c fb 9b 74
```
