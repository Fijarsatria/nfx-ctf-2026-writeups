# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh — Recon

[← Overview](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Illal
>
> Vendor ini baru aja minggu lalu rilis key exchange *"post-quantum"*
> andalannya, terus ngomong gede: *"Yang ini mah mustahil dibobol, bro!"* 😏
>
> Eh, transkripnya malah berhasil kesadap dong, dan flag-nya ikut
> keenkripsi di sana. Semua datanya ada di file yang dikasih. Vendor bilang
> mustahil? Ya buktiin aja salah, senpai~ ⚔️

Petunjuk utama ada di judul: **LWE** dan **"small secret"**. Flag yang
diverifikasi juga mengandung `l4tt1c3_sm4ll_s3cr3t`.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `lwe.py` | 33.679 byte | `6a996ad10f8ee04aed2f3befe3f1268b2b4bff8c9d6c6740b2cd88db0a623e1c` |

### 1.3 Environment

- Python 3.12
- `fpylll` 0.6.4 (LLL/BKZ)
- Tidak perlu Sage; semua operasi cukup integer Python + fpylll.

### 1.4 Triage awal

```bash
$ head -5 lwe.py
q = 257
n = 40
m = 64
A = [
    [
        67,
        123,
```

```bash
$ tail -5 lwe.py
    "8c8d8b0001438bf68076c012df3bb170d82e882152d9c13ab813435e7e5ada38a9abfed5eec11cbfb4"
)
```

```python
>>> ns = {}; exec(open("lwe.py").read(), ns)
>>> ns.keys()
dict_keys(['__builtins__', 'q', 'n', 'm', 'A', 'b', 'ct'])
>>> len(ns["A"]), len(ns["A"][0]), len(ns["b"])
(64, 40, 64)
>>> ns["q"], ns["n"], ns["m"]
(257, 40, 64)
```

**Temuan:** file hanya berisi data; tidak ada fungsi enkripsi/dekripsi, tidak
ada komentar, tidak ada import. Artinya peserta harus mengenali struktur LWE
dari bentuk data.
