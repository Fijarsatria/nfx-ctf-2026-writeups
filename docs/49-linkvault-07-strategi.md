# LinkVault — Strategi

[← Overview](49-linkvault.md) · [Index](index.md)

> **Langkah 7/12 — Strategi.** Strategi
>
> **Titik penting:** —
>
> **Berikutnya:** [Langkah exploit (live)](49-linkvault-08-langkah-exploit-live.md)

## 3.1 Strategi

- Gunakan IPv6 loopback `[::1]` untuk SSRF.
- Gunakan endpoint `/internal/import` untuk menyisipkan `filter` tanpa validasi.
- Susun payload XSS yang:
  - keluar dari regex literal: `./; ... ;var q=/.`
  - tidak memakai karakter `>` agar tidak di-escape,
  - memakai `fetch` same-origin untuk `/flag`,
  - mengirim hasil ke `/api/share` milik user penyerang.

### Evidence langkah ini

![term-01-recon.png](assets/linkvault/term-01-recon.png)

*Terminal evidence — `01-recon.txt` (arsip transkrip sesi solve).*

![term-02-exploit-run.png](assets/linkvault/term-02-exploit-run.png)

*Terminal evidence — `02-exploit-run.txt` (arsip transkrip sesi solve).*

![term-03-ssrf-evidence.png](assets/linkvault/term-03-ssrf-evidence.png)

*Terminal evidence — `03-ssrf-evidence.txt` (arsip transkrip sesi solve).*

![term-source-notes.png](assets/linkvault/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-recon.txt`](assets/linkvault/01-recon.txt)
- [`02-exploit-run.txt`](assets/linkvault/02-exploit-run.txt)
- [`03-ssrf-evidence.py`](assets/linkvault/03-ssrf-evidence.py)
- [`03-ssrf-evidence.txt`](assets/linkvault/03-ssrf-evidence.txt)
- [`source-notes.txt`](assets/linkvault/source-notes.txt)
