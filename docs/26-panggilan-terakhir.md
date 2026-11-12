# Panggilan Terakhir

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Forensics</span><span class="nx-chip">Medium</span><span class="nx-chip">380 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `380` |
| Author | `Candelena` |
| Solves | `7` |
| Tools | python3, tshark |
| Flag | `NFXCTF{arsip_merah_204}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/panggilan-terakhir/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. `korban.pcap` berisi satu panggilan SIP antara Raka (ext 204, `10.24.8.31`) dan Dina (ext 231, `10.24.8.24`). Terus, sDP menegosiasikan `RTP/AVP 0` = **PCMU/8000** (G.711 μ-law), RTP port 4000 ↔ 4002. Lalu, rTP diekstrak per arah, di-decode μ-law menjadi WAV 8 kHz. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | sha256sum korban.pcap | [Buka](26-panggilan-terakhir-01-recon-artefak.md) |
| 2 | SIP INVITE dan SDP | tcpdump -nn -r korban.pcap 'udp port 5060' -A | [Buka](26-panggilan-terakhir-02-sip-invite-dan-sdp.md) |
| 3 | Ekstraksi RTP | RTP header 12 byte, payload 160 byte (20 ms @ 8 kHz), total UDP payload 172 byte. | [Buka](26-panggilan-terakhir-03-ekstraksi-rtp.md) |
| 4 | Transkripsi | NFXCTF { ARSIP _ MERAH _ 204 } | [Buka](26-panggilan-terakhir-04-transkripsi.md) |
| 5 | Pemulihan Artefak | python3 solve_panggilan.py | [Buka](26-panggilan-terakhir-05-pemulihan-artefak.md) |
| 6 | Flag | NFXCTF{arsip_merah_204} | [Buka](26-panggilan-terakhir-06-flag.md) |
| 7 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](26-panggilan-terakhir-07-bukti-evidence.md) |
| 8 | Referensi | — | [Buka](26-panggilan-terakhir-08-referensi.md) |

## TL;DR

- `korban.pcap` berisi satu panggilan SIP antara Raka (ext 204, `10.24.8.31`) dan Dina (ext 231, `10.24.8.24`).
- SDP menegosiasikan `RTP/AVP 0` = **PCMU/8000** (G.711 μ-law), RTP port 4000 ↔ 4002.
- RTP diekstrak per arah, di-decode μ-law menjadi WAV 8 kHz.
- Dina (stream 4002 → 4000) mengucapkan flag secara lisan: “NFXCTF, kurung kurawa buka, garis bawah, merah, garis bawah, 2 0 4, kurung kurawa tutup”.
- Flag: `NFXCTF{arsip_merah_204}`.

<div class="nx-evidence-preview"><a href="26-panggilan-terakhir-07-bukti-evidence.html"><img src="assets/panggilan-terakhir/00b-terminal-evidence.png" alt="Pratinjau evidence Panggilan Terakhir" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="26-panggilan-terakhir-07-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="26-panggilan-terakhir-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-02-sip-invite-dan-sdp.html"><b>SIP INVITE dan SDP</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-03-ekstraksi-rtp.html"><b>Ekstraksi RTP</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-04-transkripsi.html"><b>Transkripsi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-05-pemulihan-artefak.html"><b>Pemulihan Artefak</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-06-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-07-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="26-panggilan-terakhir-08-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
