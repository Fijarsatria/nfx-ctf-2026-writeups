# NFX CTF 2026 — Writeup Lengkap (GitHub Pages)

Situs statis MkDocs Material untuk **86 challenge NFX CTF 2026**:
**85 VERIFIED** dan **1 OPEN** (NXPortal).

Setiap challenge dipecah menjadi Overview, Recon, Analisis, Eksploitasi/Solver,
Flag, Evidence, dan Referensi. Setiap challenge yang **VERIFIED** punya
screenshot validasi asli dari platform:

```text
docs/assets/<slug>/00b-platform-validation.png
```

Screenshot itu diambil langsung dari form challenge di
<https://ctf.nfx.my.id/> dan menampilkan pesan
**`CORRECT, BUT ALREADY SOLVED.`**

**Disusun oleh:** **B0TCIL**

**Live:** <https://fijarsatria.github.io/nfx-ctf-2026-writeups/>

## Status

| Status | Jumlah |
|---|---:|
| Challenge | **86** |
| VERIFIED | **85** |
| OPEN | **1** (NXPortal) |
| Validasi platform (`00b-platform-validation.png`) | **85** |

NXPortal tetap **OPEN**: flag challenge belum ditemukan, jadi tidak ada
screenshot `CORRECT` dan tidak ada klaim `VERIFIED`. Halaman NXPortal berisi
blocker serta analisis yang sudah dicoba, bukan flag.

## Fitur

- Hero, statistik, kartu kategori, dan tabel challenge yang bisa difilter
  berdasarkan status, track, kategori, atau kata kunci.
- Sidebar dipisah **Track Mahasiswa NF** dan **Track Umum / Extend**.
- Badge status (`VERIFIED` dan `OPEN`) serta kartu navigasi per challenge.
- Galeri evidence berbentuk grid, dengan pratinjau screenshot di halaman
  Overview.
- Setiap halaman Flag punya bagian **Validasi platform (real)**.
- Mode gelap/terang, pencarian global, daftar isi per halaman, tombol salin
  kode, dan tombol kembali ke atas.

## Preview lokal

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Buka `http://127.0.0.1:8000/`.

## Deploy ke GitHub Pages

1. Push **isi folder ini** sebagai root repo.
2. Buka **Settings → Pages**.
3. Di **Build and deployment**, pilih **Source: GitHub Actions**.
4. Push ke branch `main`.
5. Workflow `.github/workflows/pages.yml` akan build dan deploy.

Workflow memakai `mkdocs build --strict`; kalau ada link/asset yang hilang,
build akan gagal dan menampilkan nama file yang bermasalah.

## Struktur

- `docs/index.md` — cover, status, daftar challenge.
- `docs/NN-*.md` — halaman per bagian (Recon, Analisis, Solver, Flag, dst.).
- `docs/assets/` — screenshot dan file evidence.
- `mkdocs.yml` — nav per track/kategori.

## Evidence

- **Validasi platform:** `docs/assets/<slug>/00b-platform-validation.png`.
- **Brief challenge:** `docs/assets/<slug>/00-challenge-platform.png`.
- **Terminal/transkrip:** `docs/assets/<slug>/term-*.png` dan file mentah
  pendukung.
- **13 Is Not Enough:** solver empat layer (XOR 13 → reverse → ROT13 →
  digit -3) ada di `docs/assets/13-is-not-enough/11-solver.py` dan
  `11-solver.txt`.

Semua screenshot validasi berasal dari platform, bukan mockup.
