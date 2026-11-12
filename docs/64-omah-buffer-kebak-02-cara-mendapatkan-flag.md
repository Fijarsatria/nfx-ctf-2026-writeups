# Omah Buffer Kebak — Flag & Verifikasi

[← Overview](64-omah-buffer-kebak.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.** Cara Mendapatkan Flag
>
> **Titik penting:** NFX{OmahhKUuD0Ndoll_Uw0nggG}
>
> **Berikutnya:** [Flag](64-omah-buffer-kebak-03-flag.md)

> **Flag:** `NFX{OmahhKUuD0Ndoll_Uw0nggG}`
> **Status:** `VERIFIED`

1. Cek binary:
```bash
file omah_buffer
checksec ./omah_buffer
```
2. Cari offset dengan pola cyclic dan lihat register saat crash.
3. Susun payload sesuai arsitektur, lalu baca flag di server.

### Terminal evidence (real)

![Terminal evidence (real)](assets/omah-buffer-kebak/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).
