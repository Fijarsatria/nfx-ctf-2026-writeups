# NexusGate — Strategi

[← Overview](50-nexusgate.md) · [Index](index.md)

## 3.1 Strategi

- Gunakan `requests` lalu set `PreparedRequest.url` mentah agar `/./` tidak dinormalisasi.
- Lakukan cursor over-grant dan baca journal.
- Baca nonce bot dari `/app/data/bot` (permission tree).
- Ambil cached ticket dan tukar dengan flag.

### Evidence langkah ini

![term-03-exploit-run.png](assets/nexusgate/term-03-exploit-run.png)

*Terminal evidence — `03-exploit-run.txt` (arsip transkrip sesi solve).*
