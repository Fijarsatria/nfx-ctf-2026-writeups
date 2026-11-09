# NexusGate

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Web` |
| Difficulty | `Hard` |
| Poin | `320` |
| Author | `Ariaf` |
| Solves | `10` |
| Flag | `NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- **NexusGate** terdiri dari edge reverse proxy Node.js (`:80`) di depan microservice vault (`127.0.0.1:8080`).
- ACL edge hanya memblokir `req.url.startsWith('/internal/')`. Path `/./internal/...` lolos dari string check, lalu dinormalisasi oleh `new URL()` di backend menjadi `/internal/...` → **ACL bypass**.
- Endpoint `/internal/console/cursor` membuat iterator SQL dari parameter `owner` yang dikendalikan user. `owner=admin` menghasilkan cursor atas vault admin; endpoint GET dengan parameter `journal=<user>` menulis isi row (`secret=PHASE_TOKEN`) ke audit journal penyerang.
- Endpoint `/internal/console/files` membaca file dengan Node `--permission`. Allow-list `bot1.json`, `bot2.json`, `bot3.json` memiliki common prefix `/app/data/bot`; permission tree Node 24.14.0 menganggap node prefix itu readable, sehingga `/app/data/bot` (nonce bot) bisa dibaca.
- Nonce bot adalah `aud` yang dipakai bot admin saat mengambil `/tickets/latest?aud=<nonce>` melalui edge cache (`undici interceptors.cache()`). Cache key tidak memisahkan admin vs anonim, sehingga penyerang mendapatkan HTML admin yang berisi `MASTER_TICKET`.
- `POST /flag` dengan ticket tersebut mengembalikan flag: `NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}`.

## Navigasi Halaman

- [Recon](50-nexusgate-01-recon.md)
- [Analisis](50-nexusgate-02-analisis.md)
- [Eksploitasi / Solver](50-nexusgate-03-eksploitasi-solver.md)
- [Flag](50-nexusgate-04-flag.md)
- [Bukti / Evidence](50-nexusgate-05-bukti-evidence.md)
- [Referensi](50-nexusgate-06-referensi.md)
