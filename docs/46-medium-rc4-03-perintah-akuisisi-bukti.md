# Medium RC4 — Perintah akuisisi bukti

[← Overview](46-medium-rc4.md) · [Index](index.md)

## 1.5 Perintah akuisisi bukti

```bash
mkdir -p writeups/assets/medium-rc4
BIN=reverse/Medium_01_RC4/medium_rc4
file "$BIN"                                  >  writeups/assets/medium-rc4/01-identitas.txt
sha256sum "$BIN"                             >> writeups/assets/medium-rc4/01-identitas.txt
md5sum "$BIN"                                >> writeups/assets/medium-rc4/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  writeups/assets/medium-rc4/02-readelf.txt
strings -n 4 "$BIN"                          >  writeups/assets/medium-rc4/03-strings.txt
objdump -d -Mintel "$BIN"                    >  writeups/assets/medium-rc4/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  writeups/assets/medium-rc4/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  writeups/assets/medium-rc4/08-checksec.txt
python3 writeups/assets/medium-rc4/solve_rc4.py \
                                             | tee writeups/assets/medium-rc4/06-solver-output.txt
```
