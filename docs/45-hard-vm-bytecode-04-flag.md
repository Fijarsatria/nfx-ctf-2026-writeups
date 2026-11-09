# Hard VM Bytecode — Flag & Verifikasi

[← Overview](45-hard-vm-bytecode.md) · [Index](index.md)

```text
NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}
```

Cek file flag lokal:

```text
$ cat flags/reverse/Hard_01_VM_Bytecode.txt
NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}
```

Verifikasi:

```text
$ ./reverse/Hard_01_VM_Bytecode/hard_vm 'NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}'
Correct! Bytecode VM berhasil dibongkar.
rc=0

$ ./reverse/Hard_01_VM_Bytecode/hard_vm 'NFX{wrong}'
Wrong!
rc=1
```

Isi `flags/reverse/Hard_01_VM_Bytecode.txt` identik. **Status: `verified local`.** Flag tidak disubmit ke platform; verifikasi dilakukan sepenuhnya terhadap binary dan file flag lokal.

## Flag

`NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}`

**Status:** `VERIFIED`
