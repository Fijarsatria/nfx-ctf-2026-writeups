# NexaIdentity

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Web</span><span class="nx-chip">Medium</span><span class="nx-chip">120 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `120` |
| Author | `Ariaf` |
| Solves | `20` |
| Tools | curl, python3 |
| Flag | `NFX{n0sql_0p3r4t0r_4uth_byp4ss}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/nexaidentity/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. **NexaIdentity** adalah direktori karyawan NexaCommerce berbasis Express. Halaman login menyediakan akun demo `employee@nexaidentity.test` / `employee1234` (Raka Pratama, employee biasa). Terus, endpoint admin `/admin` mengembalikan `403` untuk Raka. Lalu, login memakai query bergaya Mongo/NoSQL dengan objek dari body form. Karena `express.urlencoded({ extended: true })` memakai `qs`, field `password[$ne]=x` menjadi objek `{ $ne: "x" }`. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | http://s1.nfx.my.id:41270 | [Buka](11-nexaidentity-01-recon.md) |
| 2 | Triage awal | curl -sS -i "$BASE/" | [Buka](11-nexaidentity-02-triage-awal.md) |
| 3 | Analisis | Form login menggunakan application/x-www-form-urlencoded. | [Buka](11-nexaidentity-03-analisis.md) |
| 4 | Analisis | NFX{...} | [Buka](11-nexaidentity-04-analisis-2.md) |
| 5 | Eksploitasi / Solver | curl -sS -i -c admin.cookies \ | [Buka](11-nexaidentity-05-eksploitasi-solver.md) |
| 6 | Script minimal | http://s1.nfx.my.id:41270" | [Buka](11-nexaidentity-06-script-minimal.md) |
| 7 | Flag | NFX{n0sql_0p3r4t0r_4uth_byp4ss} | [Buka](11-nexaidentity-07-flag.md) |
| 8 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](11-nexaidentity-08-bukti-evidence.md) |
| 9 | Referensi | — | [Buka](11-nexaidentity-09-referensi.md) |

## TL;DR

- **NexaIdentity** adalah direktori karyawan NexaCommerce berbasis Express. Halaman login menyediakan akun demo `employee@nexaidentity.test` / `employee1234` (Raka Pratama, employee biasa).
- Endpoint admin `/admin` mengembalikan `403` untuk Raka.
- Login memakai query bergaya Mongo/NoSQL dengan objek dari body form. Karena `express.urlencoded({ extended: true })` memakai `qs`, field `password[$ne]=x` menjadi objek `{ $ne: "x" }`.
- Payload `email[$ne]=x&password[$ne]=x` membuat query mencocokkan user pertama (admin, Nadia Kusuma) → session admin.
- `/admin` lalu menampilkan *Emergency recovery token*: `NFX{n0sql_0p3r4t0r_4uth_byp4ss}`.

<div class="nx-evidence-preview"><a href="11-nexaidentity-08-bukti-evidence.html"><img src="assets/nexaidentity/00b-terminal-evidence.png" alt="Pratinjau evidence NexaIdentity" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="11-nexaidentity-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="11-nexaidentity-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="11-nexaidentity-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="11-nexaidentity-03-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="11-nexaidentity-04-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="11-nexaidentity-05-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="11-nexaidentity-06-script-minimal.html"><b>Script minimal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="11-nexaidentity-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="11-nexaidentity-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="11-nexaidentity-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
