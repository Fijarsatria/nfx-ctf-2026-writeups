# Frekuensi Sunyi — Flag & Verifikasi

[← Overview](08-frekuensi-sunyi.md) · [Index](index.md)

```text
NFX{b0sC4_Ce01L}
```

Verifikasi:

```text
$ python3 -c 'import codecs; print(codecs.decode("ASK{o0fP4_Pr01Y}","rot_13"))'
NFX{b0sC4_Ce01L}

$ cat flags/misc/Frekuensi_Sunyi.txt
NFX{b0sC4_Ce01L}
```

Report submit (`flags/misc/Frekuensi_Sunyi.report.txt`) mencatat:

```text
VERIFIED FLAG (accepted by platform, submit log: Correct! +460 points):
  NFX{b0sC4_Ce01L}
```

## Flag

`NFX{b0sC4_Ce01L}`

**Status:** `VERIFIED`

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
