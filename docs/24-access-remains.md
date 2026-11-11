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

## Challenge Brief (platform)

![00-challenge-platform.png](assets/access-remains/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. evidence Windows: `SAM`, `SYSTEM`, `SECURITY`, `NTUSER.DAT`, DPAPI masterkey, Credential Manager, dan `Kumiko.zip`. Terus, `secretsdump` menghasilkan NTLM user `aria` dan `ariaf`; NTLM di-crack menjadi `aria` dan `ariafe006`. Lalu, password `ariaf` membuka DPAPI masterkey `bb24f650-...`; Credential Manager menyimpan `AccessRemains:WaifuVault` dengan password `KumikoOumae2107!@`. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Deskripsi challenge | — | [Buka](24-access-remains-01-deskripsi-challenge.md) |
| 2 | Recon Artefak | sha256sum Evidence/Windows/System32/config/SAM \ | [Buka](24-access-remains-02-recon-artefak.md) |
| 3 | Triage awal | file menunjukkan registry hive dan file DPAPI: | [Buka](24-access-remains-03-triage-awal.md) |
| 4 | SAM + SYSTEM + SECURITY → NTLM | impacket-secretsdump -sam SAM -system SYSTEM -security SECURITY local | [Buka](24-access-remains-04-sam-system-security-ntlm.md) |
| 5 | Analisis Artefak | python3 /usr/share/doc/python3-impacket/examples/dpapi.py masterkey \ | [Buka](24-access-remains-05-analisis-artefak.md) |
| 6 | Analisis Artefak | 7z x -y -p'KumikoOumae2107!@' Kumiko.zip | [Buka](24-access-remains-06-analisis-artefak-2.md) |
| 7 | Pemulihan Artefak | python3 /usr/share/doc/python3-impacket/examples/dpapi.py masterkey \ | [Buka](24-access-remains-07-pemulihan-artefak.md) |
| 8 | Alur 8 Sub-Challenge Q&A (verified) | NFX{The_Real_Access_Was_Kumiko_All_Along} | [Buka](24-access-remains-08-alur-8-sub-challenge-q-a-verified.md) |
| 9 | Flag | NFX{The_Real_Access_Was_Kumiko_All_Along} | [Buka](24-access-remains-09-flag.md) |
| 10 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](24-access-remains-10-bukti-evidence.md) |
| 11 | Referensi | — | [Buka](24-access-remains-11-referensi.md) |

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

<div class="nx-evidence-preview"><a href="24-access-remains-10-bukti-evidence.html"><img src="assets/access-remains/00b-submit-platform.png" alt="Pratinjau evidence Access Remains" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="24-access-remains-10-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="24-access-remains-01-deskripsi-challenge.html"><b>Deskripsi challenge</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="24-access-remains-02-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="24-access-remains-03-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="24-access-remains-04-sam-system-security-ntlm.html"><b>SAM + SYSTEM + SECURITY → NTLM</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="24-access-remains-05-analisis-artefak.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="24-access-remains-06-analisis-artefak-2.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="24-access-remains-07-pemulihan-artefak.html"><b>Pemulihan Artefak</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="24-access-remains-08-alur-8-sub-challenge-q-a-verified.html"><b>Alur 8 Sub-Challenge Q&amp;A (verified)</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="24-access-remains-09-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="24-access-remains-10-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="24-access-remains-11-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
