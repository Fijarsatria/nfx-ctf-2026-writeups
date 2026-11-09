# Hard VM Bytecode — Recon

[← Overview](45-hard-vm-bytecode.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: cypera**
>
> Binary ini bukan validator biasa: ia menjalankan bytecode custom pada VM kecil. Setiap karakter diproses dengan urutan LOAD, XOR, ADD, ROL, lalu CMP. Tugasmu adalah memahami opcode dan membalik transformasinya.
>
> Format: `NFX{...}`

Deskripsi memberi tahu urutan operasi per karakter. Tantangan sebenarnya adalah memetakan opcode ke handler, memahami format instruksi (3 byte), dan menemukan di mana bytecode berada.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 | MD5 |
|---|---|---|---|
| `reverse/Hard_01_VM_Bytecode/hard_vm` | 14.472 byte | `54cc69e2f8213ccb685818c3a371a08c87caf9d487d5a47b157ab3bcf7f93697` | `7b33fd7a143dc9123434672e26c50d3d` |

Catatan operasional: file asli tidak memiliki bit executable (`-rw-r--r--`). Agar bisa dijalankan untuk verifikasi, permission diubah dengan `chmod +x reverse/Hard_01_VM_Bytecode/hard_vm`. Ini tidak mengubah isi binary (hash tetap sama).

### 1.3 Environment

- Linux x86-64; tools: `file`, `readelf`, `objdump`, `strings`, `gdb`, `python3`, `pyelftools`, `pwntools`.
- `checksec` standalone tidak tersedia; memakai `ELF.checksec()`.
- Binary membaca flag dari `argv[1]`.

### 1.4 Triage awal

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

### 1.5 Perintah akuisisi bukti

```bash
mkdir -p writeups/assets/hard-vm-bytecode
BIN=reverse/Hard_01_VM_Bytecode/hard_vm
file "$BIN"                                  >  writeups/assets/hard-vm-bytecode/01-identitas.txt
sha256sum "$BIN"                             >> writeups/assets/hard-vm-bytecode/01-identitas.txt
md5sum "$BIN"                                >> writeups/assets/hard-vm-bytecode/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  writeups/assets/hard-vm-bytecode/02-readelf.txt
strings -n 4 "$BIN"                          >  writeups/assets/hard-vm-bytecode/03-strings.txt
objdump -d -Mintel "$BIN"                    >  writeups/assets/hard-vm-bytecode/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  writeups/assets/hard-vm-bytecode/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  writeups/assets/hard-vm-bytecode/08-checksec.txt
python3 writeups/assets/hard-vm-bytecode/solve_vm.py \
                                             | tee writeups/assets/hard-vm-bytecode/06-solver-output.txt
```
