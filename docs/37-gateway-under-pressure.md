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

## TL;DR

- `gateway` adalah binary PIE dengan menu: register session, **audit memory**, dispatch request.
- `do_audit()` melakukan `write(1, buf, len)` dengan `len` yang dikendalikan pengguna (sampai `0x1000`) dari buffer stack `0x50` → **stack disclosure**: canary, saved RBP, dan return address PIE bocor.
- `do_dispatch()` melakukan `read_exact(buf, len)` dengan `len` sampai `0x200` ke buffer stack `0x50` tanpa validasi → **stack overflow**.
- Ada fungsi tersembunyi `release_gateway()` yang membuka `flag.txt` dan mencetak `FLAG: ...` (tidak dipanggil pada alur normal).
- Exploit: leak canary + PIE base dari audit, lalu ret2win `release_gateway()` dengan satu gadget `ret` untuk alignment.
- Flag: `NFX{Nyoss_Gte3wayy_Pr3ssureee0!}`.

<div class="nx-evidence-preview"><a href="37-gateway-under-pressure-05-bukti-evidence.html"><img src="assets/gateway-under-pressure/98-terminal-evidence.png" alt="Pratinjau evidence Gateway Under Pressure" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="37-gateway-under-pressure-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="37-gateway-under-pressure-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-03-eksploitasi.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="37-gateway-under-pressure-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
