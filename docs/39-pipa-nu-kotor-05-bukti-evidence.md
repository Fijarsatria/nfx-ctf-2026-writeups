# Pipa Nu Kotor — Evidence / Bukti

[← Overview](39-pipa-nu-kotor.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/pipa-nu-kotor/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Transkrip / file pendukung

- [`01-file-hash-checksec.txt`](assets/pipa-nu-kotor/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/pipa-nu-kotor/02-disasm.txt)
- [`02b-struct.txt`](assets/pipa-nu-kotor/02b-struct.txt)
- [`03-exploit-run.txt`](assets/pipa-nu-kotor/03-exploit-run.txt)
- [`04-flag-status.txt`](assets/pipa-nu-kotor/04-flag-status.txt)
- [`exploit.py`](assets/pipa-nu-kotor/exploit.py)
- [`flag.txt`](assets/pipa-nu-kotor/flag.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `writeups/assets/pipa-nu-kotor/01-file-hash-checksec.txt` | no PIE, no canary, NX |
| Disassembly | `writeups/assets/pipa-nu-kotor/02-disasm.txt` | `op_buka`, `op_tulis`, `op_login`, `op_tutup`, `cetak_flag` |
| Layout struct | `writeups/assets/pipa-nu-kotor/02b-struct.txt` | Field dan offset flags |
| Exploit | `writeups/assets/pipa-nu-kotor/exploit.py` | Urutan open/write/close/reopen |
| Output | `writeups/assets/pipa-nu-kotor/03-exploit-run.txt` | Login root + flag lokal |
| Flag/status | `writeups/assets/pipa-nu-kotor/04-flag-status.txt` | Flag dari `flags/pwn/` |
