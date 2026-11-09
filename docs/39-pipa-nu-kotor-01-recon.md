# Pipa Nu Kotor — Recon

[← Overview](39-pipa-nu-kotor.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> **Author: Amablex**
>
> Aya hiji sistem Linux anu dipaké pikeun ngolah data ngaliwatan mékanisme pipe. Sistem éta sakuduna bisa ngajaga data sangkan henteu robah sacara teu dihaja. Tapi, tim kaamanan manggihan yén aya bagian tina mékanisme panyimpenan data anu henteu diinisialisasi kalayan bener. Anjeun dibéri hiji binary simulasi pikeun nalungtik masalah éta. Panggihan kumaha kaayaan data dina mémori bisa mangaruhan hasil pamrosesan program.

Kata kunci dari deskripsi: **"bagian ... anu henteu diinisialisasi kalayan bener"** — persis field `flags` pada struct.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---|---|
| `pwn/PipaNuKotor/peserta/pipa` | 17.288 B | `a818163453fabb867899dfab2f09ee172b6cc3b2a0de1fb26ed071713e4909ca` |

Tidak ada libc tambahan; binary non-PIE dan statically addressed. Service asli terdaftar sebagai `NFX/PWNNXCTF-2026/PipaNuKotor` (TCP), saat penulisan berstatus stopped.

### 1.3 Environment

- Linux x86-64, glibc host 2.39.
- Tools: `file`, `sha256sum`, `strings`, `objdump`, `nm`, `pwntools`.
- Menjalankan lokal:
  ```bash
  cd pwn/PipaNuKotor/peserta
  ./pipa
  ```

### 1.4 Triage awal

```text
$ file pipa
pipa: ELF 64-bit LSB executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=f693b5b749dbcba76c4cce2bd3b56acb61900fd9,
for GNU/Linux 3.2.0, not stripped

$ checksec (pwntools)
RELRO:      Partial RELRO
Stack:      No canary found
NX:         NX enabled
PIE:        No PIE (0x400000)
SHSTK:      Enabled
IBT:        Enabled
Stripped:   No
```

`strings` memperlihatkan pesan yang menjadi petunjuk utama:

```text
flag.txt
[!] flag.txt tidak ditemukan di direktori kerja
FLAG: %s
/dev/urandom
$6$%02x%02x%02x%02x%02x%02x%02x%02x$
[-] halaman dilindungi (baca-saja): penulisan ditolak
[!] penulisan ke halaman proteksi BERHASIL (flags basi)
[+] login sebagai root - akses diberikan
[-] login gagal: password salah
shadow_page
```

String **"penulisan ke halaman proteksi BERHASIL (flags basi)"** adalah konfirmasi langsung bahwa programmer sadar ada jalur bypass flags basi.

Symbol penting:

```text
00000000004040e0 b shadow_page
0000000000404120 b tabel
000000000040142c t cetak_flag
00000000004014e4 t isi_shadow
0000000000401695 t op_buka
0000000000401843 t op_tutup
0000000000401910 t op_tulis
0000000000401b3d t op_login
```
