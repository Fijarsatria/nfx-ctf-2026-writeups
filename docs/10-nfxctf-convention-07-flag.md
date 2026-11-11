# NFXCTF Convention — Flag & Verifikasi

[← Overview](10-nfxctf-convention.md) · [Index](index.md)

> **Langkah 7/9 — Flag.** Flag
>
> **Titik penting:** NFX{h4ck3r_c0nv3nt10n_m4st3r_pwn3r_9988776655}
>
> **Berikutnya:** [Bukti / Evidence](10-nfxctf-convention-08-bukti-evidence.md)

> **Flag:** `NFX{h4ck3r_c0nv3nt10n_m4st3r_pwn3r_9988776655}`
> **Status:** `VERIFIED`

```text
NFX{h4ck3r_c0nv3nt10n_m4st3r_pwn3r_9988776655}
```

Verifikasi:

```text
$ cat flags/pwn/NFXCTF_Convention.txt
NFX{h4ck3r_c0nv3nt10n_m4st3r_pwn3r_9988776655}

$ sha256sum flags/pwn/NFXCTF_Convention.txt
(lihat assets/nfxctf-convention/04-flag-status.txt)
```

**Status:** `VERIFIED platform`. Flag sudah di-submit lewat form web platform
dan diterima. Screenshot submit ada di halaman Flag. Eksploit juga diverifikasi
lokal (shell + baca flag).

### Bukti submit di platform

![00b-submit-platform.png](assets/nfxctf-convention/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Bukti submit:** screenshot form challenge di atas menampilkan `CORRECT, BUT ALREADY SOLVED.`
