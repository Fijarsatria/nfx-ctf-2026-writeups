# Black Box Protocol N4T0 — Flag & Verifikasi

[← Overview](02-black-box-protocol-n4t0.md) · [Index](index.md)

Flag challenge:

```text
NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}
```

### Verifikasi platform

Recheck 2026-11-09 memakai backend baru:

```text
$ python3 - <<'EOF'
import nx2
print(nx2.submit(
    "f72a1790-01af-4e03-b789-00a949c8c270",
    "NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}",
))
EOF
HTTP 200 {'success': True, 'message': 'Correct, but already solved.'}
```

Respons `Correct` menunjukkan flag hasil decode workbook cocok dengan
`challenge_flags` di platform. Status `already solved` muncul karena challenge
sudah pernah diselesaikan oleh akun ini.

### Riwayat pengujian backend lama

Log submit lama `work/bb_submit_agent.jsonl` berisi 53 percobaan ke backend
lama. Beberapa yang paling relevan:

```text
NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}   -> Incorrect flag
NFX{C0mbO_H3X_N4T0PH0N3T1C1N1}                  -> Incorrect flag   (release_map)
NFX{N4T0PH0N3T1C1N1_C0mbO_H3X_fl0At_b4r4ng}     -> Incorrect flag
NFX{N4T0PH0N3T1C1N1C0mbO_H3X_fl0At_b4r4ng}      -> Incorrect flag
NFX{Nato_Phonetic_Ini_Combo_Hex_Float_Barang}   -> Incorrect flag
```

Log ringkas:

```text
$ python3 - <<'EOF'
import json
for line in open('work/bb_submit_agent.jsonl'):
    d=json.loads(line)
    if d['result'].get('success'):
        print('SUCCESS', d)
EOF
(tidak ada output)
```

Semua percobaan lama ditolak. Perbedaan ini berasal dari backend/versi
challenge yang dipakai saat itu, bukan dari hasil decode workbook. Setelah
backend baru diuji ulang, flag yang sama diterima.

Kandidat alternatif yang pernah dicoba (tidak dipakai):

1. `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` — decode paling literal.
2. `NFX{C0mbO_H3X_N4T0PH0N3T1C1N1}` — yang tercatat di `work/release_map.json`.
3. `NFX{N4T0PH0N3T1C1N1_C0mbO_H3X_fl0At_b4r4ng}` — tanpa split A.
4. `NFX{N4T0PH0N3T1C1N1C0mbO_H3X_fl0At_b4r4ng}` — konkatenasi mentah.
5. `NFX{Nato_Phonetic_Ini_Combo_Hex_Float_Barang}` — de-leet.

## Flag

`NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}`

**Status:** `VERIFIED`

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
