# Unbreakable Delay — Flag & Verifikasi

[← Overview](23-unbreakable-delay.md) · [Index](index.md)

> **Langkah 6/8 — Flag.** Verifikasi (log submit asli):
>
> **Titik penting:** NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}
>
> **Berikutnya:** [Bukti / Evidence](23-unbreakable-delay-07-bukti-evidence.md)

> **Asal flag.** Flag diperoleh dari langkah exploit/solver yang terdokumentasi, lalu disubmit ke platform.  
> **Tingkat bukti metode.** Terdokumentasi. [Buka Evidence](23-unbreakable-delay-07-bukti-evidence.md)

> **Status metode:** **FULL** — metode utama berhasil direproduksi.  
> **Flag:** `NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}`
> **Status:** `VERIFIED`

```text
NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}
```

Verifikasi (log submit asli):

```json
{"time": 1794056594.077969, "id": "166046e6-4804-4104-ad43-f5b48ee768ff",
 "title": "Unbreakable Delay",
 "flag": "NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}",
 "http": 200,
 "result": {"success": true, "message": "Correct! +500 points."}}
```

Status: **verified platform**. Detail protokol service tetap `[REKONSTRUKSI]`
karena tidak ada source/instance lokal.

### Terminal evidence (real)

![Terminal evidence (real)](assets/unbreakable-delay/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/unbreakable-delay/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*
