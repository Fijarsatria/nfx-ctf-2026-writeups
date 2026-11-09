# Weak Handshake — Recon

[← Overview](27-weak-handshake.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> Beberapa kenangan mudah terlihat di awal.
>
> Namun ending-nya dikirim melalui koneksi terenkripsi, tersembunyi di balik handshake yang ternyata tidak cukup kuat untuk menjaganya.
> Awalnya mungkin terlihat jelas, tetapi ending milik Tomoyo masih menunggu di dalam capture.
>
> Temukan apa yang tertinggal.
>
> Format: NFX{}

### 1.2 File yang diberikan

| File | Ukuran | Keterangan |
|---|---:|---|
| `capture.pcapng` | 670.476 byte | pcapng, Linux cooked v2 |

Hash:

```bash
$ sha256sum capture.pcapng
de2f31ef3b6a57f63f65a31edfb20e455afd6030fa8b9040003268126be76562  capture.pcapng
```

### 1.3 Environment

- Linux
- `tcpdump` (membaca pcapng; `tshark` tidak tersedia)
- Python 3 + PyCryptodome + `cryptography`
- `openssl` untuk inspeksi sertifikat
- Pillow/ffmpeg untuk melihat JPEG

### 1.4 Triage awal

```bash
$ file capture.pcapng
pcap capture file, microsecond ts (little-endian) - version 2.4 (Linux cooked v2, capture length 262144)

$ tcpdump -nn -r capture.pcapng | head
18:22:56.345267 lo In IP 192.168.56.100 > 192.168.56.100: ICMP echo request...
18:23:03.481830 lo In IP 192.168.56.100.36538 > 192.168.56.100.2121: Flags [S]...
18:23:03.482777 lo In IP 192.168.56.100.2121 > 192.168.56.100.36538: Flags [P.] ... length 28
18:23:03.483255 lo In IP 192.168.56.100.36538 > 192.168.56.100.2121: Flags [P.] ... length 22
...
18:23:13.303188 lo In IP 192.168.56.100.56410 > 192.168.56.100.8443: Flags [S]...
18:23:17.504458 lo In IP 192.168.56.100.56422 > 192.168.56.100.8443: Flags [S]...
```

Flow utama:

| Port | Protokol | Isi |
|---|---|---|
| 2121 | FTP control | `pyftpdlib 2.2.0` |
| 42345 | FTP data | transfer `clannad.webp` (262.796 byte) |
| 8443 | TLS | dua sesi HTTPS (`56410`, `56422`) |
