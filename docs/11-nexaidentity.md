# NexaIdentity

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Medium` |
| Poin | `120` |
| Author | `Ariaf` |
| Solves | `20` |
| Flag | `NFX{n0sql_0p3r4t0r_4uth_byp4ss}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- **NexaIdentity** adalah direktori karyawan NexaCommerce berbasis Express. Halaman login menyediakan akun demo `employee@nexaidentity.test` / `employee1234` (Raka Pratama, employee biasa).
- Endpoint admin `/admin` mengembalikan `403` untuk Raka.
- Login memakai query bergaya Mongo/NoSQL dengan objek dari body form. Karena `express.urlencoded({ extended: true })` memakai `qs`, field `password[$ne]=x` menjadi objek `{ $ne: "x" }`.
- Payload `email[$ne]=x&password[$ne]=x` membuat query mencocokkan user pertama (admin, Nadia Kusuma) → session admin.
- `/admin` lalu menampilkan *Emergency recovery token*: `NFX{n0sql_0p3r4t0r_4uth_byp4ss}`.

## Navigasi Halaman

- [Recon](11-nexaidentity-01-recon.md)
- [Analisis](11-nexaidentity-02-analisis.md)
- [Eksploitasi / Solver](11-nexaidentity-03-eksploitasi-solver.md)
- [Flag](11-nexaidentity-04-flag.md)
- [Bukti / Evidence](11-nexaidentity-05-bukti-evidence.md)
- [Referensi](11-nexaidentity-06-referensi.md)
