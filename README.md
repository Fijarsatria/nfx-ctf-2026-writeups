# NFX CTF 2026 — Writeup Medium–Hard (GitHub Pages)

Situs statis MkDocs Material untuk **534 halaman** (52 challenge).
Tiap challenge dipecah menjadi Overview, Recon, Analisis, Eksploitasi, Flag,
Evidence, dan Referensi, lengkap dengan command, output, dan screenshot.

**Disusun oleh:** **B0TCIL**

**Live:** <https://fijarsatria.github.io/nfx-ctf-2026-writeups/>

Fitur utama:

- Hero, statistik, kartu kategori, dan tabel challenge yang bisa difilter
  berdasarkan status, kategori, atau kata kunci.
- Badge status (`VERIFIED` dan `OPEN`) serta kartu navigasi per challenge.
- Galeri evidence berbentuk grid, dengan pratinjau screenshot di halaman
  Overview.
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
- `docs/NN-*.md` — halaman per bagian (Recon, Analisis, Solver, dst.).
- `docs/assets/` — screenshot dan file evidence.
- `mkdocs.yml` — nav per event/kategori.

## Evidence

Setiap halaman punya bagian **Evidence / Bukti (arsip)**. Screenshot
tertanam lewat path `assets/<slug>/...`; transkrip terminal tetap ada di
langkah exploit. NXPortal berstatus OPEN dan halamannya memuat analisis
serta kendala yang ditemui, bukan flag.
