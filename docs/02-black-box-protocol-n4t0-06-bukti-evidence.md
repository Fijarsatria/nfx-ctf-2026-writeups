# Black Box Protocol N4T0 — Bukti / Evidence

[← Overview](02-black-box-protocol-n4t0.md) · [Index](index.md)

> **Langkah 6/7 — Bukti / Evidence.**
>
> **Titik penting:** screenshot `00b-terminal-evidence.png` adalah mockup;
> bukti asli adalah log API yang menunjukkan `Incorrect flag`.

## Bukti decode

```text
A: N4T0PH0N3T1C1N1
B: C0mbO_H3X_
C: fl0At_b4r4ng
```

## Bukti submit asli (log API)

```json
{"time":1794038881.9467971,
 "name":"BlackBox",
 "id":"f72a1790-01af-4e03-b789-00a949c8c270",
 "flag":"NFX{N4T0PH0N3T1C1N1_C0mbO_H3X}",
 "http":200,
 "result":{"success":false,"message":"Incorrect flag"}}
```

Kandidat lengkap juga ditolak. `total_solves = 0`.

## Terminal evidence (real)

`00b-terminal-evidence.png` sekarang adalah **capture terminal asli** dari API:

```text
$ python3 submit_curl.py f72a1790... 'NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}'
(200, {'success': False, 'message': 'Incorrect flag'})
```

Mockup lama yang menampilkan input dummy `XXX{...}`, `20 solves`, `120 pts`,
dan `CORRECT, BUT ALREADY SOLVED` sudah **dihapus**. Statistik platform asli:
`0 solves`, 500 pts dynamic.

## Kesimpulan

Status `OPEN / CANDIDATE`; tidak ada bukti flag accepted.
