# Wujud Aseli Atmin — Recon

[← Overview](52-wujud-aseli-atmin.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Syahril**
>
> Foto dokumentasi dari event Oktober kemarin.
> Boleh dilihat, tapi jangan berhenti di situ doang!

Attachment:

```text
dokumentasi.png
https://drive.google.com/file/d/1UHvCZ3Wpk2mneOxIfPJN-_oVCeEnNVwT/view
```

### 1.2 File yang diberikan

| File | Ukuran | Keterangan |
|---|---:|---|
| `dokumentasi.png` | 1.328.704 byte | PNG 1280×960, RGB |
| `scan_07.dat` | 4.753 byte | diekstrak dari trailer ZIP |
| `catatan.txt` | 43 byte | decoy |

Hash:

```text
ab61ce519d0776ecae6695649c1a98d741b9cc2ded82e11a508305ae7385a3d9  dokumentasi.png
```

### 1.3 Triage awal

```bash
file dokumentasi.png
exiftool dokumentasi.png
binwalk dokumentasi.png
```

`exiftool` langsung memberi petunjuk:

```text
Warning : [minor] Trailer data after PNG IEND chunk
```

`binwalk` menemukan ZIP di trailer:

```text
extradata:0         .. file: Zip archive data, at least v2.0 to extract
00000000: 50 4b 03 04 14 00 00 00 08 00 05 2f  68 5d 1e 14  |PK........./h]..|
00000010: 65 a4 2b 00 00 00 2b 00 00 00 0b 00  00 00 63 61  |e.+...+.......ca|
00000020: 74 61 74 61 6e 2e 74 78  74 ...                    |tatan.txt...    |
```
