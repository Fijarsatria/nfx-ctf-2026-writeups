# Invoice — Jejak awal

[← Overview](74-invoice.md) · [Index](index.md)

> **Langkah 1/5.** `zsteg` pada `b1,rgb,lsb,xy` mengeluarkan satu string base64.
>
> **Berikutnya:** [Cara Mendapatkan Flag](74-invoice-02-cara-mendapatkan-flag.md)

```bash
zsteg invoice.png | head
```

Baris yang dipakai:

```text
b1,rgb,lsb,xy .. text: "QzI9MTg1LjIyMC4xMDEuNDU6NDQ0NDtLRVk9YTFiMmMzO05YQ1RGe2w1Yl9sMDRkNV90aDNfcDR5bDA0ZH0K"
```

Baris kanal lain adalah noise. Jangan mengikuti semuanya.
