# Panggilan Terakhir — Transkripsi

[← Overview](26-panggilan-terakhir.md) · [Index](index.md)

## 2.3 Transkripsi

Audio di-upsample ke 16 kHz, lalu ditranskripsi dengan faster-whisper (`tiny`, `language=id`, `vad_filter=True`). Output mentah Dina (stream 4002 → 4000):

```text
[0.00-5.00] Gal, selinanya kamu tinggal di printer, terakhir.
[5.00-8.00] Kodanya masih kelihatan.
[8.00-13.00] NSXGTS, kurung kurawa buka,
[13.00-16.00] Garis bawah, merah, Garis bawah,
[16.00-19.00] 2.4 kurung kurawa tutu.
[19.00-22.00] Kalau besok pagi kamu nggak jelasin,
[22.00-25.00] aku kirim semuanya kekepalah kantor.
[25.00-29.00] Gal, aku udah simpan selinanya.
[30.00-33.00] Kamu kira aku bakal diam aja?
[33.00-36.00] Raka, jangan gila.
[36.00-39.00] Kita bisa ngomong baik baik.
[39.00-42.00] Halo, Raka?
[42.00-44.00] Kamu di depan pintu?
[44.00-47.00] Raka, jangan.
```

Raka (stream 4000 → 4002):

```text
[0.00-3.00] Din, kamu tahu kondidokumen itu dari mana?
[3.00-5.00] Aku simpan sendiri dilachi.
[5.00-7.00] Kamu bukalachi aku?
[7.00-10.00] Dinah, jangan main main.
[10.00-12.00] Hapu salinan itu sekarang.
[12.00-14.00] Dengarin aku.
[14.00-17.00] Kalau kamu bocorinko di itu, aku bunuh kamu.
[17.00-20.00] Aku keruang garsip sekarang.
```

Koreksi berdasarkan konteks dan flag:

| ASR | Koreksi |
|---|---|
| `NSXGTS` | `NFXCTF` (N-F-X-C-T-F) |
| `2.4` | `204` |
| `kurung kurawa buka/tutu` | `{` / `}` |
| `garis bawah` | `_` |
| `merah` | `MERAH` |

Rangkaian yang diucapkan Dina:

```text
NFXCTF { ARSIP _ MERAH _ 204 }
```
