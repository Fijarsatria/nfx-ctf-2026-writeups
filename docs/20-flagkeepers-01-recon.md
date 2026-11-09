# FlagKeepers — Recon

[← Overview](20-flagkeepers.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> **FlagKeepers** adalah layanan audit dan pemulihan terenkripsi yang
> dibangun di atas enkripsi terautentikasi AES-GCM. Layanan ini
> mempertahankan dua konteks enkripsi independen — **kunci utama** untuk log
> audit dan **kunci cadangan** untuk pemulihan bencana — yang berbagi satu
> nonce sesi.
>
> Bisakah Anda mengeksploitasi penggunaan kembali nonce, mengeksploitasi
> struktur polinomial GHASH di atas GF(2^128), dan memalsukan payload valid
> ganda untuk mengekstrak flag utama?

Petunjuk sangat eksplisit: nonce reuse + GHASH + dual valid payload.

### 1.2 File yang diberikan

| File | Ukuran | SHA-256 |
|---|---:|---|
| `app.py` | 2.222 byte | `5a4aa4e5d0425fb479283507f049ca4f6a68c20bb6d62def758568dd868104ba` |

Tidak ada flag lokal di attachment; flag hanya keluar dari oracle.

### 1.3 Environment / service

- Python 3.12 + `pycryptodome`
- Live oracle saat solve: `tcp://s1.nfx.my.id:43210`
- Service bisa dijalankan lokal dengan `app.py` (butuh `/app/flag.txt`).

### 1.4 Triage awal

Bagian penting `app.py`:

```python
key_a = urandom(16)
key_b = urandom(16)
nonce = urandom(12)
idx = 0

def encrypt(key, pt):
    ct, tag = AES.new(key, AES.MODE_GCM, nonce=nonce).encrypt_and_digest(pt)
    return ct, tag

def decrypt(key, ct, tag):
    return AES.new(key, AES.MODE_GCM, nonce=nonce).decrypt_and_verify(ct, tag)
```

Menu:

```text
[1] Audit log  [2] Recovery log  [3] Sign  [4] Flag  [5] Exit
```

- `[1]` → `idx = (idx + 16) % 256`, enkripsi AUDIT dengan `key_a`.
- `[2]` → `idx = (idx - 16) % 256`, enkripsi RECOVERY dengan `key_b`.
- `[3]` → verifikasi signature di `key_a` (tidak dipakai).
- `[4]` → verifikasi payload di `key_b`; jika
  `b"admin = True" in msg[:idx]` dan `b"admin = False" not in msg`,
  cetak flag.

**Bug utama:** `nonce` dibuat sekali di awal proses dan dipakai ulang untuk
semua enkripsi, baik `key_a` maupun `key_b`.
