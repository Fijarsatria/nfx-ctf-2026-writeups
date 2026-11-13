# Hard VM Bytecode — Perintah akuisisi bukti

[← Overview](45-hard-vm-bytecode.md) · [Index](index.md)

> **Langkah 3/13 — Perintah akuisisi bukti.** Perintah akuisisi bukti
>
> **Titik penting:** file "$BIN" > docs/assets/hard-vm-bytecode/01-identitas.txt · strings -n 4 "$BIN" > docs/assets/hard-vm-bytecode/03-strings.txt · objdump -d -Mintel "$BIN" > docs/assets/hard-vm-bytecode/04-disasm.txt
>
> **Berikutnya:** [Main dan layout](45-hard-vm-bytecode-04-main-dan-layout.md)

## 1.5 Perintah akuisisi bukti

```bash
mkdir -p docs/assets/hard-vm-bytecode
BIN=reverse/Hard_01_VM_Bytecode/hard_vm
file "$BIN"                                  >  docs/assets/hard-vm-bytecode/01-identitas.txt
sha256sum "$BIN"                             >> docs/assets/hard-vm-bytecode/01-identitas.txt
md5sum "$BIN"                                >> docs/assets/hard-vm-bytecode/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  docs/assets/hard-vm-bytecode/02-readelf.txt
strings -n 4 "$BIN"                          >  docs/assets/hard-vm-bytecode/03-strings.txt
objdump -d -Mintel "$BIN"                    >  docs/assets/hard-vm-bytecode/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  docs/assets/hard-vm-bytecode/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  docs/assets/hard-vm-bytecode/08-checksec.txt
python3 docs/assets/hard-vm-bytecode/solve_vm.py \
                                             | tee docs/assets/hard-vm-bytecode/06-solver-output.txt
```

### Evidence langkah ini

![term-01-identitas.png](assets/hard-vm-bytecode/term-01-identitas.png)

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

![term-08-checksec.png](assets/hard-vm-bytecode/term-08-checksec.png)

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-identitas.txt`](assets/hard-vm-bytecode/01-identitas.txt)
- [`08-checksec.txt`](assets/hard-vm-bytecode/08-checksec.txt)
