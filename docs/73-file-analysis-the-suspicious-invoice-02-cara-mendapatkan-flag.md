# File Analysis: The Suspicious Invoice — Cara mendapatkan flag

[← Overview](73-file-analysis-the-suspicious-invoice.md) · [Index](index.md)

> **Langkah 2/5.** Empat temuan dirangkai. Hyperlink `jarvis.example` adalah umpan.
>
> **Berikutnya:** [Flag](73-file-analysis-the-suspicious-invoice-03-flag.md)

```bash
unzip -p export word/_rels/settings.xml.rels
unzip -p export docProps/core.xml
```

| Bagian | Sumber | Nilai |
|---|---|---|
| filetype | magic ZIP / OOXML | `zip` |
| teknik | `attachedTemplate` eksternal, MITRE T1221 | `t1221` |
| domain | `http://cdn-jarvis-update.example/template.dotm` | `cdn-jarvis-update.example` |
| case | `cp:keywords` | `jarvis-ir-case-2026-0211` |

```text
NFX{zip_t1221_cdn-jarvis-update.example_jarvis-ir-case-2026-0211}
```

Hyperlink `https://jarvis.example/invoice` bukan domain yang dipakai flag.
