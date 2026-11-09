# The Alchemist's Sandbox

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Medium` |
| Poin | `240` |
| Author | `Illal` |
| Solves | `14` |
| Tools | python3, git |
| Flag | `NFXCTF{pyj41l_4st_4lch3my_vm_pwn_d84f216a}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `chall.py` mengevaluasi ekspresi Python di sandbox AST yang melarang
  angka, tanda kutip, import, lambda, comprehension, f-string, dan atribut
  yang diawali `_`.
- Namun `getattr(als, "__globals__")` bisa dipanggil jika nama atributnya
  dibangun secara dinamis. `als` adalah fungsi `_encrypt_vault`, sehingga
  `als.__globals__["_VAULT_STATE"]` membocorkan ciphertext.
- Payload 315 karakter tanpa angka/kutip membangun `__globals__` dan
  `_VAULT_STATE` dari `True` (1), bit shift, dan `chr`.
- `_VAULT_STATE` berisi 21 word 16-bit (42 byte flag) setelah **32 ronde**
  transformasi XOR/rotasi/permutasi.
- Inverse round dari 31 ke 0 memulihkan plaintext; enkripsi ulang
  memverifikasi hasilnya.
- Flag: `NFXCTF{pyj41l_4st_4lch3my_vm_pwn_d84f216a}`.

## Navigasi Halaman

- [Recon](32-the-alchemists-sandbox-01-recon.md)
- [Analisis](32-the-alchemists-sandbox-02-analisis.md)
- [Eksploitasi / Solver](32-the-alchemists-sandbox-03-eksploitasi-solver.md)
- [Flag](32-the-alchemists-sandbox-04-flag.md)
- [Bukti / Evidence](32-the-alchemists-sandbox-05-bukti-evidence.md)
- [Referensi](32-the-alchemists-sandbox-06-referensi.md)
