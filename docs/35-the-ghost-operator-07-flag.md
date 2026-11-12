# The Ghost Operator — Flag & Verifikasi

[← Overview](35-the-ghost-operator.md) · [Index](index.md)

> **Langkah 7/9 — Flag.** Verifikasi platform (2026-11-08):
>
> **Titik penting:** NFX{villa_istana_bunga_lembang}
>
> **Berikutnya:** [Bukti / Evidence](35-the-ghost-operator-08-bukti-evidence.md)

> **Asal flag.** Flag diperoleh dari langkah exploit/solver yang terdokumentasi, lalu disubmit ke platform.  
> **Tingkat bukti metode.** Terdokumentasi. [Buka Evidence](35-the-ghost-operator-08-bukti-evidence.md)

> **Flag:** `NFX{villa_istana_bunga_lembang}`
> **Status:** `VERIFIED`

```text
NFX{villa_istana_bunga_lembang}
```

Verifikasi platform (2026-11-08):

```text
HTTP 200
{"success": true, "message": "Correct! +380 points."}
```

Riwayat kandidat:

| Kandidat | Status |
|---|---|
| `NFX{villa_istana_bunga}` | Ditolak |
| `NFX{Villa_Istana_Bunga}` | Ditolak |
| `NFX{VILLA_ISTANA_BUNGA}` | Ditolak |
| `NFX{villa_istana_bunga_lembang}` | **DITERIMA** (`Correct! +380 points.`) |

### Terminal evidence (real)

![Terminal evidence (real)](assets/the-ghost-operator/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/the-ghost-operator/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*
