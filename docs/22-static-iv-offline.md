# Static IV Offline

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin | `140` |
| Author | `rio` |
| Solves | `19` |
| Flag | `NXCTF{cbc_1v_r3u53_l34k5_k3y5tr34m_b0fbd4d35f80}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `challenge.py` membocorkan `MASTER = b"\x13\x37" * 16` di source.
- Key AES-256-CBC diturunkan sebagai
  `SHA256(MASTER || counter.to_bytes(4, "little"))[:32]`.
- `output.txt` memberi `counter=11`, IV statis `aa...aa`, dan ciphertext.
- Karena semua bahan key tersedia, dekripsi langsung berhasil; plaintext
  berisi prefix `user-input-goes-here:|` diikuti flag.
- Flag: `NXCTF{cbc_1v_r3u53_l34k5_k3y5tr34m_b0fbd4d35f80}`.

## Navigasi Halaman

- [Recon](22-static-iv-offline-01-recon.md)
- [Analisis](22-static-iv-offline-02-analisis.md)
- [Eksploitasi / Solver](22-static-iv-offline-03-eksploitasi-solver.md)
- [Flag](22-static-iv-offline-04-flag.md)
- [Bukti / Evidence](22-static-iv-offline-05-bukti-evidence.md)
- [Referensi](22-static-iv-offline-06-referensi.md)
