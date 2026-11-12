# LinkVault — Flag & Verifikasi

[← Overview](49-linkvault.md) · [Index](index.md)

> **Langkah 10/12 — Flag.** Flag yang sama muncul di halaman /reports milik user penyerang pada instance live.
>
> **Titik penting:** NFX{L1nkV4ult_cve_26_3p1c_!}
>
> **Berikutnya:** [Bukti / Evidence](49-linkvault-11-bukti-evidence.md)

> **Asal flag.** Flag diperoleh dari langkah exploit/solver yang terdokumentasi, lalu disubmit ke platform.  
> **Tingkat bukti metode.** Terdokumentasi. [Buka Evidence](49-linkvault-11-bukti-evidence.md)

> **Flag:** `NFX{L1nkV4ult_cve_26_3p1c_!}`
> **Status:** `VERIFIED`

```text
NFX{L1nkV4ult_cve_26_3p1c_!}
```

Verifikasi:

```bash
cat flags/web/LinkVault.txt
# NFX{L1nkV4ult_cve_26_3p1c_!}
```

Flag yang sama muncul di halaman `/reports` milik user penyerang pada instance live. Tidak ada submit ke platform.

### Terminal evidence (real)

![Terminal evidence (real)](assets/linkvault/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/linkvault/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*
