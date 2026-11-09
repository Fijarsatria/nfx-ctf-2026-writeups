# Talatah Ti Peuntas — Alamat penting

[← Overview](41-talatah-ti-peuntas.md) · [Index](index.md)

## 2.5 Alamat penting

| Simbol | Alamat |
|---|---|
| `free@got` | `0x404000` |
| `printf@got` | `0x404028` |
| `.bss` (buffer baru) | `0x404140` |

`printf@got` dipakai untuk leak karena `printf` sudah pasti terselesaikan oleh menu; `free@got` bisa jadi masih menunjuk PLT stub kalau `free` belum pernah dipanggil.
