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

## TL;DR

- Artefak hanya berupa profil Chrome (`ChromeProfile/`), tanpa disk image dan tanpa log server.
- `History` menunjukkan riset UAC bypass, CVE-2024-21412, download `uacme.zip`, dan login ke `0x00sec.org` dengan username **wraithbyte**.
- `Login Data` menyimpan password `v10` (AES-GCM + DPAPI), tetapi **tidak ada master key DPAPI** di paket; password tidak perlu dipecahkan untuk mendapatkan flag.
- Extension non-webstore **ZenVPN 2.7.1** dan timestamp bookmark/search **20250314** melengkapi komponen flag.
- Flag disusun dari empat artefak: `wraithbyte` + `cve202421412` + `20250314` + `zenvpn271`.

<div class="nx-evidence-preview"><a href="06-insider-09-bukti-evidence.html"><img src="assets/insider/00b-submit-platform.png" alt="Pratinjau evidence insider" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="06-insider-09-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

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
