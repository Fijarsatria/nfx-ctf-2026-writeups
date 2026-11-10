# Access Remains — Recon Artefak

[← Overview](24-access-remains.md) · [Index](index.md)

> **Langkah 2/11 — Recon Artefak.** Attachment: AccessRemains.zip (password zip nxctf.id) → Evidence/.
>
> **Titik penting:** sha256sum Evidence/Windows/System32/config/SAM \
>
> **Berikutnya:** [Triage awal](24-access-remains-03-triage-awal.md)

## 1.2 File yang diberikan

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

## 1.3 Environment

- Linux
- `impacket-secretsdump`
- `impacket` DPAPI example: `/usr/share/doc/python3-impacket/examples/dpapi.py`
- `7z` (ZipCrypto)
- Python 3 + Pillow
- `regripper` (untuk sanity check registry)
