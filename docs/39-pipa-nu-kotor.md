# Pipa Nu Kotor

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Pwn</span><span class="nx-chip">Medium</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin (snapshot) | `300` |
| Author | `Amablex` |
| Solves | `11` |
| Tools | python3, pwntools, checksec, objdump, strings |
| Flag | `NFX{Si44aTehKuduSadarDip4lakSave3Jari1}` |
| Status | `VERIFIED` |
| Metode | **FULL** — metode utama berhasil direproduksi. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/pipa-nu-kotor/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. service mengelola "pipa" (pipe) dengan operasi buka/tutup/tulis/baca/login. Terus, struct pipa `malloc(0x18)` hanya menginisialisasi `data`, `capacity`, dan `readonly`; field `flags` di offset `0x14` **tidak diinisialisasi**. Lalu, setelah menulis ke pipa `rw`, `flags |= 0x10`. Saat pipa ditutup, chunk struct masuk tcache. Membuka pipa baru dengan mode `ro` mengalokasikan ulang chunk yang sama dan **flags basi 0x10 masih ada**. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Kata kunci dari deskripsi: "bagian ... | [Buka](39-pipa-nu-kotor-01-recon.md) |
| 2 | Triage awal | file pipa | [Buka](39-pipa-nu-kotor-02-triage-awal.md) |
| 3 | Analisis | opbuka() mengalokasikan malloc(0x18) untuk struct, lalu mengisi: | [Buka](39-pipa-nu-kotor-03-analisis.md) |
| 4 | Analisis | Saat free(struct) pada chunk 0x20, glibc menulis tcache->next di offset 0 dan tcache key di offset 8. | [Buka](39-pipa-nu-kotor-04-analisis-2.md) |
| 5 | Eksploitasi | python3 exploit.py \| tee 03-exploit-run.txt | [Buka](39-pipa-nu-kotor-05-eksploitasi.md) |
| 6 | Flag | NFX{Si44aTehKuduSadarDip4lakSave3Jari1} | [Buka](39-pipa-nu-kotor-06-flag.md) |
| 7 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](39-pipa-nu-kotor-07-bukti-evidence.md) |
| 8 | Referensi | — | [Buka](39-pipa-nu-kotor-08-referensi.md) |

## TL;DR

- Service mengelola "pipa" (pipe) dengan operasi buka/tutup/tulis/baca/login.
- Struct pipa `malloc(0x18)` hanya menginisialisasi `data`, `capacity`, dan `readonly`; field `flags` di offset `0x14` **tidak diinisialisasi**.
- Setelah menulis ke pipa `rw`, `flags |= 0x10`. Saat pipa ditutup, chunk struct masuk tcache. Membuka pipa baru dengan mode `ro` mengalokasikan ulang chunk yang sama dan **flags basi 0x10 masih ada**.
- Pengecekan `if (readonly && !(flags & 0x10))` jadi lolos, sehingga `memcpy()` menulis ke `shadow_page` (password root hard-coded).
- Login dengan password baru → `cetak_flag()` membaca `flag.txt`.
- Flag: `NFX{Si44aTehKuduSadarDip4lakSave3Jari1}`.

<div class="nx-evidence-preview"><a href="39-pipa-nu-kotor-07-bukti-evidence.html"><img src="assets/pipa-nu-kotor/00b-terminal-evidence.png" alt="Pratinjau evidence Pipa Nu Kotor" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="39-pipa-nu-kotor-07-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="39-pipa-nu-kotor-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-03-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-04-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-05-eksploitasi.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-06-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-07-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-08-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
