# Weak Handshake

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `360` |
| Author | `Ariaf` |
| Solves | `8` |
| Flag | `NFX{D36A64128F80788B60C677EF94FA7157}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `capture.pcapng` adalah capture loopback dengan FTP (port 2121/42345) dan dua sesi HTTPS ke port 8443.
- FTP mentransfer `clannad.webp` — “kenangan yang mudah terlihat di awal”; ini bukan flag.
- HTTPS memakai **TLS_RSA_WITH_AES_128_CBC_SHA (0x002f)** dengan sertifikat RSA **1024-bit** `CN=tomoyo.local`.
- Modulus RSA difaktorkan dengan **Fermat** karena `p` dan `q` hanya berselisih **236**; private key dipulihkan.
- Sesi memakai **Extended Master Secret** (extension `0x0017`), sehingga master secret dihitung dari `session_hash`, bukan `client_random+server_random`.
- Dua respons HTTPS didekripsi menjadi dua JPEG; JPEG kedua memuat overlay flag `{D36A64128F80788B60C677EF94FA7157}`.
- Flag: `NFX{D36A64128F80788B60C677EF94FA7157}`.

## Navigasi Halaman

- [Recon](27-weak-handshake-01-recon.md)
- [Analisis](27-weak-handshake-02-analisis.md)
- [Eksploitasi / Solver](27-weak-handshake-03-eksploitasi-solver.md)
- [Flag](27-weak-handshake-04-flag.md)
- [Bukti / Evidence](27-weak-handshake-05-bukti-evidence.md)
- [Referensi](27-weak-handshake-06-referensi.md)
