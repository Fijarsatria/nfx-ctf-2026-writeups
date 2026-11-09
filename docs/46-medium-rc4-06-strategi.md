# Medium RC4 — Strategi

[← Overview](46-medium-rc4.md) · [Index](index.md)

## 3.1 Strategi

1. Ekstrak key 19 byte dari `.rodata` `0x2021`.
2. Ekstrak ciphertext 42 byte dari `.rodata` `0x2060`.
3. Implementasikan RC4 (KSA + PRGA) di Python.
4. Jalankan `rc4(key, ciphertext)` untuk mendapatkan plaintext.
5. Verifikasi dengan menjalankan binary memakai plaintext tersebut.

Solver membaca binary lewat **program header `PT_LOAD`**, bukan hardcode offset file, sehingga tetap benar meskipun layout section berubah. Ini juga mendemonstrasikan cara mengambil data dari alamat virtual yang ditemukan di disassembly.

### Evidence langkah ini

![term-03-strings.png](assets/medium-rc4/term-03-strings.png)

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*
