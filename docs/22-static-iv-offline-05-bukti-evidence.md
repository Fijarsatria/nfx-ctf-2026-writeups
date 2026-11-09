# Static IV Offline — Evidence / Bukti

[← Overview](22-static-iv-offline.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/static-iv-offline/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Transkrip / file pendukung

- [`solve.py`](assets/static-iv-offline/solve.py)
- [`solver-output.txt`](assets/static-iv-offline/solver-output.txt)
- [`verify-output.txt`](assets/static-iv-offline/verify-output.txt)
- [`verify.py`](assets/static-iv-offline/verify.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `challenge.py`, `output.txt` |
| Solver | `assets/static-iv-offline/solve.py` | AES-CBC decrypt + unpad |
| Output solver | `assets/static-iv-offline/solver-output.txt` | Flag |
| Verifikasi | `assets/static-iv-offline/verify-output.txt` | Key, plaintext, prefix |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |
