# Castaway — Recon

[← Overview](43-castaway.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Kesatria Baja Ringan**
>
> Diberikan sebuah binary mandiri yang membaca calon flag dari stdin. Program memvalidasi input melalui state machine kecil dengan opaque predicate, transformasi per-byte yang melibatkan state, S-box, dan key, serta pengecekan anti-debug menggunakan `ptrace`. Analisis program dan temukan input yang tepat agar lolos validasi internalnya.
>
> Format: `NFX{...}`

Deskripsi menyebut semua komponen penting: stdin, state machine, opaque predicate, S-box, key, dan `ptrace`. Tantangannya adalah memetakan alur state dan membalik transformasi yang bergantung pada state.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 | MD5 |
|---|---|---|---|
| `reverse/Hard_03_Castaway/castaway` | 14.472 byte | `6ca0a8f8e50b77f7dc666cf1b7a486f1a12df1008c478cbbe6615245bca776d1` | `a77f3296127692a05ced8583fa73f480` |

Catatan operasional: file asli tidak executable; `chmod +x` dilakukan agar bisa dijalankan untuk verifikasi. Isi binary tidak berubah (hash tetap).

### 1.3 Environment

- Linux x86-64; tools: `file`, `readelf`, `objdump`, `strings`, `gdb`, `strace`, `python3`, `pyelftools`, `pwntools`.
- `checksec` standalone tidak tersedia; memakai `ELF.checksec()`.
- Binary membaca input dari stdin dan mencetak prompt `flag> `.

### 1.4 Triage awal

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

### 1.5 Perintah akuisisi bukti

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
