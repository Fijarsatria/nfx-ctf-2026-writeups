# SymHell — Flag & Verifikasi

[← Overview](31-symhell.md) · [Index](index.md)

> **Flag:** `NFX{5ymH3ll_RUnT1m3_3v4l_53cr3t_PwN!}`
> **Status:** `VERIFIED`

```text
NFX{5ymH3ll_RUnT1m3_3v4l_53cr3t_PwN!}
```

Verifikasi:

- Payload tidak mengandung karakter terlarang (`forbidden present: False`).
- Service lokal mengeksekusi payload dan mengembalikan flag di stderr.
- Flag sama dengan `flags/forensics/symhell.txt`.
- Simulasi memakai `/flag.txt` sementara; file dihapus setelah pengujian.

### Bukti submit di platform

![00b-submit-platform.png](assets/symhell/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
