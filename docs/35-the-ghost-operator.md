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

<div class="nx-evidence-preview"><a href="35-the-ghost-operator-05-bukti-evidence.html"><img src="assets/the-ghost-operator/98-terminal-evidence.png" alt="Pratinjau evidence The Ghost Operator" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="35-the-ghost-operator-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="35-the-ghost-operator-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="35-the-ghost-operator-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
