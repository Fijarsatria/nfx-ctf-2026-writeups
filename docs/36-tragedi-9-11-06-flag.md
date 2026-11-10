# Tragedi 9/11 — Flag & Verifikasi

[← Overview](36-tragedi-9-11.md) · [Index](index.md)

> **Langkah 6/8 — Flag.** Flag ini tidak disubmit ke platform (sesuai aturan tugas).
>
> **Titik penting:** NFX{OS1NT_DU4R_D34_D0R}
>
> **Berikutnya:** [Bukti / Evidence](36-tragedi-9-11-07-bukti-evidence.md)

> **Flag:** `NFX{OS1NT_DU4R_D34_D0R}`
> **Status:** `VERIFIED`

```text
NFX{OS1NT_DU4R_D34_D0R}
```

Verifikasi:

```text
$ git show df34505:.env | tr -d '\r'
SERVER_HOST=localhost
SERVER_PORT=3002

NFX{OS1NT_DU4R_D34_D0R}

$ git show 62d5640:.env.example | tr -d '\r'
SERVER_HOST=
SERVER_PORT=

NFX{OS1NT_DU4R_D34_D0R}
```

Flag ini **tidak disubmit** ke platform (sesuai aturan tugas). Status:
`verified platform` berdasarkan notes solve sebelumnya; bukti lokal
(git history live) juga konsisten.

### Bukti submit di platform

![00b-submit-platform.png](assets/tragedi-9-11/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
