# Gateway Under Pressure

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin | `300` |
| Author | `Amablex` |
| Solves | `11` |
| Flag | `NFX{Nyoss_Gte3wayy_Pr3ssureee0!}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `gateway` adalah binary PIE dengan menu: register session, **audit memory**, dispatch request.
- `do_audit()` melakukan `write(1, buf, len)` dengan `len` yang dikendalikan pengguna (sampai `0x1000`) dari buffer stack `0x50` → **stack disclosure**: canary, saved RBP, dan return address PIE bocor.
- `do_dispatch()` melakukan `read_exact(buf, len)` dengan `len` sampai `0x200` ke buffer stack `0x50` tanpa validasi → **stack overflow**.
- Ada fungsi tersembunyi `release_gateway()` yang membuka `flag.txt` dan mencetak `FLAG: ...` (tidak dipanggil pada alur normal).
- Exploit: leak canary + PIE base dari audit, lalu ret2win `release_gateway()` dengan satu gadget `ret` untuk alignment.
- Flag: `NFX{Nyoss_Gte3wayy_Pr3ssureee0!}`.

## Navigasi Halaman

- [Recon](37-gateway-under-pressure-01-recon.md)
- [Analisis](37-gateway-under-pressure-02-analisis.md)
- [Eksploitasi](37-gateway-under-pressure-03-eksploitasi.md)
- [Flag](37-gateway-under-pressure-04-flag.md)
- [Bukti / Evidence](37-gateway-under-pressure-05-bukti-evidence.md)
- [Referensi](37-gateway-under-pressure-06-referensi.md)
