# Frekuensi Sunyi — Analisis

[← Overview](08-frekuensi-sunyi.md) · [Index](index.md)

### 2.1 Mencari periode pengulangan

Musik latar berulang. Dengan membandingkan dua segmen yang sama panjang,
musik yang identik akan saling menghilangkan dan menyisakan sinyal tambahan.

```python
period = 2_268_000                 # sampel
mono = audio[:, 0].astype(float)
residual = mono[period:2*period] - mono[:period]
```

Periode 2.268.000 sampel setara:

```text
2.268.000 / 44.100 = 51,4286 detik
```

Verifikasi korelasi lokal (2.000.000 sampel pertama vs lag yang sama):

```text
lag 2.266.000 -> 0.2527
lag 2.267.000 -> 0.2210
lag 2.268.000 -> 0.8322   <-- periode musik
lag 2.269.000 -> 0.2134
lag 2.270.000 -> 0.2486
```

Struktur RIFF juga bersih: hanya `fmt` (16 byte) dan `data`
(21.184.512 byte), tanpa trailing chunk.

```text
fmt  16
data 21184512
trailing bytes after chunks: 0
```

### 2.2 STFT pada band tinggi

Pesan terlihat sebagai glyph pada ±60–82 detik (relatif terhadap awal
residual). STFT dihitung pada band 11–20 kHz, lalu komponen harmonik
horizontal dihilangkan dengan median filter vertikal (frequency axis) dan
baseline lambat dihilangkan dengan median filter horizontal (time axis).

```python
from scipy.signal import stft
from scipy.ndimage import median_filter

f, t, z = stft(segment, fs=fs, nperseg=2048, noverlap=1920, boundary=None)
band = (f >= 11500) & (f <= 19500)
s_db = 20*np.log10(np.abs(z[band]) + 1e-9)

b = s_db - median_filter(s_db, size=(9, 1))    # buang garis harmonik
b = b - median_filter(b, size=(1, 121))        # buang baseline lambat
```

Contoh output parameter:

```text
sample rate           : 44100
shape                 : (5296128, 2) (int16)
duration              : 120.094 s
channels identical    : True
STFT                  : (1025, 10321), band 11520-19488 Hz
STFT time span        : 0.023-29.977 s (relative to residual)
```

### 2.3 Membaca glyph

Hasil gambar (lihat `04-text-crop.png`) menunjukkan deretan karakter:

```text
ASK{o0fP4_Pr01Y}
```

Pada pembacaan awal, harmonik musik yang tebal bisa membuat glyph saling
menyatu (misalnya `o0fP4` terbaca sebagai `OFFP4RT`, atau `{`/`_` terbaca
sebagai `4`/spasi). Karena itu, median filter vertikal `(9,1)` — atau
`(11,1)` pada report — penting: ia membuang garis-garis harmonik horizontal
yang menutupi huruf. Spektrogram bersih yang disimpan di
`flags/misc/Frekuensi_Sunyi_spectrogram.png` mengonfirmasi pembacaan ini.

### 2.4 ROT13

`ASK` adalah `NFX` setelah ROT13. Seluruh teks didekode:

```python
import codecs
codecs.decode("ASK{o0fP4_Pr01Y}", "rot_13")
```

```text
NFX{b0sC4_Ce01L}
```
