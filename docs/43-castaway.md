# Castaway

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Hard` |
| Poin | `100` |
| Author | `Kesatria Baja Ringan` |
| Solves | `22` |
| Flag | `NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `castaway` membaca calon flag dari **stdin** (`fgets`), bukan dari argumen.
- Panjang harus tepat **40 byte**. Program menjalankan transformasi per byte dengan **state machine**, **rolling key**, **S-box 256 byte**, dan **S-box 16 byte**.
- Ada **opaque predicate** `(i*i) & 3 == 2` yang selalu false, sehingga state `0x32` (yang akan menulis `0xff`) adalah dead code.
- Ada **anti-debug** `ptrace(PTRACE_TRACEME)`: jika return `-1` (dijalankan di bawah debugger), byte hasil transformasi pertama di-XOR `1`, sehingga flag benar tetap ditolak.
- Inversi dilakukan per byte dengan brute force 256 kandidat; key state dipulihkan berurutan dari ciphertext.
- Flag: `NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}`.

## Navigasi Halaman

- [Recon](43-castaway-01-recon.md)
- [Analisis](43-castaway-02-analisis.md)
- [Eksploitasi / Solver](43-castaway-03-eksploitasi-solver.md)
- [Flag](43-castaway-04-flag.md)
- [Bukti / Evidence](43-castaway-05-bukti-evidence.md)
- [Referensi](43-castaway-06-referensi.md)
