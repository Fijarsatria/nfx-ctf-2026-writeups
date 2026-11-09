# Hard VM Bytecode

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Hard` |
| Poin | `100` |
| Author | `cypera` |
| Solves | `21` |
| Flag | `NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `hard_vm` bukan validator biasa: ia adalah **interpreter bytecode** mini dengan 498 byte program di `.rodata` `0x2080`.
- Dispatch table di `0x2060` memetakan opcode: `1=LOAD`, `2=XOR`, `3=ADD`, `4=ROL`, `5=CMP`, `0xff=OK`, `0=HALT/gagal`.
- Setiap karakter flag diproses dengan pola 5 instruksi: `LOAD`, `XOR`, `ADD`, `ROL`, `CMP`.
- Dengan membalik urutan operasi (`CMP → ROL⁻¹ → ADD⁻¹ → XOR⁻¹`), semua 33 karakter dapat dipulihkan tanpa menjalankan binary.
- Flag: `NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}`.

## Navigasi Halaman

- [Recon](45-hard-vm-bytecode-01-recon.md)
- [Analisis](45-hard-vm-bytecode-02-analisis.md)
- [Eksploitasi / Solver](45-hard-vm-bytecode-03-eksploitasi-solver.md)
- [Flag](45-hard-vm-bytecode-04-flag.md)
- [Bukti / Evidence](45-hard-vm-bytecode-05-bukti-evidence.md)
- [Referensi](45-hard-vm-bytecode-06-referensi.md)
