# Static IV Offline

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Crypto</span><span class="nx-chip">Medium</span><span class="nx-chip">140 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin | `140` |
| Author | `rio` |
| Solves | `19` |
| Tools | python3, sage |
| Flag | `NXCTF{cbc_1v_r3u53_l34k5_k3y5tr34m_b0fbd4d35f80}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- `challenge.py` membocorkan `MASTER = b"\x13\x37" * 16` di source.
- Key AES-256-CBC diturunkan sebagai
  `SHA256(MASTER || counter.to_bytes(4, "little"))[:32]`.
- `output.txt` memberi `counter=11`, IV statis `aa...aa`, dan ciphertext.
- Karena semua bahan key tersedia, dekripsi langsung berhasil; plaintext
  berisi prefix `user-input-goes-here:|` diikuti flag.
- Flag: `NXCTF{cbc_1v_r3u53_l34k5_k3y5tr34m_b0fbd4d35f80}`.

<div class="nx-evidence-preview"><a href="22-static-iv-offline-05-bukti-evidence.html"><img src="assets/static-iv-offline/98-terminal-evidence.png" alt="Pratinjau evidence Static IV Offline" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="22-static-iv-offline-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="22-static-iv-offline-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="22-static-iv-offline-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="22-static-iv-offline-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="22-static-iv-offline-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="22-static-iv-offline-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="22-static-iv-offline-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
