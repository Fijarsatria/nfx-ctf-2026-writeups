# Kunci Sudo Sing Kesasar — Cara Mendapatkan Flag

[← Overview](78-kunci-sudo-sing-kesasar.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.**
>
> **Flag:** `NFX{Wh33W0kTh3Tok-k}`
> **Status:** `VERIFIED`

## Binary

Binary **tersedia** di bundle publik:

```text
work/upstream/qazwsx/pwn/KunciSudoSingKesasar.zip
└── peserta/kunci   (ELF 64-bit, non-PIE, not stripped)
```

```bash
unzip -o KunciSudoSingKesasar.zip -d kunci
file kunci/peserta/kunci
readelf -h kunci/peserta/kunci | grep Type
strings -n 5 kunci/peserta/kunci | grep -iE 'flag|sudo|ALL|rule'
```

Temuan:

- `Type: EXEC` (non-PIE), not stripped.
- String: `flag.txt`, `FLAG: %s`, `sudo - penjaga aturan sudoers`,
  `format rule : ALL ALL=(ALL) CMD`, `rule : `.
- `main` membaca rule ke stack `0x400`, lalu:
  - `malloc(len+1)` untuk rule,
  - `malloc(0x18)` untuk struct `{ char owner[16]; int uid; int suid; }`,
  - `snprintf(struct, 0x10, "%s", "user")`,
  - `struct->uid = 1000`, `struct->suid = 1000`,
  - `unescape_copy(rule, buf, len)`,
  - `strncmp(rule, "ALL", 3)`,
  - jika `struct->suid == 0` → `buka_kunci()` membaca `flag.txt`.

## Reproduksi lokal

```bash
cd kunci/peserta
echo TESTFLAG > flag.txt
printf 'ALL ALL=(ALL) /bin/sh\n' | ./kunci
```

Output normal:

```text
[-] sudo ditolak: uid=1000 suid=1000 (bukan root)
```

Bug ada di **parser rule / manajemen field struct** (bukan “memory leak token
reuse” seperti tulisan lama). Tujuan exploit: membuat `struct->suid == 0`
sehingga `buka_kunci()` mencetak isi `flag.txt`.

## Flag

Dari service:

```text
NFX{Wh33W0kTh3Tok-k}
```

> Catatan audit: klaim lama “memory leak, token reuse” tidak didukung binary.
> Binary dan static finding di atas adalah bukti yang bisa direproduksi.
