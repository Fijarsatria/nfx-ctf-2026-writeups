# Broken Signature Scheme

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Crypto` |
| Difficulty | `Hard` |
| Poin | `180` |
| Author | `rio` |
| Solves | `17` |
| Tools | python3, sage |
| Flag | `NXCTF{mult1_l4y3r_l4tt1c3_r54_s1gn4tur3_hnp_8c211ad6b5a6}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

Challenge punya tiga lapisan:

1. **Signature RSA multiplicatif.** `sig(m) = m^d mod N` (tanpa hash).
   Target `give-me-the-flag` tepat sama dengan produk tiga pesan yang sudah
   ditandatangani, jadi signature target = produk ketiga signature.
2. **RSA close-prime + partial leak.** `q = nextprime(p + 2^300)`, sehingga
   `δ = q-p = 2^300 + g` dengan `g` kecil. Diskriminan
   `δ² + 4N = (p+q)²` harus kuadrat sempurna. Enumerasi `g < 200.000` dan
   filter 20 bit bocor di posisi 500 menemukan `p,q`.
3. **AES-GCM.** Key = `SHA256(p||q)`, lalu `decrypt_and_verify` membuka flag.

## Navigasi Halaman

- [Recon](18-broken-signature-scheme-01-recon.md)
- [Analisis](18-broken-signature-scheme-02-analisis.md)
- [Eksploitasi / Solver](18-broken-signature-scheme-03-eksploitasi-solver.md)
- [Flag](18-broken-signature-scheme-04-flag.md)
- [Bukti / Evidence](18-broken-signature-scheme-05-bukti-evidence.md)
- [Referensi](18-broken-signature-scheme-06-referensi.md)
