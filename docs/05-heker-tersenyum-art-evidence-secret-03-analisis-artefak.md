# Heker Tersenyum - Art Evidence Secret — Analisis Artefak

[← Overview](05-heker-tersenyum-art-evidence-secret.md) · [Index](index.md)

> **Langkah 3/9 — Analisis Artefak.** Kukuriuk99 adalah kandidat password/petunjuk tambahan.
>
> **Titik penting:** python3 - <<'PY'
>
> **Berikutnya:** [Ekstraksi LSB manual](05-heker-tersenyum-art-evidence-secret-04-ekstraksi-lsb-manual.md)

## 2.1 Metadata `PhotoLocation`

```bash
$ python3 - <<'PY'
import base64
s='SmFrYXJ0YSBTZWxhdGFuLCAxMzMwLCBSVyAyMCwgUlQgMTAsIFMzVnJkWEpwZFdzNU9RPT0='
d=base64.b64decode(s).decode()
print(d)
print(base64.b64decode(d.split(', ')[-1]))
PY
Jakarta Selatan, 1330, RW 20, RT 10, S3VrdXJpdWs5OQ==
b'Kukuriuk99'
```

`Kukuriuk99` adalah kandidat password/petunjuk tambahan. Pada challenge ini ia tidak dipakai untuk membuka container `CTF1`; flag tetap diperoleh dari jalur LSB.

## 2.2 Mengapa R dan B?

Pemeriksaan histogram:

```python
from PIL import Image
from collections import Counter
im = Image.open('00-original.png').convert('RGB')
c = Counter(im.getdata())
print(len(c), c.most_common(5))
```

```text
235 [(255,255,255), (0,0,0), (92,92,92), (220,220,220), (51,51,51)]
```

Tidak ada pixel dengan selisih kanal > 40; citra murni grayscale. Artinya kanal G sama dengan R/B pada area yang tidak dimodifikasi. Sisipan LSB dilakukan pada **R** dan **B**, sesuai “baju merah” dan “celana biru”.

`zsteg -a` tidak langsung menemukan teks karena payload bukan teks biasa:

```text
meta Comment        .. text: "The smallest details matter."
meta PhotoLocation  .. text: "SmFrYXJ0YSBTZWxhdGFuLCAxMzMwLCBSVyAyMCwgUlQgMTAsIFMzVnJkWEpwZFdzNU9RPT0="
imagedata           .. text: "HHH\r\r\rHHHAAA"
```
