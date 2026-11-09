#!/usr/bin/env python3
"""Frekuensi Sunyi - reproduce the high-band spectrogram and ROT13 flag.

The supplied WAV is 44.1 kHz stereo with identical channels.  The lobby
music repeats every 2,268,000 samples; subtracting one period from the
next cancels most of the music.  The hidden text lives at ~11-20 kHz and
is transcribed visually from the STFT image.

Note: the archived helper used soundfile, which is not installed in this
environment.  This version uses scipy.io.wavfile and the same processing.
"""
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


def main() -> None:
    fs, audio = wavfile.read(WAV)
    print(f"sample rate           : {fs}")
    print(f"shape                 : {audio.shape} ({audio.dtype})")
    print(f"duration              : {audio.shape[0] / fs:.3f} s")
    print(f"channels identical    : {np.array_equal(audio[:, 0], audio[:, 1])}")

    period = 2_268_000
    mono = audio[:, 0].astype(np.float64)
    residual = mono[period:2 * period] - mono[:period]
    segment = residual[:30 * fs]

    f, t, z = stft(segment, fs=fs, nperseg=2048, noverlap=1920, boundary=None)
    band = (f >= 11500) & (f <= 19500)
    s_db = 20 * np.log10(np.abs(z[band]) + 1e-9)
    print(f"STFT                  : {z.shape}, band {f[band][0]:.0f}-{f[band][-1]:.0f} Hz")
    print(f"STFT time span        : {t[0]:.3f}-{t[-1]:.3f} s (relative to residual)")

    b = s_db - median_filter(s_db, size=(9, 1))   # remove horizontal harmonics
    b = b - median_filter(b, size=(1, 121))       # remove slow baseline
    lo, hi = np.percentile(b, 5), np.percentile(b, 95)
    img = np.clip((b - lo) / (hi - lo) * 255, 0, 255).astype(np.uint8)
    im = Image.fromarray(np.flipud(img)).resize((2400, 700))
    im.save(OUT / "01-spectrogram-repro.png")
    print(f"saved                 : {OUT / '01-spectrogram-repro.png'}")

    print(f"manual transcription  : {TRANSCRIPTION}")
    print(f"ROT13                 : {codecs.decode(TRANSCRIPTION, 'rot_13')}")


if __name__ == "__main__":
    main()
