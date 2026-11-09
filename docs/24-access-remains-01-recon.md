# Access Remains — Recon

[← Overview](24-access-remains.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> Sebuah workstation Windows diamankan dalam sebuah investigasi internal.
>
> Pengguna aslinya sudah tidak dapat dihubungi, tetapi jejak aktivitasnya masih tersisa di berbagai bagian sistem.
>
> Sebagian besar akses yang terlihat sudah tidak dapat digunakan, namun investigator mencurigai bahwa masih ada sesuatu yang tertinggal.
>
> Telusuri artifact yang tersedia, pulihkan apa yang masih dapat dipulihkan, dan cari tahu apa yang sebenarnya berusaha disimpan oleh pengguna tersebut.
>
> Note: Kumiko adalah waifu admin. Informasi ini mungkin relevan, mungkin juga tidak.
>
> pass: nxctf.id

### 1.2 File yang diberikan

Attachment: `Access_Remains.zip` (password zip `nxctf.id`) → `Evidence/`.

Struktur utama:

```text
Evidence/
├── Users/ariaf/
│   ├── NTUSER.DAT
│   ├── Documents/
│   │   ├── Kumiko.zip
│   │   ├── kumiko1.gif
│   │   ├── kumiko2.jpg
│   │   └── kumiko3.jpg
│   ├── AppData/Local/Microsoft/
│   │   ├── Credentials/DFBE70A7E5CC19A398EBF1B96859CE5D
│   │   └── Vault/4BF4C442-.../Policy.vpol
│   └── AppData/Roaming/Microsoft/
│       ├── Credentials/B0294E9651990C1435CA6300E4BB2378
│       ├── Protect/S-1-5-21-.../bb24f650-d046-439c-a88b-ab8f89ba61a4
│       └── Windows/Recent/*.lnk
└── Windows/System32/
    ├── config/{SAM,SYSTEM,SECURITY,SOFTWARE}
    └── winevt/Logs/{Application,Security,System}.evtx
```

Hash artefak utama:

```bash
$ sha256sum Evidence/Windows/System32/config/SAM \
            Evidence/Windows/System32/config/SYSTEM \
            Evidence/Users/ariaf/NTUSER.DAT \
            Evidence/Users/ariaf/AppData/Roaming/Microsoft/Protect/S-1-5-21-3304503823-3980900213-1333018566-1005/bb24f650-d046-439c-a88b-ab8f89ba61a4
030df1d12a46fa5fb18bfd4efd85b151905d19a835675f240e1e3f5fce293fae  SAM
debb833ff6a4eaba9368e8c9e1d0fbb58ac5a579b0d3c9a0032f4a0ccad17143  SYSTEM
1e63364f2c6e0d078345c8eabe23d99e552a0f9d0be23ea8ada36f849c443951  NTUSER.DAT
cf3122ac29bbed1bfd220e43dc19990c1fe20227a883d85b463a8d550a5a1124  bb24f650-...
```

### 1.3 Environment

- Linux
- `impacket-secretsdump`
- `impacket` DPAPI example: `/usr/share/doc/python3-impacket/examples/dpapi.py`
- `7z` (ZipCrypto)
- Python 3 + Pillow
- `regripper` (untuk sanity check registry)

### 1.4 Triage awal

`file` menunjukkan registry hive dan file DPAPI:

```text
SAM:        MS Windows registry file, NT/2000 or above
SYSTEM:     MS Windows registry file, NT/2000 or above
SECURITY:   MS Windows registry file, NT/2000 or above
NTUSER.DAT: MS Windows registry file, NT/2000 or above
bb24f650-...: data
B0294E...:    data
Kumiko.zip:   Zip archive data, at least v2.0 to extract, compression method=deflate
```

`Kumiko.zip` terlihat sebagai ZIP terenkripsi; `kumiko03.jpg` berukuran 98.795 byte dan akan menjadi kunci visual nanti.
