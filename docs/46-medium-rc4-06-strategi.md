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

![term-01-identitas.png](assets/medium-rc4/term-01-identitas.png)

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

![term-02-readelf.png](assets/medium-rc4/term-02-readelf.png)

*Terminal evidence — `02-readelf.txt` (arsip transkrip sesi solve).*

![term-03-strings.png](assets/medium-rc4/term-03-strings.png)

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*

![term-04-disasm.png](assets/medium-rc4/term-04-disasm.png)

*Terminal evidence — `04-disasm.txt` (arsip transkrip sesi solve).*

![term-05-rodata-data-hexdump.png](assets/medium-rc4/term-05-rodata-data-hexdump.png)

*Terminal evidence — `05-rodata-data-hexdump.txt` (arsip transkrip sesi solve).*

![term-06-solver-output.png](assets/medium-rc4/term-06-solver-output.png)

*Terminal evidence — `06-solver-output.txt` (arsip transkrip sesi solve).*

![term-07-verifikasi.png](assets/medium-rc4/term-07-verifikasi.png)

*Terminal evidence — `07-verifikasi.txt` (arsip transkrip sesi solve).*

![term-08-checksec.png](assets/medium-rc4/term-08-checksec.png)

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-identitas.txt`](assets/medium-rc4/01-identitas.txt)
- [`02-readelf.txt`](assets/medium-rc4/02-readelf.txt)
- [`03-strings.txt`](assets/medium-rc4/03-strings.txt)
- [`04-disasm.txt`](assets/medium-rc4/04-disasm.txt)
- [`05-rodata-data-hexdump.txt`](assets/medium-rc4/05-rodata-data-hexdump.txt)
- [`06-solver-output.txt`](assets/medium-rc4/06-solver-output.txt)
