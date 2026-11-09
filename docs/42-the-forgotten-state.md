# THE FORGOTTEN STATE

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Hard` |
| Poin | `340` |
| Author | `Amablex` |
| Solves | `9` |
| Flag | `NFX{ElC0nloe_Forg0tten_StaticcD42#}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Service mengelola 16 record (`create`, `release`, `view`, `edit`, `list`).
- `op_release()` melakukan `free(record->data)` lalu `free(record)`, mengosongkan `active[idx]`, tetapi **tidak mengosongkan `table[idx]`** → dangling pointer. `op_view`/`op_edit`/`op_list` **tidak memeriksa `active[]`**, jadi pointer basi masih bisa dipakai (use-after-free).
- `op_edit()` memvalidasi `new_len` hanya pada rentang `1..0x400`, bukan terhadap ukuran alokasi asli → **heap overflow** ke record berikutnya.
- Exploit yang diverifikasi memakai overflow: record pertama (data 0x20 byte) diedit 0x50 byte, menimpa header record kedua: `name`, `len=8`, `flags=1`, dan `data = free@got`.
- `view` → leak `free@got`; `edit` → tulis `system` ke `free@got`; `release` pada record berisi `"/bin/sh"` → `free("/bin/sh")` = `system("/bin/sh")`.
- Flag: `NFX{ElC0nloe_Forg0tten_StaticcD42#}`.

## Navigasi Halaman

- [Recon](42-the-forgotten-state-01-recon.md)
- [Analisis](42-the-forgotten-state-02-analisis.md)
- [Eksploitasi](42-the-forgotten-state-03-eksploitasi.md)
- [Flag](42-the-forgotten-state-04-flag.md)
- [Bukti / Evidence](42-the-forgotten-state-05-bukti-evidence.md)
- [Referensi](42-the-forgotten-state-06-referensi.md)
