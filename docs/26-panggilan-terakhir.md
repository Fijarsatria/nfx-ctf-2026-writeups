# Panggilan Terakhir

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `380` |
| Author | `Candelena` |
| Solves | `7` |
| Flag | `NFXCTF{ARSIP_MERAH_204}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `korban.pcap` berisi satu panggilan SIP antara Raka (ext 204, `10.24.8.31`) dan Dina (ext 231, `10.24.8.24`).
- SDP menegosiasikan `RTP/AVP 0` = **PCMU/8000** (G.711 μ-law), RTP port 4000 ↔ 4002.
- RTP diekstrak per arah, di-decode μ-law menjadi WAV 8 kHz.
- Dina (stream 4002 → 4000) mengucapkan flag secara lisan: “NFXCTF, kurung kurawa buka, garis bawah, merah, garis bawah, 2 0 4, kurung kurawa tutup”.
- Flag: `NFXCTF{ARSIP_MERAH_204}`.

## Navigasi Halaman

- [Recon](26-panggilan-terakhir-01-recon.md)
- [Analisis](26-panggilan-terakhir-02-analisis.md)
- [Eksploitasi / Solver](26-panggilan-terakhir-03-eksploitasi-solver.md)
- [Flag](26-panggilan-terakhir-04-flag.md)
- [Bukti / Evidence](26-panggilan-terakhir-05-bukti-evidence.md)
- [Referensi](26-panggilan-terakhir-06-referensi.md)
