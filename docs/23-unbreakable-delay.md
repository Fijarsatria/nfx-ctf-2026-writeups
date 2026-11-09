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

<div class="nx-evidence-preview"><a href="23-unbreakable-delay-05-bukti-evidence.html"><img src="assets/unbreakable-delay/98-terminal-evidence.png" alt="Pratinjau evidence Unbreakable Delay" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="23-unbreakable-delay-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="23-unbreakable-delay-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="23-unbreakable-delay-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
