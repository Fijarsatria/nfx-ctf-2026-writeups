# THE FORGOTTEN STATE — Recon

[← Overview](42-the-forgotten-state.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Amablex**
>
> Sebuah layanan pemrosesan request mengalami perilaku tidak normal ketika menangani beberapa request secara berurutan. Tim investigasi menemukan indikasi bahwa pengelolaan objek dan state internal tidak berjalan sebagaimana mestinya.

Kata kunci: **"pengelolaan objek dan state internal"** dan judul **"THE FORGOTTEN STATE"** → state `active[]`/`table[]` yang tidak konsisten.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/TheForgottenState/peserta/state` | 16.848 B | `57d3954881917b39492c0ffbea4e74b58a06c49768f103b555fd0f8887bf08e7` |
| `pwn/TheForgottenState/peserta/libc.so.6` | 2.190.608 B | `85e64f97e348786a8fb4d9f3d52fec289e2fb86bba20f0731dfe61990525e0f7` |
| `pwn/TheForgottenState/peserta/ld-linux-x86-64.so.2` | 254.864 B | loader bawaan |

Service asli: `NFX/PWNNXCTF-2026/TheForgottenState` (TCP), saat penulisan stopped.

### 1.3 Environment

- Linux x86-64; libc challenge (sama dengan Talatah).
- Menjalankan:
  ```bash
  cd pwn/TheForgottenState/peserta
  ./ld-linux-x86-64.so.2 --library-path . ./state
  ```
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `readelf`, `pwntools`.

### 1.4 Triage awal

```text
$ file state
state: ELF 64-bit LSB executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=b35d59944000aae617a421ff9df72debc43748f0,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools)
RELRO:      Partial RELRO
Stack:      Canary found
NX:         NX enabled
PIE:        No PIE (0x400000)
SHSTK:      Enabled
IBT:        Enabled
Stripped:   No
```

`strings`:

```text
=== NX STATE SERVICE ===
kelola record request (maks 16)
[!] index kosong.
[!] slot penuh.
name :
size :
data :
[+] record #%d dibuat (size=%ld)
[!] record sudah dilepas sebelumnya.
[+] record #%d dilepas (payload + header dibebaskan)
view[%d] name=%.16s len=%u data:
new length :
[+] record diperbarui.
active
released
[%d] name=%.16s len=%-4u flags=0x%x  %s
[1] create record
[2] release record
[3] view record
[4] edit record
[5] list records
[6] exit
```

Symbol:

```text
000000000040150b t op_create
000000000040173a t op_release
0000000000401830 t op_view
000000000040190f t op_edit
0000000000401a00 t op_list
```
