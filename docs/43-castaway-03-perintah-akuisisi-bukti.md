# Castaway — Perintah akuisisi bukti

[← Overview](43-castaway.md) · [Index](index.md)

## 1.5 Perintah akuisisi bukti

```bash
mkdir -p writeups/assets/castaway
BIN=reverse/Hard_03_Castaway/castaway
file "$BIN"                                  >  writeups/assets/castaway/01-identitas.txt
sha256sum "$BIN"                             >> writeups/assets/castaway/01-identitas.txt
md5sum "$BIN"                                >> writeups/assets/castaway/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  writeups/assets/castaway/02-readelf.txt
strings -n 4 "$BIN"                          >  writeups/assets/castaway/03-strings.txt
objdump -d -Mintel "$BIN"                    >  writeups/assets/castaway/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  writeups/assets/castaway/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  writeups/assets/castaway/08-checksec.txt
python3 writeups/assets/castaway/solve_castaway.py \
                                             | tee writeups/assets/castaway/06-solver-output.txt
```
