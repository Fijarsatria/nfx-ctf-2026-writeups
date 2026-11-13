# My Lovely Freya

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Misc</span><span class="nx-chip">Hard</span><span class="nx-chip">320 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Hard` |
| Poin (snapshot) | `320` |
| Author | `salep88` |
| Solves | `10` |
| Tools | python3, exiftool, openssl |
| Flag | `NFX{FR3Y4_MY_L0V3LY!}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/my-lovely-freya/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. attachment `FreyaSayangkuh` adalah **ZIP** berisi `freya_sayangkuh.png` dan `surat_untuk_freya.enc`. Terus, pNG mendeklarasikan tinggi **1200** baris, tetapi IDAT sebenarnya berisi **1536** baris. Ada **336 baris tersembunyi** di bawah gambar yang tidak pernah ditampilkan viewer PNG normal. Lalu, baris tersembunyi berisi gambar teks password: `<!HayamGoreng45@/>`. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | unzip -l FreyaSayangkuh | [Buka](29-my-lovely-freya-01-recon.md) |
| 2 | Triage awal | file FreyaSayangkuh | [Buka](29-my-lovely-freya-02-triage-awal.md) |
| 3 | Analisis | python3 extract_hidden.py | [Buka](29-my-lovely-freya-03-analisis.md) |
| 4 | Dekripsi | openssl enc -d -aes-256-cbc -md sha256 -pbkdf2 -iter 100000 \ | [Buka](29-my-lovely-freya-04-dekripsi.md) |
| 5 | Penyelesaian | openssl enc -d -aes-256-cbc -md sha256 -pbkdf2 -iter 100000 \ | [Buka](29-my-lovely-freya-05-penyelesaian.md) |
| 6 | Output asli | python3 extract_hidden.py | [Buka](29-my-lovely-freya-06-output-asli.md) |
| 7 | Flag | NFX{FR3Y4_MY_L0V3LY!} | [Buka](29-my-lovely-freya-07-flag.md) |
| 8 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](29-my-lovely-freya-08-bukti-evidence.md) |
| 9 | Referensi | — | [Buka](29-my-lovely-freya-09-referensi.md) |

## TL;DR

- Attachment `FreyaSayangkuh` adalah **ZIP** berisi `freya_sayangkuh.png`
  dan `surat_untuk_freya.enc`.
- PNG mendeklarasikan tinggi **1200** baris, tetapi IDAT sebenarnya berisi
  **1536** baris. Ada **336 baris tersembunyi** di bawah gambar yang tidak
  pernah ditampilkan viewer PNG normal.
- Baris tersembunyi berisi gambar teks password:
  `<!HayamGoreng45@/>`.
- Metadata PNG `Secret: QXlhbWdHb3Jlbmc0NQ==` adalah **decoy**; decode-nya
  `AyamgGoreng45` dan gagal dipakai untuk dekripsi.
- `surat_untuk_freya.enc` adalah format OpenSSL `Salted__`; dekripsi dengan
  **AES-256-CBC, PBKDF2, 100.000 iterasi, digest SHA-256**, password
  `<!HayamGoreng45@/>` menghasilkan surat:
  `NXCTF{FR3Y4_MY_L0V3LY!}`.
- Flag platform: `NFX{FR3Y4_MY_L0V3LY!}`.

<div class="nx-evidence-preview"><a href="29-my-lovely-freya-08-bukti-evidence.html"><img src="assets/my-lovely-freya/00b-terminal-evidence.png" alt="Pratinjau evidence My Lovely Freya" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="29-my-lovely-freya-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="29-my-lovely-freya-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-03-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-04-dekripsi.html"><b>Dekripsi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-05-penyelesaian.html"><b>Penyelesaian</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-06-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
