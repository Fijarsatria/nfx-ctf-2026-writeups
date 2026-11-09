# THE FORGOTTEN STATE — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">1 screenshot</span><span class="nx-chip">8 transkrip / script</span></div>


[← Overview](42-the-forgotten-state.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/the-forgotten-state/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`01-file-hash-checksec.txt`](assets/the-forgotten-state/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/the-forgotten-state/02-disasm.txt)
- [`02b-record-layout.txt`](assets/the-forgotten-state/02b-record-layout.txt)
- [`02c-got.txt`](assets/the-forgotten-state/02c-got.txt)
- [`03-exploit-run.txt`](assets/the-forgotten-state/03-exploit-run.txt)
- [`04-flag-status.txt`](assets/the-forgotten-state/04-flag-status.txt)
- [`exploit.py`](assets/the-forgotten-state/exploit.py)
- [`flag.txt`](assets/the-forgotten-state/flag.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `writeups/assets/the-forgotten-state/01-file-hash-checksec.txt` | non-PIE, partial RELRO |
| Disassembly | `writeups/assets/the-forgotten-state/02-disasm.txt` | `op_create`, `op_release`, `op_view`, `op_edit`, `op_list` |
| Layout record/global | `writeups/assets/the-forgotten-state/02b-record-layout.txt` | `table`, `active`, field record |
| GOT | `writeups/assets/the-forgotten-state/02c-got.txt` | `free@got` |
| Exploit | `writeups/assets/the-forgotten-state/exploit.py` | Overflow + GOT hijack |
| Output | `writeups/assets/the-forgotten-state/03-exploit-run.txt` | Leak + shell + flag lokal |
| Flag/status | `writeups/assets/the-forgotten-state/04-flag-status.txt` | Flag dari `flags/pwn/` |