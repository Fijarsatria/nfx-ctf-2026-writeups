# Medium TEA

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `cypera` |
| Solves | `25` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings, sage |
| Flag | `NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Binary `medium_tea` memvalidasi flag 40 byte dari `argv[1]`.
- Algoritmanya **TEA 32 ronde**, tetapi empat round key-nya diganti konstanta “lucu”: `0x1337beef`, `0xcafebabe`, `0xdeadc0de`, `0x0badf00d`.
- Flag diproses per blok 64-bit (little-endian), dienkripsi, lalu dibandingkan dengan 5 blok ciphertext di `.rodata` `0x2040`.
- Karena TEA invertibel, dekripsi dilakukan dengan urutan ronde terbalik, `sum` dimulai dari `0xc6ef3720` dan dikurangi `delta` setiap ronde.
- Flag: `NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}`.

## Navigasi Halaman

- [Recon](47-medium-tea-01-recon.md)
- [Analisis](47-medium-tea-02-analisis.md)
- [Eksploitasi / Solver](47-medium-tea-03-eksploitasi-solver.md)
- [Flag](47-medium-tea-04-flag.md)
- [Bukti / Evidence](47-medium-tea-05-bukti-evidence.md)
- [Referensi](47-medium-tea-06-referensi.md)
