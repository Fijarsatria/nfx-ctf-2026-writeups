# Frekuensi Sunyi

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Misc</span><span class="nx-chip">Medium</span><span class="nx-chip">180 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Misc` |
| Difficulty | `Medium` |
| Poin (snapshot) | `180` |
| Author | `Kesatria Baja Ringan` |
| Tools | python3 |
| Flag | `NFX{b0sC4_Ce01L}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/frekuensi-sunyi/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. attachment aslinya adalah `rekaman_lobi.wav`: PCM 16-bit, 44.100 Hz, stereo, durasi 120,09 detik, dan kedua kanal identik (mono duplikat). Terus, musik lobi berulang dengan periode **2.268.000 sampel** (±51,43 detik). Dua periode yang dikurangkan saling menghilangkan sebagian besar musik. Lalu, pada band **±11–20 kHz** terdapat teks yang "tidak untuk didengar": `ASK{o0fP4_Pr01Y}`. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | sha256sum work/event/misc/frekuensi-sunyi/rekaman_lobi.wav | [Buka](08-frekuensi-sunyi-01-recon.md) |
| 2 | Triage awal | file work/event/misc/frekuensi-sunyi/rekaman_lobi.wav | [Buka](08-frekuensi-sunyi-02-triage-awal.md) |
| 3 | Analisis | Musik latar berulang. | [Buka](08-frekuensi-sunyi-03-analisis.md) |
| 4 | Analisis | NFX{b0sC4_Ce01L} | [Buka](08-frekuensi-sunyi-04-analisis-2.md) |
| 5 | Penyelesaian | — | [Buka](08-frekuensi-sunyi-05-penyelesaian.md) |
| 6 | Output asli | python3 solve_frekuensi.py | [Buka](08-frekuensi-sunyi-06-output-asli.md) |
| 7 | Flag | NFX{b0sC4_Ce01L} | [Buka](08-frekuensi-sunyi-07-flag.md) |
| 8 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](08-frekuensi-sunyi-08-bukti-evidence.md) |
| 9 | Referensi | — | [Buka](08-frekuensi-sunyi-09-referensi.md) |

## Ringkasan

> Catatan metadata: `writeups/_manifest.json` mencatat 180 poin / 17 solves /
> author `syahril`, sedangkan `challenge.json` kerja dan report submit
> mencatat 460 poin / 3 solves / author `Kesatria Baja Ringan`. Nilai dari
> report submit (`+460`) dipakai di tabel ini; perbedaannya dicatat agar
> tidak menyesatkan.
## TL;DR

- Attachment aslinya adalah `rekaman_lobi.wav`: PCM 16-bit, 44.100 Hz, stereo,
  durasi 120,09 detik, dan kedua kanal identik (mono duplikat).
- Musik lobi berulang dengan periode **2.268.000 sampel** (±51,43 detik).
  Dua periode yang dikurangkan saling menghilangkan sebagian besar musik.
- Pada band **±11–20 kHz** terdapat teks yang "tidak untuk didengar":
  `ASK{o0fP4_Pr01Y}`.
- Teks itu adalah **ROT13** dari flag. ROT13 menghasilkan
  `NFX{b0sC4_Ce01L}`.
- Report solve sebelumnya juga mencatat tidak ada layer LSB, metadata, DTMF,
  Morse, atau payload tambahan; satu-satunya pesan adalah teks pada
  spektrogram.

<div class="nx-evidence-preview"><a href="08-frekuensi-sunyi-08-bukti-evidence.html"><img src="assets/frekuensi-sunyi/00b-terminal-evidence.png" alt="Pratinjau evidence Frekuensi Sunyi" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="08-frekuensi-sunyi-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="08-frekuensi-sunyi-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-03-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-04-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-05-penyelesaian.html"><b>Penyelesaian</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-06-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="08-frekuensi-sunyi-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
