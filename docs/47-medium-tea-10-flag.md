# Medium TEA — Flag & Verifikasi

[← Overview](47-medium-tea.md) · [Index](index.md)

> **Langkah 10/12 — Flag.** Cek file flag lokal:
>
> **Titik penting:** NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}
>
> **Berikutnya:** [Bukti / Evidence](47-medium-tea-11-bukti-evidence.md)

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

Isi `flags/reverse/Medium_02_TEA.txt` juga identik dengan flag di atas. **Status: `VERIFIED platform`.** Flag sudah disubmit lewat web platform dan diterima (lihat screenshot submit); verifikasi lokal tetap dilakukan terhadap binary dan file flag.

### Bukti submit di platform

![00b-submit-platform.png](assets/medium-tea/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Bukti submit:** screenshot form challenge di atas menampilkan `CORRECT, BUT ALREADY SOLVED.`
