# Weak Handshake

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Forensics</span><span class="nx-chip">Medium</span><span class="nx-chip">360 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `360` |
| Author | `Ariaf` |
| Solves | `8` |
| Tools | exiftool, tshark, Wireshark, openssl |
| Flag | `NFX{D36A64128F80788B60C677EF94FA7157}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/weak-handshake/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## TL;DR

- `capture.pcapng` adalah capture loopback dengan FTP (port 2121/42345) dan dua sesi HTTPS ke port 8443.
- FTP mentransfer `clannad.webp` — “kenangan yang mudah terlihat di awal”; ini bukan flag.
- HTTPS memakai **TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)** dengan sertifikat RSA **1024-bit** `CN=tomoyo.local`.
- Modulus RSA difaktorkan dengan **Fermat** karena `p` dan `q` hanya berselisih **236**; private key dipulihkan.
- Sesi memakai **Extended Master Secret** (extension `0x0017`), sehingga master secret dihitung dari `session_hash`, bukan `client_random+server_random`.
- Dua respons HTTPS didekripsi menjadi dua JPEG; JPEG kedua memuat overlay flag `{D36A64128F80788B60C677EF94FA7157}`.
- Flag: `NFX{D36A64128F80788B60C677EF94FA7157}`.

<div class="nx-evidence-preview"><a href="27-weak-handshake-09-bukti-evidence.html"><img src="assets/weak-handshake/00b-submit-platform.png" alt="Pratinjau evidence Weak Handshake" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="27-weak-handshake-09-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="27-weak-handshake-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="27-weak-handshake-02-analisis-artefak.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="27-weak-handshake-03-analisis-artefak-2.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="27-weak-handshake-04-analisis-artefak-3.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="27-weak-handshake-05-analisis-artefak-4.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="27-weak-handshake-06-pemulihan-artefak.html"><b>Pemulihan Artefak</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="27-weak-handshake-07-output.html"><b>Output</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="27-weak-handshake-08-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="27-weak-handshake-09-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="27-weak-handshake-10-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
