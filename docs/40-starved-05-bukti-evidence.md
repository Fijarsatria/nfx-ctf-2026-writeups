# Starved — Evidence / Bukti

[← Overview](40-starved.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/starved/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Transkrip / file pendukung

- [`01-file-hash-checksec.txt`](assets/starved/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/starved/02-disasm.txt)
- [`02b-seccomp.txt`](assets/starved/02b-seccomp.txt)
- [`02c-records.txt`](assets/starved/02c-records.txt)
- [`03-exploit-run.txt`](assets/starved/03-exploit-run.txt)
- [`03b-leak-probe.py`](assets/starved/03b-leak-probe.py)
- [`03b-leak-probe.txt`](assets/starved/03b-leak-probe.txt)
- [`03c-run-printable.txt`](assets/starved/03c-run-printable.txt)
- [`04-flag-status.txt`](assets/starved/04-flag-status.txt)
- [`exploit.py`](assets/starved/exploit.py)
- [`flag.txt`](assets/starved/flag.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `writeups/assets/starved/01-file-hash-checksec.txt` | PIE, canary, Full RELRO |
| Disassembly | `writeups/assets/starved/02-disasm.txt` | `leaker`, `main`, `setup_seccomp` |
| Seccomp decode | `writeups/assets/starved/02b-seccomp.txt` | Allow-list + `read` fd 0 |
| Layout stack | `writeups/assets/starved/02c-records.txt` | Offset canary/RBP/RIP |
| Leak probe | `writeups/assets/starved/03b-leak-probe.txt` | `%27`, `%29`, `%85` |
| Exploit | `writeups/assets/starved/exploit.py` | pwntools ORW |
| Output | `writeups/assets/starved/03-exploit-run.txt`, `03c-run-printable.txt` | Flag lokal + padding |
| Flag/status | `writeups/assets/starved/04-flag-status.txt` | Flag dari `flags/pwn/` |
