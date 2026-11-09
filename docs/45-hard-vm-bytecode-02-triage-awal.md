# Hard VM Bytecode — Triage awal

[← Overview](45-hard-vm-bytecode.md) · [Index](index.md)

## 1.4 Triage awal

```text
$ file reverse/Hard_01_VM_Bytecode/hard_vm
reverse/Hard_01_VM_Bytecode/hard_vm: ELF 64-bit LSB pie executable, x86-64,
version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=b0c9e6c30f4121196fc85a998419383dea6cf0e7, for GNU/Linux 3.2.0, stripped
```

```text
$ sha256sum reverse/Hard_01_VM_Bytecode/hard_vm
54cc69e2f8213ccb685818c3a371a08c87caf9d487d5a47b157ab3bcf7f93697  reverse/Hard_01_VM_Bytecode/hard_vm

$ md5sum reverse/Hard_01_VM_Bytecode/hard_vm
7b33fd7a143dc9123434672e26c50d3d  reverse/Hard_01_VM_Bytecode/hard_vm

$ stat -c '%s bytes' reverse/Hard_01_VM_Bytecode/hard_vm
14472 bytes
```

```text
$ python3 -c "from pwn import *; print(ELF('reverse/Hard_01_VM_Bytecode/hard_vm').checksec())"
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
FORTIFY:    Enabled
SHSTK:      Enabled
IBT:        Enabled
```

```text
$ strings -n 4 reverse/Hard_01_VM_Bytecode/hard_vm
...
Pemakaian: %s <flag>
Wrong!
Correct! Bytecode VM berhasil dibongkar.
...
```

**Temuan:** tidak ada string key/ciphertext yang jelas. Pesan sukses menyebut “Bytecode VM”. Ini konsisten dengan adanya array bytecode yang diinterpretasikan. Panjang input dicek `== 0x21` (33 byte) di `0x10f7`.

Menjalankan binary:

```text
$ ./reverse/Hard_01_VM_Bytecode/hard_vm 'NFX{wrong}'
Wrong!
```
