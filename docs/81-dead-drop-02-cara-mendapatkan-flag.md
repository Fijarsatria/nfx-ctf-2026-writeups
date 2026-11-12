# Dead Drop — Cara mendapatkan flag

[← Overview](81-dead-drop.md) · [Index](index.md)

> **Langkah 2/5.** Decode header config. Branch remote tidak ada di zip dan tidak ada di transkrip.
>
> **Berikutnya:** [Flag](81-dead-drop-03-flag.md)

```python
raw = open(".git/config").read().split("extraheader = AUTHORIZATION: basic ", 1)[1].split()[0]
import base64
print(base64.b64decode(raw).decode().split(":", 1)[0])
```

Hasilnya diawali `x-access-token:github_pat_`. Itu token yang tertinggal di config lokal.

Nama flag (`g1t_c0nf1g_h34d3r_l34k_h1dd3n_br4nch_...`) mengatakan langkah berikutnya memakai token itu untuk membaca branch tersembunyi di remote. Transkrip arsip berhenti di header ini. Jangan menulis seolah branch itu ada di dalam zip.

Token lengkap tidak dicantumkan di halaman ini. Ambil dari attachment, decode sendiri, dan jangan memakainya di luar challenge.
