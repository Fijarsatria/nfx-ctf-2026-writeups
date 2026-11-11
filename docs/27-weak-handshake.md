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

## Cerita singkat

Jadi ceritanya gini. `capture.pcapng` adalah capture loopback dengan FTP (port 2121/42345) dan dua sesi HTTPS ke port 8443. Terus, fTP mentransfer `clannad.webp` — “kenangan yang mudah terlihat di awal”; ini bukan flag. Lalu, HTTPS memakai **TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)** dengan sertifikat RSA **1024-bit** `CN=tomoyo.local`. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | sha256sum capture.pcapng | [Buka](27-weak-handshake-01-recon-artefak.md) |
| 2 | Analisis Artefak | file clannad.webp | [Buka](27-weak-handshake-02-analisis-artefak.md) |
| 3 | Analisis Artefak | openssl x509 -inform DER -in tomoyo_cert.der -noout -text | [Buka](27-weak-handshake-03-analisis-artefak-2.md) |
| 4 | Analisis Artefak | Decrypt dengan private key (PKCS#1 v1.5): | [Buka](27-weak-handshake-04-analisis-artefak-3.md) |
| 5 | Analisis Artefak | Setiap record setelah ChangeCipherSpec memiliki bentuk: | [Buka](27-weak-handshake-05-analisis-artefak-4.md) |
| 6 | Pemulihan Artefak | Script lengkap: assets/weak-handshake/solveweak.py. | [Buka](27-weak-handshake-06-pemulihan-artefak.md) |
| 7 | Output | — | [Buka](27-weak-handshake-07-output.md) |
| 8 | Flag | NFX{D36A64128F80788B60C677EF94FA7157} | [Buka](27-weak-handshake-08-flag.md) |
| 9 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](27-weak-handshake-09-bukti-evidence.md) |
| 10 | Referensi | — | [Buka](27-weak-handshake-10-referensi.md) |

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
