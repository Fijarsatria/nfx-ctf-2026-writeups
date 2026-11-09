# Broken Signature Scheme — Evidence / Bukti

[← Overview](18-broken-signature-scheme.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/broken-signature-scheme/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Transkrip / file pendukung

- [`solve.py`](assets/broken-signature-scheme/solve.py)
- [`solver-output.txt`](assets/broken-signature-scheme/solver-output.txt)
- [`verify-output.txt`](assets/broken-signature-scheme/verify-output.txt)
- [`verify.py`](assets/broken-signature-scheme/verify.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `challenge.py`, `output.txt` |
| Solver | `assets/broken-signature-scheme/solve.py` | Faktorisasi + AES-GCM |
| Output solver | `assets/broken-signature-scheme/solver-output.txt` | `p`, `q`, flag |
| Verifikasi 3 layer | `assets/broken-signature-scheme/verify.py` / `verify-output.txt` | L1/L2/L3 |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |
