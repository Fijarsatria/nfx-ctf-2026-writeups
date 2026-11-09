# Hard Feistel — Analisis

[← Overview](44-hard-feistel.md) · [Index](index.md)

### 2.1 Main dan layout

Main ada di `0x10e0`.

```asm
1102:  cmp    edi,0x1
1105:  jle    1236                   ; usage
110b:  mov    rbp,QWORD PTR [rsi+0x8] ; argv[1]
110f:  call   10a0 <strlen@plt>
1117:  mov    rdx,rax
111a:  cmp    rax,0x27               ; 39 byte
111e:  jne    11f4                   ; Wrong!
1124:  lea    rsi,[rsp+0x20]
1129:  mov    r8,rsp
112c:  mov    ecx,0x38              ; zero 224 byte
1136:  lea    r9,[rsp+0x100]         ; buffer output
113e:  lea    r11,[rsp+0x28]         ; akhir input (40 byte)
1143:  mov    rsi,rbp
1146:  rep stos DWORD PTR es:[rdi],eax
114b:  mov    rdi,r8
114e:  mov    rcx,rdx
1151:  rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]  ; copy 39 byte
```

Input 39 byte disalin ke `[rsp]`, sisa buffer sudah di-zero, sehingga blok terakhir (byte ke-40) bernilai `0x00`. Loop memproses `[rsp]` sampai `[rsp+0x28)`, yaitu **10 blok × 4 byte = 40 byte**.

### 2.2 Memuat blok dan round key

```asm
1156:  lea    r8,[rip+0xf43]        # 20a0  (akhir array key)
1160:  movzx  esi,BYTE PTR [rdi]    ; byte 0
1163:  movzx  eax,BYTE PTR [rdi+1]  ; byte 1
1167:  lea    rcx,[rip+0xef6]        # 2064 (key ke-1)
116e:  mov    ebp,0x5a               ; key ke-0
1173:  movzx  ebx,BYTE PTR [rdi+2]  ; byte 2
1177:  shl    esi,0x8
117a:  or     esi,eax                ; L = (b0 << 8) | b1
117c:  movzx  eax,BYTE PTR [rdi+3]  ; byte 3
1180:  shl    ebx,0x8
1183:  or     ebx,eax                ; R = (b2 << 8) | b3
```

Jadi blok 4 byte dibaca **big-endian**: `L = b0b1`, `R = b2b3`.

Round key disimpan sebagai 16 dword di `0x2060`, tetapi nilainya 16-bit. Key pertama `0x5a` di-load langsung, sisanya dibaca dari `0x2064`, `0x2068`, ..., `0x209c`.

### 2.3 Fungsi ronde

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

### 2.4 Jadwal round key

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

### 2.5 Serialisasi output

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

### 2.6 Ciphertext

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

### 2.7 Dekripsi Feistel

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
