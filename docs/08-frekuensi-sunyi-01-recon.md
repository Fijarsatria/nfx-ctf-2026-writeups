# Frekuensi Sunyi — Recon

[← Overview](08-frekuensi-sunyi.md) · [Index](index.md)

## 1.1 Deskripsi challenge

> **Author: Kesatria Baja Ringan**
>
> Musik lobi ini diputar setiap hari, dan tidak ada yang pernah merasa
> terganggu. Sampai suatu hari, seorang teknisi suara bilang ada yang
> "menempel" di dalamnya. Katanya, pesan itu tidak untuk didengar.

Petunjuk "tidak untuk didengar" mengarah kuat ke **spektrogram**: pesan
tidak dimaksudkan untuk telinga, tetapi untuk mata yang melihat domain
frekuensi.

## 1.2 File / service yang diberikan

| File/Service | Ukuran | Keterangan |
|---|---|---|
| `umum/Misc/frekuensi-sunyi/view` | 84.547 byte | Halaman HTML viewer Google Drive, **bukan** audio |
| `work/event/misc/frekuensi-sunyi/rekaman_lobi.wav` | 21.184.556 byte | Audio asli yang diunduh dari Drive |
| `flags/misc/Frekuensi_Sunyi_spectrogram.png` | 4.513.166 byte | Spektrogram bersih hasil solve sebelumnya |
| `flags/misc/Frekuensi_Sunyi.report.txt` | 2.111 byte | Report analisis dan status submit |

Hash:

```bash
$ sha256sum work/event/misc/frekuensi-sunyi/rekaman_lobi.wav
22746242af986a2b70a9f84774ba996eeb2ea6bff3fdba3716f3ab7e26acc166  rekaman_lobi.wav

$ sha256sum umum/Misc/frekuensi-sunyi/view
a556512ee8203fc4c080013303f496bef9a01902fe3e8a7766433f502c293dea  view
```

## 1.3 Environment

- OS: Linux x86-64.
- Tools: `file`, `sha256sum`, Python 3, `numpy`, `scipy`, `Pillow`.
- `soundfile` tidak terpasang di environment ini, sehingga solver yang
  diarsipkan (`soundfile`) diadaptasi memakai `scipy.io.wavfile`. Hasil
  pemrosesannya sama.
- Tidak ada service jaringan; challenge sepenuhnya offline.

### Evidence langkah ini

![01-spectrogram-repro.png](assets/frekuensi-sunyi/01-spectrogram-repro.png)

*Evidence — `01-spectrogram-repro.png`.*
