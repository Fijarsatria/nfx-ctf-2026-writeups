# NexaPartner

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Web</span><span class="nx-chip">Medium</span><span class="nx-chip">200 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `200` |
| Author | `Ariaf` |
| Solves | `16` |
| Tools | curl, python3 |
| Flag | `NFX{js0n_pr0t0_p0llut10n_4dm1n_byp4ss}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- **NexaPartner** adalah portal partner/reseller NexaCommerce berbasis Express. Halaman login menyediakan akun demo `partner@nexapartner.test` / `partner1234` (Arunika Retail Group).
- `/admin` mengembalikan `403` untuk partner biasa.
- Halaman `/settings` mengirim JSON ke `POST /api/settings`; server menggabungkan objek tersebut ke settings tanpa memblokir key prototipe.
- Payload `{"__proto__":{"role":"admin","isAdmin":true,"admin":true,"tier":"platinum"}}` mencemari `Object.prototype` (atau objek otorisasi turunannya).
- Setelah itu `/admin` berubah dari `403` menjadi `302 /admin/audit`; halaman audit menampilkan recovery token: `NFX{js0n_pr0t0_p0llut10n_4dm1n_byp4ss}`.

<div class="nx-evidence-preview"><a href="12-nexapartner-05-bukti-evidence.html"><img src="assets/nexapartner/98-terminal-evidence.png" alt="Pratinjau evidence NexaPartner" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="12-nexapartner-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="12-nexapartner-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="12-nexapartner-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="12-nexapartner-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="12-nexapartner-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="12-nexapartner-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="12-nexapartner-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
