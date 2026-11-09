# Bluebird Session

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Hard` |
| Poin | `420` |
| Author | `Ariaf` |
| Solves | `5` |
| Flag | `NFX{Mizore_Promise_Never_Forgotten_The_Bluebird_Still_Sings}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Evidence Linux: `/etc/passwd`, `/etc/shadow`, `/etc/group`, dua home (`mizore`, `nozomi`), keyring GNOME, `for_nozomi.zip`, `Ensemble.mp4`, dan log.
- Dua user utama: **mizore** (UID 1001, “Liz”) dan **nozomi** (UID 1002, “blue bird”).
- Hash SHA-512 crypt mizore (`$6$bluebird$...`) di-crack/verifikasi menjadi **`Bluebirds1927!`**.
- Password itu membuka `login.keyring`; item “Mizore Promise Note” berisi password **`MizoreCanFly2077!@`** untuk `for_nozomi.zip`.
- ZIP berisi 5 JPG + `README.txt`; salah satu gambar, `423261422632617826.jpg`, memuat overlay 32 hex.
- Hex32 `3220D64291CDFA4B26844C90690E8F1D` adalah jawaban Q11, **bukan** flag akhir.
- Setelah 11/11 Q&A selesai, platform mengembalikan flag final:
  `NFX{Mizore_Promise_Never_Forgotten_The_Bluebird_Still_Sings}`.

## Navigasi Halaman

- [Recon](25-bluebird-session-01-recon.md)
- [Analisis](25-bluebird-session-02-analisis.md)
- [Eksploitasi / Solver](25-bluebird-session-03-eksploitasi-solver.md)
- [Alur 11 Sub-Challenge Q&A (verified)](25-bluebird-session-04-alur-11-sub-challenge-q-a-verified.md)
- [Flag](25-bluebird-session-05-flag.md)
- [Bukti / Evidence](25-bluebird-session-06-bukti-evidence.md)
- [Referensi](25-bluebird-session-07-referensi.md)
