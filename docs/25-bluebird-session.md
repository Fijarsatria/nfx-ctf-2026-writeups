# Bluebird Session

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Forensics</span><span class="nx-chip">Hard</span><span class="nx-chip">420 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Hard` |
| Poin | `420` |
| Author | `Ariaf` |
| Solves | `5` |
| Tools | strings, exiftool |
| Flag | `NFX{Mizore_Promise_Never_Forgotten_The_Bluebird_Still_Sings}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Evidence Linux: `/etc/passwd`, `/etc/shadow`, `/etc/group`, dua home (`mizore`, `nozomi`), keyring GNOME, `for_nozomi.zip`, `Ensemble.mp4`, dan log.
- Dua user utama: **mizore** (UID 1001, “Liz”) dan **nozomi** (UID 1002, “blue bird”).
- Hash SHA-512 crypt mizore (`$6$bluebird$...`) di-crack/verifikasi menjadi **`Bluebirds1927!`**.
- Password itu membuka `login.keyring`; item “Mizore Promise Note” berisi password **`MizoreCanFly2077!@`** untuk `for_nozomi.zip`.
- ZIP berisi 5 JPG + `README.txt`; salah satu gambar, `423261422632617826.jpg`, memuat overlay 32 hex.
- Hex32 `3220D64291CDFA4B26844C90690E8F1D` adalah jawaban Q11, **bukan** flag akhir.
- Setelah 11/11 Q&A selesai, platform mengembalikan flag final:
  `NFX{Mizore_Promise_Never_Forgotten_The_Bluebird_Still_Sings}`.

<div class="nx-evidence-preview"><a href="25-bluebird-session-06-bukti-evidence.html"><img src="assets/bluebird-session/98-terminal-evidence.png" alt="Pratinjau evidence Bluebird Session" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="25-bluebird-session-06-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="25-bluebird-session-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="25-bluebird-session-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="25-bluebird-session-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="25-bluebird-session-04-alur-11-sub-challenge-q-a-verified.html"><b>Alur 11 Sub-Challenge Q&amp;A (verified)</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="25-bluebird-session-05-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="25-bluebird-session-06-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="25-bluebird-session-07-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
