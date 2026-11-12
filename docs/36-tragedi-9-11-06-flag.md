# Tragedi 9/11 — Flag & Verifikasi

[← Overview](36-tragedi-9-11.md) · [Index](index.md)

> **Langkah 6/8 — Flag.** Flag ini sudah disubmit lewat web platform dan diterima.
>
> **Titik penting:** NFX{OS1NT_DU4R_D34_D0R}
>
> **Berikutnya:** [Bukti / Evidence](36-tragedi-9-11-07-bukti-evidence.md)

> **Asal flag.** Flag dari git history video, lalu disubmit lewat web.  
> **Tingkat bukti metode.** Terdokumentasi. [Buka Evidence](36-tragedi-9-11-07-bukti-evidence.md)

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

Flag sudah disubmit lewat web platform dan diterima (`CORRECT, BUT ALREADY SOLVED.`).

### Terminal evidence (real)

![Terminal evidence (real)](assets/tragedi-9-11/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).

### Bukti submit web

![Screenshot submit web](assets/tragedi-9-11/00b-submit-platform.png)

*Form challenge menampilkan `CORRECT, BUT ALREADY SOLVED.`*
