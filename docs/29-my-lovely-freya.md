# My Lovely Freya

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Misc</span><span class="nx-chip">Hard</span><span class="nx-chip">320 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Hard` |
| Poin | `320` |
| Author | `salep88` |
| Solves | `10` |
| Tools | python3, exiftool, openssl |
| Flag | `NFX{FR3Y4_MY_L0V3LY!}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

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

<div class="nx-evidence-preview"><a href="29-my-lovely-freya-05-bukti-evidence.html"><img src="assets/my-lovely-freya/98-terminal-evidence.png" alt="Pratinjau evidence My Lovely Freya" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="29-my-lovely-freya-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="29-my-lovely-freya-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="29-my-lovely-freya-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
