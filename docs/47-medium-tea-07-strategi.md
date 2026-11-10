# Medium TEA — Strategi

[← Overview](47-medium-tea.md) · [Index](index.md)

> **Langkah 7/12 — Strategi.** Strategi
>
> **Titik penting:** —
>
> **Berikutnya:** [Solver lengkap](47-medium-tea-08-solver-lengkap.md)

## 3.1 Strategi

1. Ekstrak 40 byte ciphertext dari `.rodata` `0x2040`.
2. Gunakan empat key word yang ditemukan dari disassembly.
3. Dekripsi tiap blok 8 byte dengan TEA inverse (32 ronde).
4. Gabungkan hasilnya, lalu verifikasi dengan binary.
5. Sebagai pemeriksaan tambahan, enkripsi ulang plaintext dan pastikan hasilnya sama persis dengan ciphertext.

### Evidence langkah ini

![term-01-identitas.png](assets/medium-tea/term-01-identitas.png)

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

![term-02-readelf.png](assets/medium-tea/term-02-readelf.png)

*Terminal evidence — `02-readelf.txt` (arsip transkrip sesi solve).*

![term-03-strings.png](assets/medium-tea/term-03-strings.png)

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*

![term-04-disasm.png](assets/medium-tea/term-04-disasm.png)

*Terminal evidence — `04-disasm.txt` (arsip transkrip sesi solve).*

![term-05-rodata-data-hexdump.png](assets/medium-tea/term-05-rodata-data-hexdump.png)

*Terminal evidence — `05-rodata-data-hexdump.txt` (arsip transkrip sesi solve).*

![term-06-solver-output.png](assets/medium-tea/term-06-solver-output.png)

*Terminal evidence — `06-solver-output.txt` (arsip transkrip sesi solve).*

![term-07-verifikasi.png](assets/medium-tea/term-07-verifikasi.png)

*Terminal evidence — `07-verifikasi.txt` (arsip transkrip sesi solve).*

![term-08-checksec.png](assets/medium-tea/term-08-checksec.png)

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-identitas.txt`](assets/medium-tea/01-identitas.txt)
- [`02-readelf.txt`](assets/medium-tea/02-readelf.txt)
- [`03-strings.txt`](assets/medium-tea/03-strings.txt)
- [`04-disasm.txt`](assets/medium-tea/04-disasm.txt)
- [`05-rodata-data-hexdump.txt`](assets/medium-tea/05-rodata-data-hexdump.txt)
- [`06-solver-output.txt`](assets/medium-tea/06-solver-output.txt)
