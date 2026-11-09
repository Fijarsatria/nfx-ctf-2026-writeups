# Medium TEA — Flag & Verifikasi

[← Overview](47-medium-tea.md) · [Index](index.md)

> **Flag:** `NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}`
> **Status:** `VERIFIED`

```text
NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}
```

Cek file flag lokal:

```text
$ cat flags/reverse/Medium_02_TEA.txt
NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}
```

Verifikasi:

```text
$ ./reverse/Medium_02_TEA/medium_tea 'NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}'
Correct! TEA terpecahkan.
rc=0

$ ./reverse/Medium_02_TEA/medium_tea 'NFX{wrong}'
Wrong!
rc=1
```

Isi `flags/reverse/Medium_02_TEA.txt` juga identik dengan flag di atas. **Status: `VERIFIED platform`.** Flag sudah dicek ulang ke platform pada 2026-11-09 (`Correct, but already solved.`); verifikasi lokal tetap dilakukan terhadap binary dan file flag.

### Bukti submit di platform

![00b-submit-platform.png](assets/medium-tea/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*
