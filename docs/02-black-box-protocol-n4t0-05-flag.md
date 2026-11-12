# Black Box Protocol N4T0 — Flag

[← Overview](02-black-box-protocol-n4t0.md) · [Index](index.md)

> **Langkah 5/7 — Flag.**
>
> **Kandidat:** `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}`
> **Status:** `OPEN / CANDIDATE — ditolak`

## Kandidat

```text
NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}
```

## Hasil submit

Semua kandidat yang dicoba ditolak:

```json
{"name":"BlackBox","id":"f72a1790-01af-4e03-b789-00a949c8c270",
 "flag":"NFX{N4T0PH0N3T1C1N1_C0mbO_H3X}",
 "http":200,"result":{"success":false,"message":"Incorrect flag"}}
```

Kandidat lengkap dengan `_fl0At_b4r4ng` juga ditolak pada percobaan terpisah.
`total_solves` challenge = **0**, jadi belum ada solver publik.

## Bukti terminal (real)

`00b-terminal-evidence.png` sekarang adalah **capture terminal asli** dari log API:

```text
$ python3 submit_curl.py f72a1790... 'NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}'
(200, {'success': False, 'message': 'Incorrect flag'})
```

Screenshot mockup lama (`SOLVED · 120 pts · 20 solves`, input `XXX{...}`) sudah
dihapus. Statistik platform asli: `0 solves`, 500 pts dynamic.

## Status

`OPEN / CANDIDATE`. Flag accepted belum ditemukan.
