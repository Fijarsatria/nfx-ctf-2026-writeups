# Frekuensi Sunyi — Penyelesaian

[← Overview](08-frekuensi-sunyi.md) · [Index](index.md)

## 3.1 Strategi

1. Baca WAV dan pastikan channel identik.
2. Kurangkan dua periode musik yang berulang.
3. Hitung STFT pada band 11–20 kHz.
4. Hilangkan harmonik dan baseline, lalu render sebagai gambar.
5. Transkripsi glyph secara manual, lalu ROT13.

## 3.2 Solver

```python
#!/usr/bin/env python3
# assets/frekuensi-sunyi/solve_frekuensi.py (ringkas)
from pathlib import Path
import codecs
import numpy as np
from PIL import Image
from scipy.io import wavfile
from scipy.ndimage import median_filter
from scipy.signal import stft

WAV = Path("/home/bocil/ctf/nfx/work/event/misc/frekuensi-sunyi/rekaman_lobi.wav")
OUT = Path("/home/bocil/ctf/nfx/writeups/assets/frekuensi-sunyi")
TRANSCRIPTION = "ASK{o0fP4_Pr01Y}"

fs, audio = wavfile.read(WAV)
print("sample rate           :", fs)
print("shape                 :", audio.shape, audio.dtype)
print("duration              :", round(audio.shape[0]/fs, 3), "s")
print("channels identical    :", np.array_equal(audio[:,0], audio[:,1]))

period = 2_268_000
mono = audio[:, 0].astype(np.float64)
residual = mono[period:2*period] - mono[:period]
segment = residual[:30*fs]

f, t, z = stft(segment, fs=fs, nperseg=2048, noverlap=1920, boundary=None)
band = (f >= 11500) & (f <= 19500)
s_db = 20*np.log10(np.abs(z[band]) + 1e-9)

b = s_db - median_filter(s_db, size=(9, 1))
b = b - median_filter(b, size=(1, 121))
lo, hi = np.percentile(b, 5), np.percentile(b, 95)
img = np.clip((b-lo)/(hi-lo)*255, 0, 255).astype(np.uint8)
Image.fromarray(np.flipud(img)).resize((2400, 700)).save(OUT/"01-spectrogram-repro.png")

print("manual transcription  :", TRANSCRIPTION)
print("ROT13                 :", codecs.decode(TRANSCRIPTION, "rot_13"))
```

### Evidence langkah ini

![term-05-audio-analysis.png](assets/frekuensi-sunyi/term-05-audio-analysis.png)

*Terminal evidence — `05-audio-analysis.txt` (arsip transkrip sesi solve).*

![04-text-crop.png](assets/frekuensi-sunyi/04-text-crop.png)

*Evidence — `04-text-crop.png`.*
