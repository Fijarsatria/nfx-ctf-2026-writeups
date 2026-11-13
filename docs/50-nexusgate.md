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

## Cerita singkat

Jadi ceritanya gini. **NexusGate** terdiri dari edge reverse proxy Node.js (`:80`) di depan microservice vault (`127.0.0.1:8080`). Terus, aCL edge hanya memblokir `req.url.startsWith('/internal/')`. Path `/./internal/...` lolos dari string check, lalu dinormalisasi oleh `new URL()` di backend menjadi `/internal/...` → **ACL bypass**. Lalu, endpoint `/internal/console/cursor` membuat iterator SQL dari parameter `owner` yang dikendalikan user. `owner=admin` menghasilkan cursor atas vault admin; endpoint GET dengan parameter `journal=<user>` menulis isi row (`secret=PHASE_TOKEN`) ke audit journal penyerang. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Deskripsi challenge | Empat komponen yang disebut: 1. | [Buka](50-nexusgate-01-deskripsi-challenge.md) |
| 2 | Recon | curl -sS http://s1.nfx.my.id:49535/health | [Buka](50-nexusgate-02-recon.md) |
| 3 | ACL bypass: raw `req.url` vs `new URL()` | http://127.0.0.1:8080' | [Buka](50-nexusgate-03-acl-bypass-raw-req-url-vs-new-url.md) |
| 4 | Cursor over-grant → PHASE_TOKEN | Audit user <user> sekarang berisi: | [Buka](50-nexusgate-04-cursor-over-grant-phase-token.md) |
| 5 | File-read sandbox: Node permission tree | file read: /app/data/bot -> f0f6801a74026cf1 | [Buka](50-nexusgate-05-file-read-sandbox-node-permission-tree.md) |
| 6 | Analisis | — | [Buka](50-nexusgate-06-analisis.md) |
| 7 | Strategi | — | [Buka](50-nexusgate-07-strategi.md) |
| 8 | Langkah exploit (live) | curl -sS -c cj -X POST -d 'username=ng123456&password=pw' "$BASE/register" | [Buka](50-nexusgate-08-langkah-exploit-live.md) |
| 9 | Output asli | NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026} | [Buka](50-nexusgate-09-output-asli.md) |
| 10 | Flag | NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026} | [Buka](50-nexusgate-10-flag.md) |
| 11 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](50-nexusgate-11-bukti-evidence.md) |
| 12 | Referensi | — | [Buka](50-nexusgate-12-referensi.md) |

## TL;DR

- **NexusGate** terdiri dari edge reverse proxy Node.js (`:80`) di depan microservice vault (`127.0.0.1:8080`).
- ACL edge hanya memblokir `req.url.startsWith('/internal/')`. Path `/./internal/...` lolos dari string check, lalu dinormalisasi oleh `new URL()` di backend menjadi `/internal/...` → **ACL bypass**.
- Endpoint `/internal/console/cursor` membuat iterator SQL dari parameter `owner` yang dikendalikan user. `owner=admin` menghasilkan cursor atas vault admin; endpoint GET dengan parameter `journal=<user>` menulis isi row (`secret=PHASE_TOKEN`) ke audit journal penyerang.
- Endpoint `/internal/console/files` membaca file dengan Node `--permission`. Allow-list `bot1.json`, `bot2.json`, `bot3.json` memiliki common prefix `/app/data/bot`; permission tree Node 24.14.0 menganggap node prefix itu readable, sehingga `/app/data/bot` (nonce bot) bisa dibaca.
- Nonce bot adalah `aud` yang dipakai bot admin saat mengambil `/tickets/latest?aud=<nonce>` melalui edge cache (`undici interceptors.cache()`). Cache key tidak memisahkan admin vs anonim, sehingga penyerang mendapatkan HTML admin yang berisi `MASTER_TICKET`.
- `POST /flag` dengan ticket tersebut mengembalikan flag: `NFX{n3xu5_g4t3_0v3r_gr4nt_c4ch3_smuggl3_2026}`.

<div class="nx-evidence-preview"><a href="50-nexusgate-11-bukti-evidence.html"><img src="assets/nexusgate/00b-terminal-evidence.png" alt="Pratinjau evidence NexusGate" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="50-nexusgate-11-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

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
