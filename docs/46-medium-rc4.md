# Medium RC4

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Reverse</span><span class="nx-chip">Medium</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `cypera` |
| Solves | `26` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings |
| Flag | `NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Binary `medium_rc4` adalah ELF x86-64 PIE, stripped, dan meminta flag lewat `argv[1]`.
- Program mengecek panjang input tepat `42` byte, lalu menjalankan **RC4** dengan key hardcoded `n0t_s3cur3_k3y_2026`.
- Ciphertext 42 byte disimpan di `.rodata` pada alamat `0x2060`; hasil enkripsi input dibandingkan dengan `memcmp`.
- Karena RC4 simetris, dekripsi memakai rutin yang sama dengan enkripsi. Cukup ekstrak key + ciphertext, jalankan RC4, selesai.
- Flag: `NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}`.

<div class="nx-evidence-preview"><a href="46-medium-rc4-05-bukti-evidence.html"><img src="assets/medium-rc4/98-terminal-evidence.png" alt="Pratinjau evidence Medium RC4" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="46-medium-rc4-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="46-medium-rc4-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="46-medium-rc4-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="46-medium-rc4-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="46-medium-rc4-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="46-medium-rc4-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="46-medium-rc4-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
