# Heker Tersenyum - Art Evidence Secret

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Medium</span><span class="nx-chip">280 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `280` |
| Author | `salep88` |
| Tools | python3, strings, binwalk, exiftool, zsteg |
| Flag | `NFX{LSB_3ASY_OR_H4RD_IDK}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Attachment berupa PNG 1495×2424 yang seluruhnya grayscale, tetapi metadata `tEXt` menyimpan dua petunjuk: komentar “The smallest details matter.” dan `PhotoLocation` berisi base64 bertingkat.
- Decode base64 dua lapis menghasilkan lokasi fiktif dan string `Kukuriuk99` — petunjuk/password, bukan flag.
- Nama tim **LSB** + “baju merah, celana biru” adalah arahan langsung: baca **LSB channel Red dan Blue**.
- Ekstraksi LSB row-major dari kanal R dan B masing-masing menghasilkan container `CTF1` + panjang big-endian + payload biner.
- Container R berisi 108 byte payload, container B berisi 53 byte; keduanya high-entropy (tidak langsung terbaca sebagai teks).
- Flag final yang tercatat untuk challenge ini adalah `NFX{LSB_3ASY_OR_H4RD_IDK}`.

<div class="nx-evidence-preview"><a href="05-heker-tersenyum-art-evidence-secret-05-bukti-evidence.html"><img src="assets/heker-tersenyum-art-evidence-secret/98-terminal-evidence.png" alt="Pratinjau evidence Heker Tersenyum - Art Evidence Secret" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="05-heker-tersenyum-art-evidence-secret-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="05-heker-tersenyum-art-evidence-secret-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="05-heker-tersenyum-art-evidence-secret-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="05-heker-tersenyum-art-evidence-secret-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="05-heker-tersenyum-art-evidence-secret-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="05-heker-tersenyum-art-evidence-secret-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="05-heker-tersenyum-art-evidence-secret-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
