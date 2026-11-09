# Gateway Under Pressure — Evidence / Bukti

[← Overview](37-gateway-under-pressure.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/gateway-under-pressure/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Transkrip / file pendukung

- [`01-file-hash-checksec.txt`](assets/gateway-under-pressure/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/gateway-under-pressure/02-disasm.txt)
- [`02b-stack.txt`](assets/gateway-under-pressure/02b-stack.txt)
- [`03-exploit-run.txt`](assets/gateway-under-pressure/03-exploit-run.txt)
- [`04-flag-status.txt`](assets/gateway-under-pressure/04-flag-status.txt)
- [`exploit.py`](assets/gateway-under-pressure/exploit.py)
- [`flag.txt`](assets/gateway-under-pressure/flag.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `writeups/assets/gateway-under-pressure/01-file-hash-checksec.txt` | `file`, sha256, checksec |
| Disassembly | `writeups/assets/gateway-under-pressure/02-disasm.txt` | `do_audit`, `do_dispatch`, `release_gateway`, `main` |
| Layout stack | `writeups/assets/gateway-under-pressure/02b-stack.txt` | Offset canary/RBP/RIP |
| Exploit | `writeups/assets/gateway-under-pressure/exploit.py` | pwntools |
| Output | `writeups/assets/gateway-under-pressure/03-exploit-run.txt` | Leak + ret2win |
| Flag/status | `writeups/assets/gateway-under-pressure/04-flag-status.txt` | Flag dari `flags/pwn/` |
