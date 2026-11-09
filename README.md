# NFX CTF 2026 — Writeup Medium–Hard (GitHub Pages)

Situs statis MkDocs Material untuk **368 halaman** (52 challenge).
Tiap challenge dipecah menjadi Overview, Recon, Analisis, Eksploitasi, Flag,
Evidence, dan Referensi, lengkap dengan command, output, dan screenshot.

## Preview lokal

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Buka `http://127.0.0.1:8000/`.

## Deploy ke GitHub Pages

1. Buat repository GitHub, lalu push **isi folder ini** sebagai root repo.
2. Buka **Settings → Pages**.
3. Di **Build and deployment**, pilih **Source: GitHub Actions**.
4. Push ke branch `main` (atau jalankan workflow manual).
5. Workflow `.github/workflows/pages.yml` akan build dan deploy.
6. URL ada di halaman **Actions → Deploy MkDocs to GitHub Pages**.

Workflow memakai `mkdocs build --strict`; kalau ada link/asset yang hilang,
build akan gagal dan menampilkan nama file yang bermasalah.

## Struktur

- `docs/index.md` — cover, status, daftar challenge.
- `docs/NN-*.md` — halaman per challenge.
- `docs/assets/` — screenshot dan file evidence.
- `mkdocs.yml` — nav per event/kategori.

## Evidence

Setiap halaman punya bagian **Evidence / Bukti (arsip)**. Screenshot
tertanam lewat path `assets/<slug>/...`; transkrip terminal tetap ada di
langkah exploit. NXPortal berstatus OPEN dan halamannya adalah dokumentasi
blocker, bukan flag.
