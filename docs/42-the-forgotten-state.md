# THE FORGOTTEN STATE

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Pwn</span><span class="nx-chip">Hard</span><span class="nx-chip">340 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Pwn` |
| Difficulty | `Hard` |
| Poin (snapshot) | `340` |
| Author | `Amablex` |
| Solves | `9` |
| Tools | python3, pwntools, checksec, objdump, readelf, strings |
| Flag | `NFX{ElC0nloe_Forg0tten_StaticcD42#}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/the-forgotten-state/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. service mengelola 16 record (`create`, `release`, `view`, `edit`, `list`). Terus, `op_release()` melakukan `free(record->data)` lalu `free(record)`, mengosongkan `active[idx]`, tetapi **tidak mengosongkan `table[idx]`** → dangling pointer. `op_view`/`op_edit`/`op_list` **tidak memeriksa `active[]`**, jadi pointer basi masih bisa dipakai (use-after-free). Lalu, `op_edit()` memvalidasi `new_len` hanya pada rentang `1..0x400`, bukan terhadap ukuran alokasi asli → **heap overflow** ke record berikutnya. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Kata kunci: "pengelolaan objek dan state internal" dan judul "THE FORGOTTEN STATE" → state active[]/table[] yang tidak konsisten. | [Buka](42-the-forgotten-state-01-recon.md) |
| 2 | Triage awal | file state | [Buka](42-the-forgotten-state-02-triage-awal.md) |
| 3 | Analisis | Record (malloc 0x20 → chunk 0x30): | [Buka](42-the-forgotten-state-03-analisis.md) |
| 4 | Analisis | Jika field rec->len dan rec->data bisa dikendalikan, view menjadi arbitrary read (dibatasi 0x400 byte). | [Buka](42-the-forgotten-state-04-analisis-2.md) |
| 5 | Analisis | edit(rec0, 0x50) menulis dari user data B0: | [Buka](42-the-forgotten-state-05-analisis-3.md) |
| 6 | Eksploitasi | python3 exploit.py \| tee 03-exploit-run.txt | [Buka](42-the-forgotten-state-06-eksploitasi.md) |
| 7 | Catatan jalur UAF | Selain overflow di atas, binary ini juga meninggalkan dangling pointer (table[idx] tidak di-null-kan) dan view/edit tidak memeriksa active[idx]. | [Buka](42-the-forgotten-state-07-catatan-jalur-uaf.md) |
| 8 | Flag | NFX{ElC0nloe_Forg0tten_StaticcD42#} | [Buka](42-the-forgotten-state-08-flag.md) |
| 9 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](42-the-forgotten-state-09-bukti-evidence.md) |
| 10 | Referensi | — | [Buka](42-the-forgotten-state-10-referensi.md) |

## TL;DR

- Service mengelola 16 record (`create`, `release`, `view`, `edit`, `list`).
- `op_release()` melakukan `free(record->data)` lalu `free(record)`, mengosongkan `active[idx]`, tetapi **tidak mengosongkan `table[idx]`** → dangling pointer. `op_view`/`op_edit`/`op_list` **tidak memeriksa `active[]`**, jadi pointer basi masih bisa dipakai (use-after-free).
- `op_edit()` memvalidasi `new_len` hanya pada rentang `1..0x400`, bukan terhadap ukuran alokasi asli → **heap overflow** ke record berikutnya.
- Exploit yang diverifikasi memakai overflow: record pertama (data 0x20 byte) diedit 0x50 byte, menimpa header record kedua: `name`, `len=8`, `flags=1`, dan `data = free@got`.
- `view` → leak `free@got`; `edit` → tulis `system` ke `free@got`; `release` pada record berisi `"/bin/sh"` → `free("/bin/sh")` = `system("/bin/sh")`.
- Flag: `NFX{ElC0nloe_Forg0tten_StaticcD42#}`.

<div class="nx-evidence-preview"><a href="42-the-forgotten-state-09-bukti-evidence.html"><img src="assets/the-forgotten-state/00b-terminal-evidence.png" alt="Pratinjau evidence THE FORGOTTEN STATE" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="42-the-forgotten-state-09-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="42-the-forgotten-state-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-03-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-04-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-05-analisis-3.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-06-eksploitasi.html"><b>Eksploitasi</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-07-catatan-jalur-uaf.html"><b>Catatan jalur UAF</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-08-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-09-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="42-the-forgotten-state-10-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
