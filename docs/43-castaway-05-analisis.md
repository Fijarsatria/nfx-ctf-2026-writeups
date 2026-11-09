# Castaway — Analisis

[← Overview](43-castaway.md) · [Index](index.md)

## 2.2 Anti-debug

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

## 2.3 Fungsi rotate `0x1249`

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
