# Hard VM Bytecode — Analisis

[← Overview](45-hard-vm-bytecode.md) · [Index](index.md)

### 2.1 Main dan layout

Main ada di `0x10c0`. Bagian awal:

```asm
10df:  cmp    edi,0x1
10e2:  jle    11dc                   ; usage
10e8:  mov    rbp,QWORD PTR [rsi+0x8] ; argv[1]
10ef:  call   1090 <strlen@plt>
10f4:  mov    rdx,rax
10f7:  cmp    rax,0x21               ; 33 byte
10fb:  jne    1170                   ; Wrong!
```

Lalu:

```asm
10fd:  lea    rsi,[rsp+0x30]         ; buffer state
1102:  mov    ecx,0x38              ; zero 0x38 dword = 224 byte
1109:  mov    DWORD PTR [rsp+0xc],0x0
1111:  mov    rdi,rsi
1114:  lea    r8,[rsp+0x10]          ; buffer input
1119:  mov    rsi,rbp
111c:  rep stos DWORD PTR es:[rdi],eax
111e:  mov    rcx,rdx
1121:  lea    rdx,[rip+0xf58]        ; bytecode @ 0x2080
1128:  mov    rdi,r8
112b:  rep movs BYTE PTR es:[rdi],BYTE PTR ds:[rsi]  ; copy 33 byte input
112d:  lea    r8,[rdx+0x1f2]         ; akhir bytecode = 0x2080 + 498
1134:  lea    rdi,[rip+0xf25]        ; dispatch table @ 0x2060
```

Layout stack yang relevan:

- `[rsp+0x0c]` — register/state byte (hanya dword pertama di-zero).
- `[rsp+0x10]` — input flag 33 byte.
- `[rsp+0x30]` — buffer tambahan yang di-zero (tidak dipakai sebagai register oleh bytecode ini).

### 2.2 Format instruksi

Loop mengambil **3 byte** per instruksi:

```asm
113b:  movzx  eax,BYTE PTR [rdx]      ; opcode
113e:  movzx  esi,BYTE PTR [rdx+0x1]  ; reg / index
1142:  movzx  ecx,BYTE PTR [rdx+0x2]  ; immediate
1146:  cmp    al,0x5
1148:  ja     11c8                    ; opcode > 5 -> cek 0xff
114a:  test   al,al
114c:  je     1170                    ; opcode 0 -> gagal
1152:  movsxd rax,DWORD PTR [rdi+rax*4] ; dispatch table
1156:  add    rax,rdi
1159:  notrack jmp rax
```

Dispatch table berada di `.rodata` `0x2060`:

```text
Contents of section .rodata:
 2060 56f1ffff 56f1ffff 48f1ffff fcf0ffff  V...V...H.......
 2070 3df1ffff 4ef1ffff 00000000 00000000  =...N...........
```

Setiap entry adalah offset 32-bit bertanda relatif terhadap `rdi = 0x2060`:

| Index | Raw | Target | Handler |
|---|---|---|---|
| 0 | `0xfffff156` | `0x11b6` | LOAD (tidak terpakai; opcode 0 langsung gagal) |
| 1 | `0xfffff156` | `0x11b6` | LOAD |
| 2 | `0xfffff148` | `0x11a8` | XOR |
| 3 | `0xfffff0fc` | `0x115c` | ADD |
| 4 | `0xfffff13d` | `0x119d` | ROL |
| 5 | `0xfffff14e` | `0x11ae` | CMP |

Perhitungan contoh: `0xfffff148` sebagai signed = `-0xeb8`; `0x2060 - 0xeb8 = 0x11a8`.

### 2.3 Semantik tiap opcode

```asm
; ADD: state[reg] += imm
115c:  add    BYTE PTR [rsp+rsi*1+0xc],cl
1160:  add    rdx,0x3
1164:  cmp    rdx,r8
1167:  jne    113b

; ROL: state[reg] = rol8(state[reg], imm & 7)
119d:  and    cl,0x7
11a0:  je     1160                 ; rotasi 0 -> tidak ada perubahan
11a2:  rol    BYTE PTR [rsp+rsi*1+0xc],cl

; XOR: state[reg] ^= imm
11a8:  xor    BYTE PTR [rsp+rsi*1+0xc],cl

; CMP: bandingkan state[reg] dengan imm
11ae:  cmp    BYTE PTR [rsp+rsi*1+0xc],cl
11b2:  je     1160                 ; sama -> lanjut
11b4:  jmp    1170                 ; beda -> Wrong!

; LOAD: state[reg] = input[imm]
11b6:  movzx  eax,BYTE PTR [rsp+rcx*1+0x10]
11bb:  mov    BYTE PTR [rsp+rsi*1+0xc],al

; 0xff -> sukses
11c8:  cmp    al,0xff
11ca:  jne    1170
11cc:  lea    rdi,[rip+0xe55]      # 2028 "Correct! Bytecode VM berhasil dibongkar."
11d3:  call   1080 <puts@plt>
```

Catatan penting: pada `LOAD`, byte ketiga instruksi adalah **index input**, sedangkan pada opcode lain byte ketiga adalah **immediate**. Pada challenge ini semua instruksi memakai `reg = 0`, tetapi interpreter mendukung register lain karena `reg` dipakai sebagai offset ke `[rsp+reg+0xc]`.

### 2.4 Bytecode

Bytecode 498 byte di `0x2080`. 16 byte pertama:

```text
01 00 00 02 00 5a 03 00 21 04 00 01 05 00 6a 01
```

Dibaca per 3 byte:

```text
01 00 00   LOAD reg0, input[0]
02 00 5a   XOR  reg0, 0x5a
03 00 21   ADD  reg0, 0x21
04 00 01   ROL  reg0, 1
05 00 6a   CMP  reg0, 0x6a
01 00 01   LOAD reg0, input[1]
...
```

Jumlah instruksi: `498 / 3 = 166`. Karena flag 33 karakter dan tiap karakter memakai 5 instruksi, totalnya `33 × 5 = 165`, ditambah satu instruksi terakhir `ff 00 00` (OK). Ini cocok persis.

### 2.5 Membalik transformasi

Untuk karakter ke-`i`, bytecode melakukan:

```text
v = input[i]
v = v XOR xor_i
v = (v + add_i) mod 256
v = rol8(v, rot_i)
assert v == cmp_i
```

Maka inverse-nya:

```text
v = ror8(cmp_i, rot_i)
v = (v - add_i) mod 256
input[i] = v XOR xor_i
```

Dengan `ror8(x, n) = ((x >> n) | (x << (8-n))) & 0xff`.

Contoh karakter pertama dari output solver:

```text
char[0] = ror8(0x6a, 1) - 0x21 ^ 0x5a
        = 0x35 - 0x21 ^ 0x5a
        = 0x14 ^ 0x5a
        = 0x4e = 'N'
```
