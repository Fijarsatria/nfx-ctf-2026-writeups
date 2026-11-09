# THE FORGOTTEN STATE — Triage awal

[← Overview](42-the-forgotten-state.md) · [Index](index.md)

## 1.4 Triage awal

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
