# Status verifikasi 9 writeup Crypto

| # | Challenge | Slug | Flag | Status | Bukti |
|---|---|---|---|---|---|
| 1 | Black Box Protocol N4T0 | `black-box-protocol-n4t0` | `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` | **CANDIDATE / DITOLAK** | `work/bb_submit_agent.jsonl` (53x incorrect) |
| 2 | Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh | `cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh` | `NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195}` | VERIFIED | `work/submit_curl_log.jsonl` |
| 3 | Feistel Differential | `feistel-differential` | `NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}` | VERIFIED | `work/verify_extra.jsonl` |
| 4 | RSA Coppersmith cihuy | `rsa-coppersmith-cihuy` | `NFXCTF{C0pp3rsm1th_p4rt14l_k3y_3xp0sur3_9617eda9}` | VERIFIED | `work/wave2_submit_parallel.jsonl` |
| 5 | Static IV Offline | `static-iv-offline` | `NXCTF{cbc_1v_r3u53_l34k5_k3y5tr34m_b0fbd4d35f80}` | VERIFIED | `work/wave2_submit_parallel.jsonl` |
| 6 | Broken Signature Scheme | `broken-signature-scheme` | `NXCTF{mult1_l4y3r_l4tt1c3_r54_s1gn4tur3_hnp_8c211ad6b5a6}` | VERIFIED | `work/wave2_submit_parallel.jsonl` |
| 7 | ECDSA Nonce Bias | `ecdsa-nonce-bias` | `NXCTF{ecds4_hnp_n0nc3_b14s_8b1t_l4tt1c3_a3d2ae498097}` | VERIFIED | `work/wave2_submit_parallel.jsonl` |
| 8 | FlagKeepers | `flagkeepers` | `NFX{gcm_f0rb1dd3n_4tt4ck_du4l_t4g_c0ll1s10n_m4st3r}` | VERIFIED (platform + live oracle) | `work/wave2_submit_parallel.jsonl`, `assets/flagkeepers/live_run.log` |
| 9 | Unbreakable Delay | `unbreakable-delay` | `NFX{x0r_f4ct0r1ng_4nd_f4st_vdf_byp4ss_m4k3s_1t_h4rd}` | VERIFIED (protokol `[REKONSTRUKSI]`) | `work/wave2_submit_parallel.jsonl` |

## Catatan

- **BlackBox:** payload workbook ter-decode 100% konsisten, tetapi flag
  tersimpan (`flags/crypto/BlackBoxProtocolN4T0.txt`) dan alternatif
  `work/release_map.json` sama-sama ditolak platform. Tidak ada klaim
  verified.
- **LWE:** secret LWE berhasil dipulihkan penuh (`b = A·s + e`, 64/64).
  Attachment tidak memuat kode KDF, sehingga dekripsi `ct` byte-exact tidak
  dapat direproduksi dari lampiran; flag diverifikasi lewat submit platform.
- **Unbreakable Delay:** tidak ada source/instance lokal; service historis
  sudah menolak koneksi. Protokol ditandai `[REKONSTRUKSI]`, demo solver
  memakai instance sintetis. Flag diverifikasi lewat submit platform.
