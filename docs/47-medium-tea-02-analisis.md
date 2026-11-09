# Medium TEA — Analisis

[← Overview](47-medium-tea.md) · [Index](index.md)

### 2.1 Alur utama

Main ada di `0x10c0`. Bagian pentingnya:

```asm
10df:  cmp    edi,0x1
10e2:  jle    11f5                  ; tidak ada argumen -> usage
10e8:  mov    rbp,QWORD PTR [rsi+0x8] ; argv[1]
10ef:  call   1090 <strlen@plt>
10f4:  cmp    rax,0x28              ; harus 40 byte
10f8:  je     112b
```

Lalu:

```asm
112b:  lea    r8,[rsp+0x28]         ; akhir area output/padding
1130:  mov    rdx,rsp
1133:  mov    ecx,0x36              ; zero 0x36 dword = 216 byte
113a:  mov    rdi,r8
1140:  lea    r10,[rip+0xef9]       # 2040  ciphertext
1147:  rep stos DWORD PTR es:[rdi],eax
1149:  mov    ecx,0xa               ; copy 10 dword = 40 byte input
114e:  mov    rdi,rdx
1151:  rep movs DWORD PTR es:[rdi],DWORD PTR ds:[rsi]
```

Input 40 byte disalin ke `[rsp]`, lalu diproses 5 blok × 8 byte. Setiap blok diambil sebagai qword little-endian:

```asm
1156:  mov    rdx,QWORD PTR [rdi]   ; 8 byte blok
1159:  xor    esi,esi               ; sum = 0
115b:  mov    ecx,edx               ; v0 = low 32 bit
115d:  shr    rdx,0x20              ; v1 = high 32 bit
```

### 2.2 Round function TEA yang dimodifikasi

TEA standar:

```text
sum += delta
v0 += ((v1 << 4) + k0) XOR (v1 + sum) XOR ((v1 >> 5) + k1)
v1 += ((v0 << 4) + k2) XOR (v0 + sum) XOR ((v0 >> 5) + k3)
```

Binary melakukan hal yang sama, tetapi dengan konstanta berbeda:

```asm
1168:  mov    eax,edx              ; v1
116a:  mov    r9d,edx
116d:  sub    esi,0x61c88647       ; sum += 0x9e3779b9
1173:  shl    eax,0x4              ; v1 << 4
1176:  shr    r9d,0x5              ; v1 >> 5
117a:  sub    r9d,0x35014542       ; + 0xcafebabe
1181:  add    eax,0x1337beef       ; + k0
1186:  xor    eax,r9d              ; XOR (v1>>5)+k1
1189:  lea    r9d,[rsi+rdx*1]      ; sum + v1
118d:  xor    eax,r9d
1190:  add    ecx,eax              ; v0 += ...
1192:  mov    eax,ecx              ; v0
1194:  mov    r9d,ecx
1197:  shl    eax,0x4              ; v0 << 4
119a:  shr    r9d,0x5              ; v0 >> 5
119e:  add    r9d,0xbadf00d        ; + k3
11a5:  sub    eax,0x21523f22       ; + 0xdeadc0de = k2
11aa:  xor    eax,r9d
11ad:  lea    r9d,[rsi+rcx*1]      ; sum + v0
11b1:  xor    eax,r9d
11b4:  add    edx,eax              ; v1 += ...
11b6:  cmp    esi,0xc6ef3720       ; sudah 32 ronde?
11bc:  jne    1168
```

Konstanta yang terbaca:

| Parameter | Nilai | Bukti |
|---|---|---|
| `delta` | `0x9e3779b9` | `sub esi,0x61c88647` = `add esi,0x9e3779b9` (two's complement) |
| `k0` | `0x1337beef` | `add eax,0x1337beef` |
| `k1` | `0xcafebabe` | `sub r9d,0x35014542` = `add r9d,0xcafebabe` |
| `k2` | `0xdeadc0de` | `sub eax,0x21523f22` = `add eax,0xdeadc0de` |
| `k3` | `0x0badf00d` | `add r9d,0xbadf00d` |
| Jumlah ronde | 32 | loop sampai `sum == 0xc6ef3720` |
| `sum` akhir | `0xc6ef3720` | `32 * 0x9e3779b9 mod 2^32` |

Verifikasi `sum` akhir:

```text
0x9e3779b9 * 32 = 0x13c6ef3720
0x13c6ef3720 mod 2^32 = 0xc6ef3720
```

Setelah 32 ronde, binary membandingkan `v0` dan `v1` hasil enkripsi dengan ciphertext:

```asm
11be:  cmp    DWORD PTR [r10],ecx       ; v0 == ct[0]
11c1:  jne    10fa                      ; Wrong!
11c7:  cmp    DWORD PTR [r10+0x4],edx   ; v1 == ct[1]
11cb:  jne    10fa
11d1:  add    rdi,0x8
11d5:  add    r10,0x8
11d9:  cmp    r8,rdi                    ; 5 blok
11dc:  jne    1156
```

### 2.3 Ciphertext

Dari `lea r10,[rip+0xef9] # 2040` dan panjang 40 byte:

```text
Contents of section .rodata:
 2040 d08b910e 9e3d818e eadab483 cfc8fd8a  .....=..........
 2050 083b4483 6a130476 724d7205 905af697  .;D.j..vrMr..Z..
 2060 db1395e7 c74c5385                    .....LS.
```

Ciphertext (40 byte):

```text
d0 8b 91 0e 9e 3d 81 8e ea da b4 83 cf c8 fd 8a
08 3b 44 83 6a 13 04 76 72 4d 72 05 90 5a f6 97
db 13 95 e7 c7 4c 53 85
```

### 2.4 Dekripsi TEA

Karena TEA adalah Feistel-like cipher yang invertibel, dekripsi dilakukan dengan membalik urutan operasi:

```text
sum = 0xc6ef3720
for 32 kali:
    v1 -= ((v0 << 4) + k2) XOR (v0 + sum) XOR ((v0 >> 5) + k3)
    v0 -= ((v1 << 4) + k0) XOR (v1 + sum) XOR ((v1 >> 5) + k1)
    sum -= delta
```

Semua operasi dilakukan modulo `2^32`. Blok dibaca/ditulis **little-endian** karena binary memakai `mov ecx, edx` (low 32 bit) dan `shr rdx, 0x20` (high 32 bit) dari qword yang dimuat little-endian.
