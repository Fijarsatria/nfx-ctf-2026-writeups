# Access Remains

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Forensics</span><span class="nx-chip">Hard</span><span class="nx-chip">360 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Hard` |
| Poin | `360` |
| Author | `Ariaf` |
| Solves | `8` |
| Tools | python3, exiftool, sage |
| Flag | `NFX{The_Real_Access_Was_Kumiko_All_Along}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Evidence Windows: `SAM`, `SYSTEM`, `SECURITY`, `NTUSER.DAT`, DPAPI masterkey, Credential Manager, dan `Kumiko.zip`.
- `secretsdump` menghasilkan NTLM user `aria` dan `ariaf`; NTLM di-crack menjadi `aria` dan `ariafe006`.
- Password `ariaf` membuka DPAPI masterkey `bb24f650-...`; Credential Manager menyimpan `AccessRemains:WaifuVault` dengan password `KumikoOumae2107!@`.
- Password tersebut membuka `Kumiko.zip` (ZipCrypto). Isinya foto-foto Kumiko dan `note.txt`.
- `note.txt` mengarah ke “one that remembers”; `kumiko03.jpg` memuat overlay teks 32 hex:
  `{3E2D6090E7EEB47D5` + `38FC27AC2789C02}`.
- Hex32 `3E2D6090E7EEB47D538FC27AC2789C02` adalah jawaban Q8, **bukan**
  flag akhir.
- Setelah 8/8 Q&A selesai, platform mengembalikan flag final:
  `NFX{The_Real_Access_Was_Kumiko_All_Along}`.

<div class="nx-evidence-preview"><a href="24-access-remains-06-bukti-evidence.html"><img src="assets/access-remains/98-terminal-evidence.png" alt="Pratinjau evidence Access Remains" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="24-access-remains-06-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="24-access-remains-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="24-access-remains-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="24-access-remains-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="24-access-remains-04-alur-8-sub-challenge-q-a-verified.html"><b>Alur 8 Sub-Challenge Q&amp;A (verified)</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="24-access-remains-05-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="24-access-remains-06-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="24-access-remains-07-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
