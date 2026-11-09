# Hard Feistel — Perintah akuisisi bukti

[← Overview](44-hard-feistel.md) · [Index](index.md)

## 1.5 Perintah akuisisi bukti

```bash
mkdir -p writeups/assets/hard-feistel
BIN=reverse/Hard_02_Feistel/hard_feistel
file "$BIN"                                  >  writeups/assets/hard-feistel/01-identitas.txt
sha256sum "$BIN"                             >> writeups/assets/hard-feistel/01-identitas.txt
md5sum "$BIN"                                >> writeups/assets/hard-feistel/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  writeups/assets/hard-feistel/02-readelf.txt
strings -n 4 "$BIN"                          >  writeups/assets/hard-feistel/03-strings.txt
objdump -d -Mintel "$BIN"                    >  writeups/assets/hard-feistel/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  writeups/assets/hard-feistel/05-rodata-data-hexdump.txt
objdump -s -j .data "$BIN"                   >> writeups/assets/hard-feistel/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  writeups/assets/hard-feistel/08-checksec.txt
python3 writeups/assets/hard-feistel/solve_feistel.py \
                                             | tee writeups/assets/hard-feistel/06-solver-output.txt
```
