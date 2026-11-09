# NexaIdentity — Recon

[← Overview](11-nexaidentity.md) · [Index](index.md)

### 1.1 Deskripsi challenge

> Author: Ariaf
>
> **NexaIdentity** adalah direktori karyawan internal dan portal identitas workspace untuk NexaCommerce. Karyawan dapat masuk, mencari kolega, membuka profil workspace, dan meninjau detail tim.

Tidak ada attachment. Service diberikan lewat platform:

```text
NFX/web/05_nexaidentity   key: NFXCTF-NFCC-NXCTF-2026
```

### 1.2 File / service

Tidak ada source lokal di workspace (`umum/Web/nexaidentity` hanya berisi `BRIEF.md` dan `challenge.json`). Validasi dilakukan black-box pada instance live.

| Item | Nilai |
|---|---|
| Instance | `http://s1.nfx.my.id:41270` (saat validasi) |
| Stack | Express (`X-Powered-By: Express`) |
| Halaman publik | `/`, `/login`, `/directory` (butuh login) |
| Halaman auth | `/dashboard`, `/directory`, `/directory/:id`, `/admin` |
| Akun demo | `employee@nexaidentity.test` / `employee1234` |

Struktur halaman yang teramati:

```text
/                       landing + statistik 12 employees / 11 departments
/login                  form email + password; demo account tertera
/dashboard              ringkasan user
/directory              people search + daftar 12 karyawan
/directory/1            profil Nadia Kusuma (admin@nexaidentity.test)
/directory/2            profil Raka Pratama (employee@nexaidentity.test)
/admin                  403 untuk employee; console admin untuk admin
```

### 1.3 Environment

- `curl`, `python3` + `requests`.
- Instance dijalankan dengan `nxapi.py nx-up "NFX/web/05_nexaidentity" ...`.
- Tidak ada submit flag ke platform.

### 1.4 Triage awal

```bash
BASE=http://s1.nfx.my.id:41270
curl -sS -i "$BASE/"
curl -sS -i "$BASE/login"
curl -sS -i "$BASE/robots.txt"
```

Temuan:
- `/` → `200`, Express, halaman direktori.
- `/login` → `200`, form `POST /login` dengan field `email` dan `password`.
- Halaman login menampilkan **Demo employee account**:
  ```text
  employee@nexaidentity.test / employee1234
  ```
- `/robots.txt` → `404`.
- `/directory` tanpa session → `302 /login`.
- `/admin` tanpa session → `302 /login`.

Login normal:

```bash
curl -sS -i -c cookies.txt \
  -d 'email=employee@nexaidentity.test&password=employee1234' \
  "$BASE/login"
```

```text
HTTP/1.1 302 Found
Location: /dashboard
Set-Cookie: connect.sid=s%3A...; Path=/; HttpOnly; SameSite=Lax
```

Setelah login, `/dashboard` menampilkan `Raka Pratama · Platform Engineering`. `/admin` → `403`:

```text
HTTP/1.1 403 Forbidden
The identity admin console is restricted to People Operations administrators.
```
