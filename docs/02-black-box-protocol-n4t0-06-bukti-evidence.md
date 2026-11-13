# Black Box Protocol N4T0 — Bukti / Evidence

[← Overview](02-black-box-protocol-n4t0.md) · [Index](index.md)

> **Langkah 6/7 — Bukti / Evidence.** Timeline submit + dua screenshot form
> (flag diketik dan respons `CORRECT`).

## Bukti decode

```text
A: N4T0PH0N3T1C1N1
B: C0mbO_H3X_
C: fl0At_b4r4ng
```

Urutan yang benar adalah **A-B-C**:

```text
NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}
```

## Timeline verifikasi

| Waktu | Yang dicoba | Respons |
|---|---|---|
| 2026-11-07 14:50 WIB | urutan kolom salah `NFX{C0mbO_H3X_N4T0PH0N3T1C1N1}` | `Incorrect flag` |
| 2026-11-07 20:17 WIB | challenge di-update platform (`updated_at 13:17 UTC`) | — |
| 2026-11-13 | flag final `NFX{N4T0...}` | `Correct, but already solved.` |

## Screenshot form challenge

**Sebelum submit — flag final diketik:**

![Flag final diketik di form challenge](assets/black-box-protocol-n4t0/00b-platform-validation-before.png)

*Screenshot asli: input berisi
`NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}`.*

**Setelah submit — respons platform:**

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/black-box-protocol-n4t0/00b-platform-validation.png)

*Screenshot asli: banner `CORRECT, BUT ALREADY SOLVED.`. Input otomatis
dikosongkan setelah submit, lalu menampilkan placeholder `XXX{...}`; teks itu
bukan flag yang dikirim.*

## Terminal evidence (timeline submit)

![Timeline submit Black Box Protocol N4T0](assets/black-box-protocol-n4t0/00b-terminal-evidence.png)

*Arsip transkrip: kandidat urutan kolom salah ditolak, lalu flag final
diterima setelah challenge di-update.*

**Berkas mentah:** [`10-api-submit.txt`](assets/black-box-protocol-n4t0/10-api-submit.txt)

## Catatan

- Screenshot `00b-terminal-evidence.png` yang lama menampilkan percobaan
  kandidat urutan kolom salah dan `total_solves=0`; itu **bukan** flag final.
  Bukti itu sudah diganti dengan timeline yang membedakan kandidat salah dan
  flag final.
- Flag final diverifikasi ulang lewat API pada 2026-11-13:
  `{"success": true, "message": "Correct, but already solved."}`.
