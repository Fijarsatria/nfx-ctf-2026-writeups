# NexusGate

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Web</span><span class="nx-chip">Hard</span><span class="nx-chip">320 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Web` |
| Difficulty | `Hard` |
| Poin | `320` |
| Author | `Ariaf` |
| Solves | `10` |
| Tools | curl, docker |
| Flag | `NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/nexusgate/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## TL;DR

- **NexusGate** terdiri dari edge reverse proxy Node.js (`:80`) di depan microservice vault (`127.0.0.1:8080`).
- ACL edge hanya memblokir `req.url.startsWith('/internal/')`. Path `/./internal/...` lolos dari string check, lalu dinormalisasi oleh `new URL()` di backend menjadi `/internal/...` → **ACL bypass**.
- Endpoint `/internal/console/cursor` membuat iterator SQL dari parameter `owner` yang dikendalikan user. `owner=admin` menghasilkan cursor atas vault admin; endpoint GET dengan parameter `journal=<user>` menulis isi row (`secret=PHASE_TOKEN`) ke audit journal penyerang.
- Endpoint `/internal/console/files` membaca file dengan Node `--permission`. Allow-list `bot1.json`, `bot2.json`, `bot3.json` memiliki common prefix `/app/data/bot`; permission tree Node 24.14.0 menganggap node prefix itu readable, sehingga `/app/data/bot` (nonce bot) bisa dibaca.
- Nonce bot adalah `aud` yang dipakai bot admin saat mengambil `/tickets/latest?aud=<nonce>` melalui edge cache (`undici interceptors.cache()`). Cache key tidak memisahkan admin vs anonim, sehingga penyerang mendapatkan HTML admin yang berisi `MASTER_TICKET`.
- `POST /flag` dengan ticket tersebut mengembalikan flag: `NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}`.

<div class="nx-evidence-preview"><a href="50-nexusgate-11-bukti-evidence.html"><img src="assets/nexusgate/00b-submit-platform.png" alt="Pratinjau evidence NexusGate" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="50-nexusgate-11-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="50-nexusgate-01-deskripsi-challenge.html"><b>Deskripsi challenge</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-02-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="50-nexusgate-03-acl-bypass-raw-req-url-vs-new-url.html"><b>ACL bypass: raw `req.url` vs `new URL()`</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-04-cursor-over-grant-phase-token.html"><b>Cursor over-grant → PHASE_TOKEN</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-05-file-read-sandbox-node-permission-tree.html"><b>File-read sandbox: Node permission tree</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-06-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="50-nexusgate-07-strategi.html"><b>Strategi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-08-langkah-exploit-live.html"><b>Langkah exploit (live)</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-09-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="50-nexusgate-10-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="50-nexusgate-11-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="50-nexusgate-12-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
