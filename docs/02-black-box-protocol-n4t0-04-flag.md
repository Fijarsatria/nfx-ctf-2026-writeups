# Black Box Protocol N4T0 — Flag & Verifikasi

[← Overview](02-black-box-protocol-n4t0.md) · [Index](index.md)

Kandidat yang tersimpan:

```text
NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}
```

### Verifikasi (tidak berhasil)

Log submit backend baru `work/bb_submit_agent.jsonl` berisi 53 percobaan.
Beberapa yang paling relevan:

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

**Kesimpulan verifikasi:** tidak ada satu pun kandidat yang diterima. Flag
platform kemungkinan berbeda dari payload workbook (mis. typo pada saat
pembuatan challenge — sheet ini bahkan sudah mengandung typo `kusi` untuk
`kunci`). Status yang benar adalah **candidate / unverified**, bukan
`verified`.

Kandidat berurut keyakinan (semuanya sudah diuji dan ditolak):

1. `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` — decode paling literal.
2. `NFX{C0mbO_H3X_N4T0PH0N3T1C1N1}` — yang tercatat di `work/release_map.json`.
3. `NFX{N4T0PH0N3T1C1N1_C0mbO_H3X_fl0At_b4r4ng}` — tanpa split A.
4. `NFX{N4T0PH0N3T1C1N1C0mbO_H3X_fl0At_b4r4ng}` — konkatenasi mentah.
5. `NFX{Nato_Phonetic_Ini_Combo_Hex_Float_Barang}` — de-leet.

## Flag

`NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` *(candidate)*

**Status:** `CANDIDATE`
