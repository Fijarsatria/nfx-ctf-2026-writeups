# Invoice — Cara mendapatkan flag

[← Overview](74-invoice.md) · [Index](index.md)

> **Langkah 2/5.** Base64 itu langsung berisi C2, key, dan flag.
>
> **Berikutnya:** [Flag](74-invoice-03-flag.md)

```python
import base64
s = "QzI9MTg1LjIyMC4xMDEuNDU6NDQ0NDtLRVk9YTFiMmMzO05YQ1RGe2w1Yl9sMDRkNV90aDNfcDR5bDA0ZH0K"
print(base64.b64decode(s).decode())
```

```text
C2=185.220.101.45:4444;KEY=a1b2c3;NXCTF{l5b_l04d5_th3_p4yl04d}
```

Prefix flag adalah `NXCTF`, bukan `NFX`.
