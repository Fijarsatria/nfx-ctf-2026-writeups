# Record Keeper (User) — Flag & Verifikasi

[← Overview](17-record-keeper-user.md) · [Index](index.md)

```text
NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}
```

Verifikasi lokal:

```bash
sha256sum flags/b2r/NexusRecordTransform_User.txt
# 849fc4aa022f84dac5481d7c33d228caac07ab64605ef9884ab581621c39fa4b

wc -c flags/b2r/NexusRecordTransform_User.txt
# 37
```

Byte-exact dari target:

```text
base64: TkZYe2JyMHRsMV8wb2Jfd3IxdDNfdzByazNyX3IwcF9yYzN9Cg==
hex:    4e 46 58 7b 62 72 30 74 6c 31 5f 30 6f 62 5f 77
        72 31 74 33 5f 77 30 72 6b 33 72 5f 72 30 70 5f
        72 63 33 7d 0a
```

### 4.1 Riwayat penolakan dan koreksi

Percobaan pertama memakai nilai yang salah transkripsi:

```text
NFX{br0tl1_0ob_w1r1t3_w0rk3r_r0p_rc3}
```

Perhatikan `w1r1t3` — ada tambahan angka `1`. Platform menjawab:

```json
{"success": false, "message": "Incorrect flag"}
```

Nilai yang benar di target adalah:

```text
NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}
```

Setelah dikoreksi, submit berhasil:

```json
{
  "id": "598dedd9-21d5-4946-bd8f-e47732c1fbd6",
  "title": "Record Keeper (User)",
  "flag": "NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}",
  "http": 200,
  "result": {"success": true, "message": "Correct! +500 points."}
}
```

Jadi penolakan pertama bukan karena flag target berubah, melainkan typo manual
saat menyalin. Hash file target (`849fc4...c39fa4b`) cocok dengan isi yang
akhirnya diterima.

Status: **verified platform**.

## Flag

`NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}`

**Status:** `VERIFIED`

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
