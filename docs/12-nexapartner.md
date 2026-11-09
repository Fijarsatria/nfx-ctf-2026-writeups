# NexaPartner

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `200` |
| Author | `Ariaf` |
| Solves | `16` |
| Flag | `NFX{js0n_pr0t0_p0llut10n_4dm1n_byp4ss}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- **NexaPartner** adalah portal partner/reseller NexaCommerce berbasis Express. Halaman login menyediakan akun demo `partner@nexapartner.test` / `partner1234` (Arunika Retail Group).
- `/admin` mengembalikan `403` untuk partner biasa.
- Halaman `/settings` mengirim JSON ke `POST /api/settings`; server menggabungkan objek tersebut ke settings tanpa memblokir key prototipe.
- Payload `{"__proto__":{"role":"admin","isAdmin":true,"admin":true,"tier":"platinum"}}` mencemari `Object.prototype` (atau objek otorisasi turunannya).
- Setelah itu `/admin` berubah dari `403` menjadi `302 /admin/audit`; halaman audit menampilkan recovery token: `NFX{js0n_pr0t0_p0llut10n_4dm1n_byp4ss}`.

## Navigasi Halaman

- [Recon](12-nexapartner-01-recon.md)
- [Analisis](12-nexapartner-02-analisis.md)
- [Eksploitasi / Solver](12-nexapartner-03-eksploitasi-solver.md)
- [Flag](12-nexapartner-04-flag.md)
- [Bukti / Evidence](12-nexapartner-05-bukti-evidence.md)
- [Referensi](12-nexapartner-06-referensi.md)
