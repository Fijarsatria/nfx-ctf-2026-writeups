# Medium TEA — Triage awal

[← Overview](47-medium-tea.md) · [Index](index.md)

## 1.4 Triage awal

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
