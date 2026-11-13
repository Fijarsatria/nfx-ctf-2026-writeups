# Medium RC4 — Perintah akuisisi bukti

[← Overview](46-medium-rc4.md) · [Index](index.md)

> **Langkah 3/11 — Perintah akuisisi bukti.** Perintah akuisisi bukti
>
> **Titik penting:** file "$BIN" > docs/assets/medium-rc4/01-identitas.txt · strings -n 4 "$BIN" > docs/assets/medium-rc4/03-strings.txt · objdump -d -Mintel "$BIN" > docs/assets/medium-rc4/04-disasm.txt
>
> **Berikutnya:** [Peta fungsi `main`](46-medium-rc4-04-peta-fungsi-main.md)

## 1.5 Perintah akuisisi bukti

```bash
mkdir -p docs/assets/medium-rc4
BIN=reverse/Medium_01_RC4/medium_rc4
file "$BIN"                                  >  docs/assets/medium-rc4/01-identitas.txt
sha256sum "$BIN"                             >> docs/assets/medium-rc4/01-identitas.txt
md5sum "$BIN"                                >> docs/assets/medium-rc4/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  docs/assets/medium-rc4/02-readelf.txt
strings -n 4 "$BIN"                          >  docs/assets/medium-rc4/03-strings.txt
objdump -d -Mintel "$BIN"                    >  docs/assets/medium-rc4/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  docs/assets/medium-rc4/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  docs/assets/medium-rc4/08-checksec.txt
python3 docs/assets/medium-rc4/solve_rc4.py \
                                             | tee docs/assets/medium-rc4/06-solver-output.txt
```

### Evidence langkah ini

![term-01-identitas.png](assets/medium-rc4/term-01-identitas.png)

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

![term-08-checksec.png](assets/medium-rc4/term-08-checksec.png)

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-identitas.txt`](assets/medium-rc4/01-identitas.txt)
- [`08-checksec.txt`](assets/medium-rc4/08-checksec.txt)
