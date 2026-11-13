# The Ghost Operator

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Osint</span><span class="nx-chip">Medium</span><span class="nx-chip">380 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Osint` |
| Difficulty | `Medium` |
| Poin | `380` |
| Author | `Ariaf` |
| Solves | `7` |
| Tools | curl, python3, sage, angr, git, gpg |
| Flag | `NFX{villa_istana_bunga_lembang}` |
| Status | `VERIFIED` |
[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/the-ghost-operator/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. `investigation.zip` berisi repo git dengan satu commit yang **ditandatangani GPG**. Terus, `git log --show-signature` membuka identitas key: `Dimas Wirawan (rentry.co/ghost-route-0914)`. Lalu, enumerasi keyserver `veloxphantom.net` menemukan **tiga key**:. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Jejak Awal | sha256sum osint/investigation.zip | [Buka](35-the-ghost-operator-01-jejak-awal.md) |
| 2 | Analisis Jejak | git log --all --oneline --decorate | [Buka](35-the-ghost-operator-02-analisis-jejak.md) |
| 3 | Analisis Jejak | Dua URL telegra.ph dapat diakses langsung. | [Buka](35-the-ghost-operator-03-analisis-jejak-2.md) |
| 4 | Identifikasi tempat | Sumber publik yang cocok: | [Buka](35-the-ghost-operator-04-identifikasi-tempat.md) |
| 5 | Mengapa lowercase ditolak? | NFX{villa_istana_bunga} | [Buka](35-the-ghost-operator-05-mengapa-lowercase-ditolak.md) |
| 6 | Pencarian & Verifikasi | curl -s 'https://keyserver.ubuntu.com/pks/lookup?op=index&search=veloxphantom.net&options=mr' | [Buka](35-the-ghost-operator-06-pencarian-verifikasi.md) |
| 7 | Flag | NFX{villa_istana_bunga_lembang} | [Buka](35-the-ghost-operator-07-flag.md) |
| 8 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](35-the-ghost-operator-08-bukti-evidence.md) |
| 9 | Referensi | NFX{Villa_Istana_Bunga} | [Buka](35-the-ghost-operator-09-referensi.md) |

## Ringkasan

> Catatan verifikasi: kandidat `NFX{villa_istana_bunga}` dan
> `NFX{Villa_Istana_Bunga}` **ditolak**. String yang diterima adalah
> `NFX{villa_istana_bunga_lembang}` (nama tempat + lokasi Lembang).
## TL;DR

- `investigation.zip` berisi repo git dengan satu commit yang **ditandatangani
  GPG**.
- `git log --show-signature` membuka identitas key:
  `Dimas Wirawan (rentry.co/ghost-route-0914)`.
- Enumerasi keyserver `veloxphantom.net` menemukan **tiga key**:
  - dua key mengarah ke `telegra.ph/Field-Notes-0914-Escape-Route-10-25`
    (dan varian `-2`);
  - satu key mengarah ke `rentry.co/ghost-route-0914`.
- Semua field notes (telegra.ph, telegra.ph `-2`, `-3`, dan snapshot rentry)
  berisi petunjuk yang sama: kompleks villa di **Jl. Kolonel Masturi KM 9**,
  kaki **Gunung Burangrang**, **taman bunga tematik**, dan **kompleks villa
  terbesar di Parongpong–Lembang**.
- Tempat yang cocok: **Villa Istana Bunga (VIB)**, Jl. Kolonel Masturi KM 9,
  Parongpong/Lembang.
- Flag yang diterima platform: `NFX{villa_istana_bunga_lembang}` —
  nama safehouse + kota Lembang (bukan sekadar `villa_istana_bunga`).

<div class="nx-evidence-preview"><a href="35-the-ghost-operator-08-bukti-evidence.html"><img src="assets/the-ghost-operator/00b-terminal-evidence.png" alt="Pratinjau evidence The Ghost Operator" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="35-the-ghost-operator-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="35-the-ghost-operator-01-jejak-awal.html"><b>Jejak Awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-02-analisis-jejak.html"><b>Analisis Jejak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-03-analisis-jejak-2.html"><b>Analisis Jejak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-04-identifikasi-tempat.html"><b>Identifikasi tempat</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-05-mengapa-lowercase-ditolak.html"><b>Mengapa lowercase ditolak?</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-06-pencarian-verifikasi.html"><b>Pencarian &amp; Verifikasi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
