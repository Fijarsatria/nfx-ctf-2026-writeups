# Talatah Ti Peuntas

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Hard` |
| Poin | `440` |
| Author | `Amablex` |
| Solves | `4` |
| Tools | python3, pwntools, checksec, objdump, readelf, strings |
| Flag | `NFX{HiduPPk1T4AAyangMelawann}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Service "pengelola talatah" mem-parsing pesan protokol **TLT1**: `magic | total_len | key_size | tag | tlv_len | payload`.
- Validasi memeriksa `key_size` (1..0x40) dan `total_len >= tlv_len + 0x14`, tetapi **tidak pernah membandingkan `tlv_len` dengan `key_size`**.
- Parser melakukan `data = malloc(key_size)` lalu `memcpy(data, msg+0x14, tlv_len)` → **heap overflow** dari chunk data ke chunk node yang berdekatan.
- Node struct 0x20 byte berisi `name[16]`, `len`, `flags`, dan `char *data`. Overflow mengontrol `node->len` dan `node->data`.
- `op_view` menjadi **arbitrary read** (`fwrite(node->data, node->len)`); `op_edit` menjadi **arbitrary write** (`memcpy(node->data, input, new_len)`).
- Exploit: leak `printf@got`, hitung libc, tulis `system` ke `free@got`, taruh `/bin/sh` di `.bss`, lalu `delete` node → `free("/bin/sh")` = `system("/bin/sh")`.
- Flag: `NFX{HiduPPk1T4AAyangMelawann}`.

## Navigasi Halaman

- [Recon](41-talatah-ti-peuntas-01-recon.md)
- [Analisis](41-talatah-ti-peuntas-02-analisis.md)
- [Eksploitasi](41-talatah-ti-peuntas-03-eksploitasi.md)
- [Flag](41-talatah-ti-peuntas-04-flag.md)
- [Bukti / Evidence](41-talatah-ti-peuntas-05-bukti-evidence.md)
- [Referensi](41-talatah-ti-peuntas-06-referensi.md)
