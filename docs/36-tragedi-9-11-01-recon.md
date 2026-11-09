# Tragedi 9/11 — Recon

[← Overview](36-tragedi-9-11.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: salep88**
>
> Jangan percaya bahwa semua yang berharga dapat ditemukan dengan melihat
> lebih dekat.
>
> Sebuah rekaman dari salah satu peristiwa paling kelam yang pernah terjadi
> di sebuah negara adidaya kembali beredar di internet. Di tengah kepulan
> asap dan kepanikan, seorang pria terlihat membantu seorang ibu yang nyaris
> terjebak dalam asap.
>
> Seorang pemilik toko kemudian meminta wanita tersebut masuk ke dalam
> tokonya untuk menyelamatkan diri.
> Rekaman itu dibagikan oleh seseorang di sebuah forum yang mungkin tidak
> asing bagi para pencari informasi.
> Jika kau menemukan videonya, jangan berhenti di sana.
> Perhatikan orang yang membagikannya.
>
> Gunakan nama tersebut untuk mencari jejak lain yang ditinggalkannya di
> dunia para pembuat perangkat lunak.
>
> Kau mungkin menemukan sebuah tempat yang tampaknya tidak menyimpan apa-apa.
> Tapi jangan hanya melihat apa yang ada sekarang.
>
> Format Flag: `NFX{your_flag_here}`

Petunjuk utama:

- “forum yang mungkin tidak asing” → **Reddit**.
- “jejak lain di dunia para pembuat perangkat lunak” → **GitHub**.
- “tempat yang tampaknya tidak menyimpan apa-apa” → repo yang terlihat
  kosong/bersih.
- “jangan hanya melihat apa yang ada sekarang” → **git history**.

### 1.2 File / service yang diberikan

| File/Service | Ukuran | Keterangan |
|---|---|---|
| `drive/view.mp4` | 35.738.008 byte | Video 9/11, 58,5 detik |
| `/tmp/opencode/skywriteups/writeups/13-tragedi-9-11.md` | 2.2 KB | Draft writeup sebelumnya |
| `flags/wave2/Tragedi_911.txt` | 24 byte | Flag |

Hash:

```bash
$ sha256sum drive/view.mp4
c617b4d71998d0def7afab221836f095b7b7db908443aef1cb717a7b1ba2101e  view.mp4
```

### 1.3 Environment

- OS: Linux x86-64.
- Tools: `ffprobe`, `ffmpeg`, `sha256sum`, `git`, `curl`, `python3`.
- Service publik: Reddit (diblokir dari environment ini), GitHub.
- Video: `drive/view.mp4` (hasil unduhan dari lampiran Google Drive).

### 1.4 Triage awal

```bash
$ file drive/view.mp4
ISO Media, MP4 Base Media v1 [IS0 14496-12:2003]

$ ffprobe -v error -show_format -show_streams drive/view.mp4
codec_name=h264        width=1920   height=1080
r_frame_rate=30/1      duration=58.500000
bit_rate=4751167       nb_frames=1755
codec_name=aac         duration=58.514000
format_name=mov,mp4    size=35738008
encoder=Lavf62.12.102
```

**Temuan:** video adalah rekaman asli berdurasi 58,5 detik, bukan slideshow
atau file rusak. Tidak ada metadata lokasi/timestamp yang bisa dipakai
langsung; pivot harus dilakukan dari isi video dan jejak unggahan.
