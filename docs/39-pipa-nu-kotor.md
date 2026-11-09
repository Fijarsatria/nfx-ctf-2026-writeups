# Pipa Nu Kotor

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Pwn</span><span class="nx-chip">Medium</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin | `300` |
| Author | `Amablex` |
| Solves | `11` |
| Tools | python3, pwntools, checksec, objdump, strings |
| Flag | `NFX{Si44aTehKuduSadarDip4lakSave3Jari1}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Service mengelola "pipa" (pipe) dengan operasi buka/tutup/tulis/baca/login.
- Struct pipa `malloc(0x18)` hanya menginisialisasi `data`, `capacity`, dan `readonly`; field `flags` di offset `0x14` **tidak diinisialisasi**.
- Setelah menulis ke pipa `rw`, `flags |= 0x10`. Saat pipa ditutup, chunk struct masuk tcache. Membuka pipa baru dengan mode `ro` mengalokasikan ulang chunk yang sama dan **flags basi 0x10 masih ada**.
- Pengecekan `if (readonly && !(flags & 0x10))` jadi lolos, sehingga `memcpy()` menulis ke `shadow_page` (password root hard-coded).
- Login dengan password baru → `cetak_flag()` membaca `flag.txt`.
- Flag: `NFX{Si44aTehKuduSadarDip4lakSave3Jari1}`.

<div class="nx-evidence-preview"><a href="39-pipa-nu-kotor-05-bukti-evidence.html"><img src="assets/pipa-nu-kotor/98-terminal-evidence.png" alt="Pratinjau evidence Pipa Nu Kotor" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="39-pipa-nu-kotor-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="39-pipa-nu-kotor-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-03-eksploitasi.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="39-pipa-nu-kotor-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
