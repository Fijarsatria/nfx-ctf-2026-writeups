# Pipeline Phantom — Cara mendapatkan flag

[← Overview](82-pipeline-phantom.md) · [Index](index.md)

> **Langkah 2/5.** Prefix dari log Actions yang dicetak dengan spasi. Sufiks dari commit yang di-revert.
>
> **Berikutnya:** [Flag](82-pipeline-phantom-03-flag.md)

1. Actions log, run `40221200390`, job `121252951677`, baris 273:

```text
[DEBUG_PAYLOAD]: N F X { g h _ 4 c t 1 0 n s _ m 4 s k _ b y p 4 s s _
```

Masking CI gagal karena secret dicetak dengan spasi. Gabungkan tanpa spasi:

```text
NFX{gh_4ct10ns_m4sk_byp4ss_
```

2. Issue publik menunjuk commit yang di-revert `62d3ad55d0cd1d95c64fc0168e317b928b0b4d95`. File `config/c2_endpoint.json` di commit itu berisi fragmen `4nd_0rph4n_c0mm1t_l34k_9f82}`.

```text
NFX{gh_4ct10ns_m4sk_byp4ss_4nd_0rph4n_c0mm1t_l34k_9f82}
```

Log Actions mentah tidak ada di folder evidence. Halaman ini mengikuti report arsip.
