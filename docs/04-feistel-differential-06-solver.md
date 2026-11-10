# Feistel Differential — Solver

[← Overview](04-feistel-differential.md) · [Index](index.md)

> **Langkah 6/9 — Solver.** Catatan: output pairs 6 adalah model underdetermined yang salah; sengaja ditampilkan untuk menunjukkan mengapa 7 pasangan dipakai.
>
> **Titik penting:** python3 writeups/assets/feistel-differential/solve.py · NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835} · NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835} (49 byte)
>
> **Berikutnya:** [Flag](04-feistel-differential-07-flag.md)

## 3.3 Output asli

```text
$ python3 writeups/assets/feistel-differential/solve.py
blocks [('0xa', 20000), ('0x5', 20000), ('0xa0', 20000), ('0x50', 20000), ('0xa00', 20000), ('0x500', 20000), ('0xa000', 20000), ('0x5000', 20000), ('0x5000000', 20000), ('0xa000000', 20000), ('0x50000000', 20000), ('0xa0000000', 20000), ('0x770000', 20000), ('0x550000', 20000)]
pairs 6 master 0xfdec721297377228d7783abfa383 block0 matches 11183 / 20000
pairs 7 master 0xfdec721297377222d7283ab5a383 block0 matches 20000 / 20000
VERIFY 280000 / 280000
FLAGPT b'NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}\x03\x03\x03'
```

Catatan: output `pairs 6` adalah model underdetermined yang **salah**; sengaja
ditampilkan untuk menunjukkan mengapa 7 pasangan dipakai. Model 7 pasangan
memenuhi seluruh 280.000 baris.

## 3.4 Padding

`flag.enc` berisi 52 byte. Plaintext hasil dekripsi 52 byte:

```text
NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}   (49 byte)
03 03 03                                           (PKCS#7, 3 byte)
```

Padding 3 byte mengikuti aturan PKCS#7 untuk blok 4-byte (vendor memakai
"blok" 32-bit), sehingga `03 03 03` dibuang.

### Evidence langkah ini

![term-solver-output.png](assets/feistel-differential/term-solver-output.png)

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`solver-output.txt`](assets/feistel-differential/solver-output.txt)
