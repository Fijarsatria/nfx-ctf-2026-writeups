# SymHell — Flag & Verifikasi

[← Overview](31-symhell.md) · [Index](index.md)

```text
NFX{5ymH3ll_RUnT1m3_3v4l_53cr3t_PwN!}
```

Verifikasi:

- Payload tidak mengandung karakter terlarang (`forbidden present: False`).
- Service lokal mengeksekusi payload dan mengembalikan flag di stderr.
- Flag sama dengan `flags/forensics/symhell.txt`.
- Simulasi memakai `/flag.txt` sementara; file dihapus setelah pengujian.

## Flag

`NFX{5ymH3ll_RUnT1m3_3v4l_53cr3t_PwN!}`

**Status:** `VERIFIED`
