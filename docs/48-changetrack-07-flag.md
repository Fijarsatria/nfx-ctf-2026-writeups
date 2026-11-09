# ChangeTrack — Flag & Verifikasi

[← Overview](48-changetrack.md) · [Index](index.md)

> **Flag:** `NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}`
> **Status:** `VERIFIED`

```text
NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}
```

Verifikasi:

```bash
cat flags/misc/ChangeTrack.txt
# NFX{ch4ng3_d3t3ct10n_j1nj4_sst1_oob_cve_2024_32651_2026}
```

Flag yang sama muncul di body webhook dari instance live. Tidak ada submit ke platform.

### Bukti submit di platform

![00b-submit-platform.png](assets/changetrack/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Evidence langkah ini

![term-14-flag-capture.png](assets/changetrack/term-14-flag-capture.png)

*Terminal evidence — `14-flag-capture.txt` (arsip transkrip sesi solve).*

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
