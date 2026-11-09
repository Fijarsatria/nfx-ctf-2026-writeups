# Hard Feistel — Recon

[← Overview](44-hard-feistel.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: cypera**
>
> Flag dienkripsi dengan jaringan Feistel 16 ronde pada blok 32-bit (L dan R masing-masing 16-bit). Round key diturunkan dari jadwal sederhana dan tertanam di binary. Karena Feistel invertible, dekripsi tidak perlu menginversi fungsi F.
>
> Format: `NFX{...}`

Deskripsi sudah memberi struktur lengkap: 16 ronde, blok 32-bit, key 16-bit. Tantangannya adalah menemukan detail fungsi `F`, jadwal key, dan cara output di-serialisasi.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 | MD5 |
|---|---|---|---|
| `reverse/Hard_02_Feistel/hard_feistel` | 14.528 byte | `2db9a9e254792a497cc71e64be16b35b02665e4d9d553734dff3b9dfc7e21e51` | `9ff3b4313af3f7dceedf5e0443408231` |

Catatan operasional: file asli tidak executable; `chmod +x` dilakukan agar bisa dijalankan untuk verifikasi. Isi binary tidak berubah (hash tetap).

### 1.3 Environment

- Linux x86-64; tools: `file`, `readelf`, `objdump`, `strings`, `gdb`, `python3`, `pyelftools`, `pwntools`.
- `checksec` standalone tidak tersedia; memakai `ELF.checksec()`.
- Binary membaca flag dari `argv[1]`.

### 1.4 Triage awal

```text
$ file reverse/Hard_02_Feistel/hard_feistel
reverse/Hard_02_Feistel/hard_feistel: ELF 64-bit LSB pie executable, x86-64,
version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=07ef75b61feb2bef67ee155a70783c772f166dda, for GNU/Linux 3.2.0, stripped
```

```text
$ sha256sum reverse/Hard_02_Feistel/hard_feistel
2db9a9e254792a497cc71e64be16b35b02665e4d9d553734dff3b9dfc7e21e51  reverse/Hard_02_Feistel/hard_feistel

$ md5sum reverse/Hard_02_Feistel/hard_feistel
9ff3b4313af3f7dceedf5e0443408231  reverse/Hard_02_Feistel/hard_feistel

$ stat -c '%s bytes' reverse/Hard_02_Feistel/hard_feistel
14528 bytes
```

```text
$ python3 -c "from pwn import *; print(ELF('reverse/Hard_02_Feistel/hard_feistel').checksec())"
RELRO:      Full RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        PIE enabled
FORTIFY:    Enabled
SHSTK:      Enabled
IBT:        Enabled
```

```text
$ strings -n 4 reverse/Hard_02_Feistel/hard_feistel
...
Pemakaian: %s <flag>
Wrong!
Correct! Jaringan Feistel berhasil dibalik.
...
```

**Temuan:** panjang input dicek `== 0x27` (39 byte) di `0x111a`. Ciphertext tidak muncul sebagai string; ia berada di `.data` dan diakses lewat `lea rsi,[rip+0x2e3b] # 4020`. Round key berada di `.rodata` `0x2060` dan terlihat sebagai deret nilai 16-bit.

### 1.5 Perintah akuisisi bukti

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
