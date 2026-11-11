# Gateway Under Pressure

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Pwn</span><span class="nx-chip">Medium</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Medium` |
| Poin | `300` |
| Author | `Amablex` |
| Solves | `11` |
| Tools | python3, pwntools, checksec, objdump, strings |
| Flag | `NFX{Nyoss_Gte3wayy_Pr3ssureee0!}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/gateway-under-pressure/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. `gateway` adalah binary PIE dengan menu: register session, **audit memory**, dispatch request. Terus, `do_audit()` melakukan `write(1, buf, len)` dengan `len` yang dikendalikan pengguna (sampai `0x1000`) dari buffer stack `0x50` → **stack disclosure**: canary, saved RBP, dan return address PIE bocor. Lalu, `do_dispatch()` melakukan `read_exact(buf, len)` dengan `len` sampai `0x200` ke buffer stack `0x50` tanpa validasi → **stack overflow**. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Petunjuk "fungsi yang tidak tersedia pada alur normal" sangat sesuai dengan fungsi releasegateway() yang ada di symbol table tetapi tidak dipanggil dari main(). | [Buka](37-gateway-under-pressure-01-recon.md) |
| 2 | Triage awal | file gateway | [Buka](37-gateway-under-pressure-02-triage-awal.md) |
| 3 | `do_audit()` — arbitrary-length stack read | Buffer hanya 0x50 byte (dari rbp-0x50 sampai rbp), tetapi write() membaca sampai 0x1000 byte. | [Buka](37-gateway-under-pressure-03-do-audit-arbitrary-length-stack-read.md) |
| 4 | Analisis | readexact membaca persis len byte (loop sampai terpenuhi) ke buffer 0x50. | [Buka](37-gateway-under-pressure-04-analisis.md) |
| 5 | Eksploitasi | python3 exploit.py \| tee 03-exploit-run.txt | [Buka](37-gateway-under-pressure-05-eksploitasi.md) |
| 6 | Flag | NFX{Nyoss_Gte3wayy_Pr3ssureee0!} | [Buka](37-gateway-under-pressure-06-flag.md) |
| 7 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](37-gateway-under-pressure-07-bukti-evidence.md) |
| 8 | Referensi | — | [Buka](37-gateway-under-pressure-08-referensi.md) |

## TL;DR

- `gateway` adalah binary PIE dengan menu: register session, **audit memory**, dispatch request.
- `do_audit()` melakukan `write(1, buf, len)` dengan `len` yang dikendalikan pengguna (sampai `0x1000`) dari buffer stack `0x50` → **stack disclosure**: canary, saved RBP, dan return address PIE bocor.
- `do_dispatch()` melakukan `read_exact(buf, len)` dengan `len` sampai `0x200` ke buffer stack `0x50` tanpa validasi → **stack overflow**.
- Ada fungsi tersembunyi `release_gateway()` yang membuka `flag.txt` dan mencetak `FLAG: ...` (tidak dipanggil pada alur normal).
- Exploit: leak canary + PIE base dari audit, lalu ret2win `release_gateway()` dengan satu gadget `ret` untuk alignment.
- Flag: `NFX{Nyoss_Gte3wayy_Pr3ssureee0!}`.

<div class="nx-evidence-preview"><a href="37-gateway-under-pressure-07-bukti-evidence.html"><img src="assets/gateway-under-pressure/00b-submit-platform.png" alt="Pratinjau evidence Gateway Under Pressure" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="37-gateway-under-pressure-07-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="37-gateway-under-pressure-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-03-do-audit-arbitrary-length-stack-read.html"><b>`do_audit()` — arbitrary-length stack read</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-04-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-05-eksploitasi.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-06-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-07-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-08-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
