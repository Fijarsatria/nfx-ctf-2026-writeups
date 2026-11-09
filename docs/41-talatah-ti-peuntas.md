# Talatah Ti Peuntas

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Pwn</span><span class="nx-chip">Hard</span><span class="nx-chip">440 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Hard` |
| Poin | `440` |
| Author | `Amablex` |
| Solves | `4` |
| Tools | python3, pwntools, checksec, objdump, readelf, strings |
| Flag | `NFX{HiduPPk1T4AAyangMelawann}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/talatah-ti-peuntas/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## TL;DR

- Service "pengelola talatah" mem-parsing pesan protokol **TLT1**: `magic | total_len | key_size | tag | tlv_len | payload`.
- Validasi memeriksa `key_size` (1..0x40) dan `total_len >= tlv_len + 0x14`, tetapi **tidak pernah membandingkan `tlv_len` dengan `key_size`**.
- Parser melakukan `data = malloc(key_size)` lalu `memcpy(data, msg+0x14, tlv_len)` → **heap overflow** dari chunk data ke chunk node yang berdekatan.
- Node struct 0x20 byte berisi `name[16]`, `len`, `flags`, dan `char *data`. Overflow mengontrol `node->len` dan `node->data`.
- `op_view` menjadi **arbitrary read** (`fwrite(node->data, node->len)`); `op_edit` menjadi **arbitrary write** (`memcpy(node->data, input, new_len)`).
- Exploit: leak `printf@got`, hitung libc, tulis `system` ke `free@got`, taruh `/bin/sh` di `.bss`, lalu `delete` node → `free("/bin/sh")` = `system("/bin/sh")`.
- Flag: `NFX{HiduPPk1T4AAyangMelawann}`.

<div class="nx-evidence-preview"><a href="41-talatah-ti-peuntas-09-bukti-evidence.html"><img src="assets/talatah-ti-peuntas/00b-submit-platform.png" alt="Pratinjau evidence Talatah Ti Peuntas" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="41-talatah-ti-peuntas-09-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="41-talatah-ti-peuntas-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-03-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-04-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-05-alamat-penting.html"><b>Alamat penting</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-06-eksploitasi.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-07-eksploitasi-2.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-08-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-09-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="41-talatah-ti-peuntas-10-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
