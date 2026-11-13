# Progress Bar (User) — Flag & Verifikasi

[← Overview](15-progress-bar-user.md) · [Index](index.md)

> **Langkah 8/10 — Flag.** Byte-exact dari target:
>
> **Titik penting:** NFX{pr0gr3ss_b4r_qu3u3_st4g1ng_pwn3d_4s_www_d4t4}
>
> **Berikutnya:** [Bukti / Evidence](15-progress-bar-user-09-bukti-evidence.md)

> **Asal flag.** Flag diperoleh dari langkah exploit/solver yang terdokumentasi, lalu disubmit ke platform.  

> **Flag:** `NFX{pr0gr3ss_b4r_qu3u3_st4g1ng_pwn3d_4s_www_d4t4}`
> **Status:** `VERIFIED`

```text
NFX{pr0gr3ss_b4r_qu3u3_st4g1ng_pwn3d_4s_www_d4t4}
```

### 4.1 Verifikasi lokal

```bash
sha256sum flags/b2r/ProgressBar_User.txt
# 417cbc99464eaa61e26a0357eea76c372371df762cbfca74efe2a87758c17f04

wc -c flags/b2r/ProgressBar_User.txt
# 50
```

Byte-exact dari target:

```text
base64: TkZYe3ByMGdyM3NzX2I0cl9xdTN1M19zdDRnMW5nX3B3bjNkXzRzX3d3d19kNHQ0fQo=
hex:    4e 46 58 7b 70 72 30 67 72 33 73 73 5f 62 34 72
        5f 71 75 33 75 33 5f 73 74 34 67 31 6e 67 5f 70
        77 6e 33 64 5f 34 73 5f 77 77 77 5f 64 34 74 34
        7d 0a
```

### 4.2 Bukti submit di platform

Flag diverifikasi via API; terminal evidence asli di bawah.
Respons yang muncul:

```text
CORRECT, BUT ALREADY SOLVED.
```

Terminal evidence:

![Terminal evidence (real)](assets/progress-bar-user/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/progress-bar-user/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*
