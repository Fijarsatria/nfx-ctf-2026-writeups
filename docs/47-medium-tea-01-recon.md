# Medium TEA — Recon

[← Overview](47-medium-tea.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: cypera**
>
> Validator ini memakai TEA 32 ronde dengan kunci 128-bit yang tertanam. Flag dipad dengan nol ke kelipatan 8 byte, lalu setiap blok 64-bit dienkripsi dan dibandingkan dengan ciphertext.
>
> Format: `NFX{...}`

Petunjuknya sangat langsung: TEA, 32 ronde, key 128-bit tertanam, padding nol ke kelipatan 8 byte. Yang perlu dilakukan adalah menemukan key dan ciphertext, lalu membalik TEA.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 | MD5 |
|---|---|---|---|
| `reverse/Medium_02_TEA/medium_tea` | 14.472 byte | `a2b45f299304e0cc64582e0bdc704100b9cb2f4fc4c0f164a8cfd322b01b255a` | `edd25b68f7bb42ab3910e80d3e5304ec` |

Tidak ada source atau file pendamping; hanya satu ELF yang membaca flag dari argumen.

### 1.3 Environment

- Linux x86-64, tools: `file`, `readelf`, `objdump`, `strings`, `gdb`, `python3`, `pyelftools`, `pwntools`.
- `checksec` standalone tidak tersedia; digunakan `ELF.checksec()` dari pwntools.
- Binary dijalankan langsung (`argv[1]`), tanpa service.

### 1.4 Triage awal

```text
$ file reverse/Medium_02_TEA/medium_tea
reverse/Medium_02_TEA/medium_tea: ELF 64-bit LSB pie executable, x86-64,
version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=386b457d168f5fd5279b98b973fd66cb92d791e2, for GNU/Linux 3.2.0, stripped
```

```text
$ sha256sum reverse/Medium_02_TEA/medium_tea
a2b45f299304e0cc64582e0bdc704100b9cb2f4fc4c0f164a8cfd322b01b255a  reverse/Medium_02_TEA/medium_tea

$ md5sum reverse/Medium_02_TEA/medium_tea
edd25b68f7bb42ab3910e80d3e5304ec  reverse/Medium_02_TEA/medium_tea

$ stat -c '%s bytes' reverse/Medium_02_TEA/medium_tea
14472 bytes
```

```text
$ python3 -c "from pwn import *; print(ELF('reverse/Medium_02_TEA/medium_tea').checksec())"
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
FORTIFY:    Enabled
SHSTK:      Enabled
IBT:        Enabled
```

```text
$ strings -n 4 reverse/Medium_02_TEA/medium_tea
...
Pemakaian: %s <flag>
Wrong!
Correct! TEA terpecahkan.
...
```

**Temuan:** binary stripped dan PIE, tetapi tidak menggunakan anti-debug. Pesan sukses menyebut TEA. Tidak ada string key yang terlihat, jadi key harus dicari dari instruksi aritmetika di fungsi utama. Panjang input yang diterima adalah **40 byte** (lihat `cmp rax,0x28`).

Menjalankan binary:

```text
$ ./reverse/Medium_02_TEA/medium_tea 'NFX{wrong}'
Wrong!

$ ./reverse/Medium_02_TEA/medium_tea
Pemakaian: reverse/Medium_02_TEA/medium_tea <flag>
```

### 1.5 Perintah akuisisi bukti

```bash
mkdir -p writeups/assets/medium-tea
BIN=reverse/Medium_02_TEA/medium_tea
file "$BIN"                                  >  writeups/assets/medium-tea/01-identitas.txt
sha256sum "$BIN"                             >> writeups/assets/medium-tea/01-identitas.txt
md5sum "$BIN"                                >> writeups/assets/medium-tea/01-identitas.txt
readelf -hW -lW -SW -dW "$BIN"               >  writeups/assets/medium-tea/02-readelf.txt
strings -n 4 "$BIN"                          >  writeups/assets/medium-tea/03-strings.txt
objdump -d -Mintel "$BIN"                    >  writeups/assets/medium-tea/04-disasm.txt
objdump -s -j .rodata "$BIN"                 >  writeups/assets/medium-tea/05-rodata-data-hexdump.txt
python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \
                                             >  writeups/assets/medium-tea/08-checksec.txt
python3 writeups/assets/medium-tea/solve_tea.py \
                                             | tee writeups/assets/medium-tea/06-solver-output.txt
```
