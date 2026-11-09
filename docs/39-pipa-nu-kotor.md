# Pipa Nu Kotor

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin | `300` |
| Author | `Amablex` |
| Solves | `11` |
| Flag | `NFX{Si44aTehKuduSadarDip4lakSave3Jari1}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Service mengelola "pipa" (pipe) dengan operasi buka/tutup/tulis/baca/login.
- Struct pipa `malloc(0x18)` hanya menginisialisasi `data`, `capacity`, dan `readonly`; field `flags` di offset `0x14` **tidak diinisialisasi**.
- Setelah menulis ke pipa `rw`, `flags |= 0x10`. Saat pipa ditutup, chunk struct masuk tcache. Membuka pipa baru dengan mode `ro` mengalokasikan ulang chunk yang sama dan **flags basi 0x10 masih ada**.
- Pengecekan `if (readonly && !(flags & 0x10))` jadi lolos, sehingga `memcpy()` menulis ke `shadow_page` (password root hard-coded).
- Login dengan password baru → `cetak_flag()` membaca `flag.txt`.
- Flag: `NFX{Si44aTehKuduSadarDip4lakSave3Jari1}`.

## Navigasi Halaman

- [Recon](39-pipa-nu-kotor-01-recon.md)
- [Analisis](39-pipa-nu-kotor-02-analisis.md)
- [Eksploitasi](39-pipa-nu-kotor-03-eksploitasi.md)
- [Flag](39-pipa-nu-kotor-04-flag.md)
- [Bukti / Evidence](39-pipa-nu-kotor-05-bukti-evidence.md)
- [Referensi](39-pipa-nu-kotor-06-referensi.md)
