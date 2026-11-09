# Hard Feistel — Analisis

[← Overview](44-hard-feistel.md) · [Index](index.md)

## 2.3 Fungsi ronde

```asm
1190:  mov    ebp,DWORD PTR [rcx]   ; key ronde berikutnya
1192:  mov    esi,ebx               ; new L = R
1194:  add    rcx,0x4
1198:  mov    ebx,eax               ; new R = hasil F
119a:  imul   eax,ebx,0x9e3779b1    ; R * 0x9e3779b1 (32-bit)
11a0:  mov    edx,ebp
11a2:  shl    edx,0x8
11a5:  add    edx,ebp               ; K * 257
11a7:  shr    eax,0x5               ; (R * C) >> 5
11aa:  xor    eax,edx               ; XOR (K * 257)
11ac:  movzx  eax,ax                ; mask 16-bit
11af:  xor    eax,esi               ; XOR L
11b1:  cmp    r8,rcx
11b4:  jne    1190
```

Secara matematis:

```text
F(R, K) = (((R * 0x9e3779b1) mod 2^32) >> 5) XOR ((K * 257) & 0xffff)
round:  (L, R) = (R, L XOR F(R, K_i))
```

`K * 257` sama dengan `K + (K << 8)`, yaitu menduplikasi byte rendah key ke dua byte (karena key hanya 8-bit). Mask 16-bit dilakukan setelah XOR.

## 2.4 Jadwal round key

Dari `.rodata` `0x2060` (64 byte):

```text
Contents of section .rodata:
 2060 5a000000 79000000 98000000 b7000000  Z...y...........
 2070 d6000000 f5000000 14000000 33000000  ............3...
 2080 52000000 71000000 90000000 af000000  R...q...........
 2090 ce000000 ed000000 0c000000 2b000000  ............+...
```

16 key 16-bit:

```text
0x005a 0x0079 0x0098 0x00b7 0x00d6 0x00f5 0x0014 0x0033
0x0052 0x0071 0x0090 0x00af 0x00ce 0x00ed 0x000c 0x002b
```

Pola: `K_i = (0x5a + 0x1f * i) mod 0x100`. Ini jadwal sederhana yang disebut di deskripsi. Meskipun disimpan sebagai dword, hanya 16 bit rendah yang dipakai.
