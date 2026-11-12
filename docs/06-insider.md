# insider

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Medium</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `Zer0` |
| Tools | python3, exiftool, git |
| Flag | `NFX{wraithbyte_cve202421412_20250314_zenvpn271}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/insider/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. artefak hanya berupa profil Chrome (`ChromeProfile/`), tanpa disk image dan tanpa log server. Terus, `History` menunjukkan riset UAC bypass, CVE-2024-21412, download `uacme.zip`, dan login ke `0x00sec.org` dengan username **wraithbyte**. Lalu, `Login Data` menyimpan password `v10` (AES-GCM + DPAPI), tetapi **tidak ada master key DPAPI** di paket; password tidak perlu dipecahkan untuk mendapatkan flag. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | file evidence_nfx_phantom_insider.tar.gz | [Buka](06-insider-01-recon-artefak.md) |
| 2 | Recon Artefak | Petunjuk penting: timestamp Chrome/WebKit = microseconds sejak 1601-01-01 UTC. | [Buka](06-insider-02-recon-artefak-2.md) |
| 3 | Struktur profil | Profil atas nama Noah Fox (n.fox@nfx-aero.example), sesuai acquisition note. | [Buka](06-insider-03-struktur-profil.md) |
| 4 | History: aktivitas tersangka | https://www.youtube.com/watch?v=dQw4w9WgXcQ | [Buka](06-insider-04-history-aktivitas-tersangka.md) |
| 5 | Analisis Artefak | https://github.com/ | [Buka](06-insider-05-analisis-artefak.md) |
| 6 | Analisis Artefak | 127.0.0.1 | [Buka](06-insider-06-analisis-artefak-2.md) |
| 7 | Pemulihan Artefak | python3 dump_insider.py | [Buka](06-insider-07-pemulihan-artefak.md) |
| 8 | Flag | NFX{wraithbyte_cve202421412_20250314_zenvpn271} | [Buka](06-insider-08-flag.md) |
| 9 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](06-insider-09-bukti-evidence.md) |
| 10 | Referensi | — | [Buka](06-insider-10-referensi.md) |

## TL;DR

- Artefak hanya berupa profil Chrome (`ChromeProfile/`), tanpa disk image dan tanpa log server.
- `History` menunjukkan riset UAC bypass, CVE-2024-21412, download `uacme.zip`, dan login ke `0x00sec.org` dengan username **wraithbyte**.
- `Login Data` menyimpan password `v10` (AES-GCM + DPAPI), tetapi **tidak ada master key DPAPI** di paket; password tidak perlu dipecahkan untuk mendapatkan flag.
- Extension non-webstore **ZenVPN 2.7.1** dan timestamp bookmark/search **20250314** melengkapi komponen flag.
- Flag disusun dari empat artefak: `wraithbyte` + `cve202421412` + `20250314` + `zenvpn271`.

<div class="nx-evidence-preview"><a href="06-insider-09-bukti-evidence.html"><img src="assets/insider/00b-terminal-evidence.png" alt="Pratinjau evidence insider" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="06-insider-09-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="06-insider-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="06-insider-02-recon-artefak-2.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="06-insider-03-struktur-profil.html"><b>Struktur profil</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="06-insider-04-history-aktivitas-tersangka.html"><b>History: aktivitas tersangka</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="06-insider-05-analisis-artefak.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="06-insider-06-analisis-artefak-2.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="06-insider-07-pemulihan-artefak.html"><b>Pemulihan Artefak</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="06-insider-08-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="06-insider-09-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="06-insider-10-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
