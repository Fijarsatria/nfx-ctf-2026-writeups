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

Isi `flags/reverse/Hard_01_VM_Bytecode.txt` identik. **Status: `VERIFIED platform`.** Flag sudah dicek ulang ke platform pada 2026-11-09 (`Correct, but already solved.`); verifikasi lokal tetap dilakukan terhadap binary dan file flag.

## Flag

`NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}`

**Status:** `VERIFIED`

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
