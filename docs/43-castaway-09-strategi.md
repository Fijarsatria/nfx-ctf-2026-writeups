# Castaway — Strategi

[← Overview](43-castaway.md) · [Index](index.md)

## 3.1 Strategi

1. Ekstrak `sbox256` (256 byte), `sbox16` (16 byte), dan ciphertext (40 byte) dari `.rodata`.
2. Untuk tiap byte `i`, coba semua 256 nilai plaintext `p`; hitung transformasi forward dengan `key` saat ini; pilih `p` yang menghasilkan ciphertext `target`.
3. Setelah ketemu, update `key` memakai `target` (karena update key memakai output byte).
4. Untuk byte pertama, coba dua kemungkinan: `target = ct[0]` (anti_debug = 0) dan `target = ct[0] ^ 1` (anti_debug = 1). Pilih hasil yang seluruhnya printable.
5. Verifikasi dengan menjalankan binary tanpa debugger.

Karena S-box 256 byte belum tentu permutasi, brute force 256 kandidat lebih aman daripada mencoba menginversi S-box secara langsung. Pada challenge ini setiap byte menghasilkan tepat satu kandidat.

### Evidence langkah ini

![term-01-identitas.png](assets/castaway/term-01-identitas.png)

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

![term-02-readelf.png](assets/castaway/term-02-readelf.png)

*Terminal evidence — `02-readelf.txt` (arsip transkrip sesi solve).*

![term-03-strings.png](assets/castaway/term-03-strings.png)

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*

![term-04-disasm.png](assets/castaway/term-04-disasm.png)

*Terminal evidence — `04-disasm.txt` (arsip transkrip sesi solve).*

![term-05-rodata-data-hexdump.png](assets/castaway/term-05-rodata-data-hexdump.png)

*Terminal evidence — `05-rodata-data-hexdump.txt` (arsip transkrip sesi solve).*

![term-06-solver-output.png](assets/castaway/term-06-solver-output.png)

*Terminal evidence — `06-solver-output.txt` (arsip transkrip sesi solve).*

![term-07-verifikasi.png](assets/castaway/term-07-verifikasi.png)

*Terminal evidence — `07-verifikasi.txt` (arsip transkrip sesi solve).*

![term-08-antidebug-gdb-strace.png](assets/castaway/term-08-antidebug-gdb-strace.png)

*Terminal evidence — `08-antidebug-gdb-strace.txt` (arsip transkrip sesi solve).*

![term-08-checksec.png](assets/castaway/term-08-checksec.png)

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

![term-castaway_in.png](assets/castaway/term-castaway_in.png)

*Terminal evidence — `castaway_in.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-identitas.txt`](assets/castaway/01-identitas.txt)
- [`02-readelf.txt`](assets/castaway/02-readelf.txt)
- [`03-strings.txt`](assets/castaway/03-strings.txt)
- [`04-disasm.txt`](assets/castaway/04-disasm.txt)
- [`05-rodata-data-hexdump.txt`](assets/castaway/05-rodata-data-hexdump.txt)
- [`06-solver-output.txt`](assets/castaway/06-solver-output.txt)
