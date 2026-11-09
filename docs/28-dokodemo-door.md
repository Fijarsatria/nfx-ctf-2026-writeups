# Dokodemo Door

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Misc</span><span class="nx-chip">Medium</span><span class="nx-chip">160 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Medium` |
| Poin | `160` |
| Author | `Kada` |
| Solves | `18` |
| Tools | python3, strings |
| Flag | `NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/dokodemo-door/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## TL;DR

- `rahasia.pdf` bukan PDF lagi: seluruh byte di-XOR dengan **repeating key**
  sepanjang 16 byte.
- Karena PDF punya magic header `%PDF-1.4\n` dan trailer `%%EOF\n`, keduanya
  bisa dipakai sebagai *known plaintext* untuk menurunkan key.
- Key yang diperoleh: `nfx_k3tuk_p1ntu!`.
- Setelah didekripsi, file valid sebagai PDF 1.4; teks di halaman pertama
  memuat flag `NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}`.

<div class="nx-evidence-preview"><a href="28-dokodemo-door-08-bukti-evidence.html"><img src="assets/dokodemo-door/00b-submit-platform.png" alt="Pratinjau evidence Dokodemo Door" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="28-dokodemo-door-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="28-dokodemo-door-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="28-dokodemo-door-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="28-dokodemo-door-03-ekstraksi-teks-dari-pdf.html"><b>Ekstraksi teks dari PDF</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="28-dokodemo-door-04-strategi.html"><b>Strategi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="28-dokodemo-door-05-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="28-dokodemo-door-06-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="28-dokodemo-door-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="28-dokodemo-door-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="28-dokodemo-door-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
