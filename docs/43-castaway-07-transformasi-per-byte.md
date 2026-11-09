# Castaway — Transformasi per byte

[← Overview](43-castaway.md) · [Index](index.md)

## 2.5 Transformasi per byte

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
