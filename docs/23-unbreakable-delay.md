# Unbreakable Delay

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Crypto</span><span class="nx-chip">Medium</span><span class="nx-chip">360 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin | `360` |
| Author | `Kad` |
| Solves | `8` |
| Tools | python3, sage, git |
| Flag | `NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/unbreakable-delay/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. challenge meminta **bukti Fiat–Shamir** untuk VDF `y = 2^(2^256) mod N`. Evaluasi naif membutuhkan `2^256` squaring berurutan — tidak mungkin. Terus, kunci bypass ada di nama flag: **XOR factoring** + **fast VDF bypass**. Lalu, jika `N` dapat difaktorkan (karena `p` dan `q` punya relasi XOR yang terstruktur), maka `φ(N)` diketahui. Dengan `φ(N)`, eksponen `2^256` dapat direduksi modulo `φ(N)`, dan `y` dihitung seketika. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | timeout 5 bash -c 'echo \| nc -v s1.nfx.my.id 43206' | [Buka](23-unbreakable-delay-01-recon.md) |
| 2 | Analisis | Verifiable Delay Function memungkinkan pihak lain memverifikasi bahwa suatu fungsi dievaluasi selama T langkah berurutan yang tidak dapat diparalelkan. | [Buka](23-unbreakable-delay-02-analisis.md) |
| 3 | Analisis | Setelah p,q diketahui: | [Buka](23-unbreakable-delay-03-analisis-2.md) |
| 4 | Solver | Karena instance asli tidak tersedia, dibuat instance sintetis dengan p XOR q = 2^300 untuk mendemonstrasikan seluruh matematika. | [Buka](23-unbreakable-delay-04-solver.md) |
| 5 | Output asli simulasi | python3 writeups/assets/unbreakable-delay/sim_vdf.py | [Buka](23-unbreakable-delay-05-output-asli-simulasi.md) |
| 6 | Flag | NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd} | [Buka](23-unbreakable-delay-06-flag.md) |
| 7 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](23-unbreakable-delay-07-bukti-evidence.md) |
| 8 | Referensi | — | [Buka](23-unbreakable-delay-08-referensi.md) |

## Ringkasan

> **Catatan artefak:** challenge ini **tidak punya file lampiran** di workspace
> dan service-nya sudah tidak menerima koneksi saat writeup ditulis
> (`tcp://s1.nfx.my.id:43206` → connection refused; inventaris mencatat port
> 1337/stopped). Karena itu bagian protokol ditandai **[REKONSTRUKSI]** dan
> demo solver di bawah adalah **simulasi**, bukan reproduksi instance asli.
> Flag-nya sendiri **terverifikasi** lewat submit platform.
## TL;DR

- Challenge meminta **bukti Fiat–Shamir** untuk VDF `y = 2^(2^256) mod N`.
  Evaluasi naif membutuhkan `2^256` squaring berurutan — tidak mungkin.
- Kunci bypass ada di nama flag: **XOR factoring** + **fast VDF bypass**.
- Jika `N` dapat difaktorkan (karena `p` dan `q` punya relasi XOR yang
  terstruktur), maka `φ(N)` diketahui. Dengan `φ(N)`, eksponen `2^256` dapat
  direduksi modulo `φ(N)`, dan `y` dihitung seketika.
- Bukti `π` juga dapat dipalsukan dengan cara yang sama:
  `π = x^(⌊T/l⌋ mod φ(N))`, lalu verifier memeriksa
  `π^l · x^(T mod l) ≡ y (mod N)`.
- Flag: `NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}`.

<div class="nx-evidence-preview"><a href="23-unbreakable-delay-07-bukti-evidence.html"><img src="assets/unbreakable-delay/00b-submit-platform.png" alt="Pratinjau evidence Unbreakable Delay" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="23-unbreakable-delay-07-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="23-unbreakable-delay-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-03-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-04-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-05-output-asli-simulasi.html"><b>Output asli simulasi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-06-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-07-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-08-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
