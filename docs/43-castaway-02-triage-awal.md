# Castaway — Triage awal

[← Overview](43-castaway.md) · [Index](index.md)

## 1.4 Triage awal

```text
$ file reverse/Hard_03_Castaway/castaway
reverse/Hard_03_Castaway/castaway: ELF 64-bit LSB pie executable, x86-64,
version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=ecc3e55a90532bddbb7e3603420f488342d3e632, for GNU/Linux 3.2.0, stripped
```

```text
$ sha256sum reverse/Hard_03_Castaway/castaway
6ca0a8f8e50b77f7dc666cf1b7a486f1a12df1008c478cbbe6615245bca776d1  reverse/Hard_03_Castaway/castaway

$ md5sum reverse/Hard_03_Castaway/castaway
a77f3296127692a05ced8583fa73f480  reverse/Hard_03_Castaway/castaway

$ stat -c '%s bytes' reverse/Hard_03_Castaway/castaway
14472 bytes
```

```text
$ python3 -c "from pwn import *; print(ELF('reverse/Hard_03_Castaway/castaway').checksec())"
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
FORTIFY:    Enabled
SHSTK:      Enabled
IBT:        Enabled
```

```text
$ strings -n 4 reverse/Hard_03_Castaway/castaway
...
fgets
strcspn
ptrace
stdout
fflush
strlen
memcmp
stdin
...
flag>
Nope.
Access granted.
...
```

**Temuan:**

1. Import `ptrace` → ada anti-debug.
2. Import `fgets`, `strcspn`, `stdin` → input dari stdin, newline di-strip.
3. String `flag> `, `Nope.`, `Access granted.`.
4. Binary stripped, PIE, canary, full RELRO, NX. Fungsi transformasi tampak dikompilasi tanpa optimasi (banyak akses `[rbp-...]`), sehingga mudah dibaca.

Menjalankan binary:

```text
$ printf 'NFX{wrong}\n' | ./reverse/Hard_03_Castaway/castaway
flag> Nope.
```
