# NexaCommerce — Jejak awal

[← Overview](67-nexacommerce.md) · [Index](index.md)

> **Langkah 1/5.** Form login memasukkan `email` mentah ke query SQL.
>
> **Berikutnya:** [Cara Mendapatkan Flag](67-nexacommerce-02-cara-mendapatkan-flag.md)

Bukan UNION. Payload yang berhasil pada sesi ini adalah boolean bypass. Host `*.ngrok-free.dev` di transkrip hanya berlaku untuk sesi itu.

```text
email=' OR 1=1-- -&password=x
```

### Evidence langkah ini

![term-01-solve.png](assets/nexacommerce/term-01-solve.png)

*Terminal evidence — transkrip langkah — `term-01-solve.png`.*

**Berkas mentah terkait:**

- [`01-solve.txt`](assets/nexacommerce/01-solve.txt)
