# Progress Bar (User) — Analisis

[← Overview](15-progress-bar-user.md) · [Index](index.md)

### 2.1 Permukaan upload dan `session.upload_progress`

PHP memiliki fitur `session.upload_progress`: ketika sebuah multipart POST
mengandung field `PHP_SESSION_UPLOAD_PROGRESS`, PHP memproses progres upload
dan session **sebelum** kode aplikasi (`RINIT`) dijalankan. Artinya, walaupun
`upload.php` sendiri tidak memanggil `session_start()`, jalur session tetap
aktif.

Pada PHP 8.4.26, kombinasi fitur ini dengan OOM bailout menimbulkan
use-after-free/dangling pointer: `PS(http_session_vars)` dan `PS(id)` tidak
dibersihkan dengan benar setelah request gagal karena kehabisan memori.
Request berikutnya yang ditangani worker yang sama memakai pointer lama itu.

Kondisi target sangat mendukung:

- `memory_limit=8M` → OOM mudah dipicu.
- `display_errors=On` → error path dan `headers_sent` dapat dikendalikan.
- Satu worker prefork → state antar-request deterministik.
- `post_max_size=64M` → cukup besar untuk field 12 MB yang memicu OOM.

### 2.2 CVE-2026-109618 / PHP2Shell

CVE-2026-109618 adalah RCE via OOM corruption di PHP; fixed di 8.4.27
(8.5.12 / 8.3.36 / 8.2.35 untuk branch lain). Chain publik 9bie/3em0
menjalankan empat tahap:

| Tahap | Aksi | Hasil |
|---|---|---|
| 0 | Worker rotation: field live 3 MB + field OOM 12 MB, lalu request session | Worker baru mewarisi mapping yang bersih |
| 1 | 1001 field memicu `max_input_vars`; field 12 MB OOM di `php_session_initialize()` | `PS(http_session_vars)` dangling |
| 2 | `php_url_encode()` over-read chunk pointer ke `Set-Cookie` | Zend MM chunk base |
| 3 | HashTable 56-byte membuat `ZSTR_LEN(PS(id))` membaca `nTableSize` | libphp base |
| 4 | Fake `reference` + fake `HashTable` dengan `pDestructor = zif_system` | RCE |

Destructor chain yang dieksploitasi:

```text
php_session_track_init()
  zval_ptr_dtor(PS(http_session_vars))
    zend_reference_destroy(R0)
      zval_ptr_dtor(&ref->val)          # IS_ARRAY_EX
        zend_array_destroy(fake HT)
          zend_hash_destroy(fake HT)
            pDestructor(&bucket->val)   # zif_system
```

Karena `zif_system` ada di `libphp.so`, offset yang dipakai adalah offset simbol
relatif terhadap base libphp, bukan alamat absolut. Ini membuat ASLR tidak
menghalangi setelah base bocor.

### 2.3 Batas 14 byte dan `/out`

Command yang dieksekusi disimpan di `zend_string` berukuran tetap; batas
praktisnya **14 byte**. Karena itu notes memakai trik:

1. Upload script enumerasi panjang ke `/out/c` lewat form upload biasa.
2. Jalankan `sh</out/c` (8 byte) sebagai command RCE.
3. Script menulis hasil ke `/out/*.txt`; file itu dibaca lewat HTTP.

Ini juga menunjukkan masalah desain: direktori upload `/out` bukan hanya
tempat file user, tetapi **web-served** dan writable oleh proses web.

### 2.4 Enumerasi pasca-foothold

Dari shell `www-data`, source service di `/opt` dibaca. Tiga service loopback
menjadi rantai eskalasi:

1. **Watchtower** (`/opt/watchtower/app.py`, port 3000) menyajikan
   `/api/config` yang membaca `/home/svc-watch/config.json`. Config ini berisi
   kredensial UCP:

   ```json
   {
     "telephony_user": "ucp-template",
     "telephony_pass": "Pr0gr3ssB4r_2026"
   }
   ```

2. **Telephony UCP** (`/opt/telephony/app.py`, port 8080) memakai kredensial
   itu untuk login. Setelah login, user bisa menambahkan widget `voicemail`
   lewat `POST /ucp/widgets`. Halaman `/ucp/inbox` lalu menampilkan automation
   key:

   ```text
   PB_AUTO_7b3f9a1c4e0d2f6a
   ```

3. **Automation** (`/opt/automation/app.py`, port 9000) berjalan sebagai root
   dan menerima `POST /jobs/export` dengan bearer automation key. Field
   `report` dimasukkan ke command shell:

   ```python
   command = f"tar czf {EXPORT_DIR}/{report}.tgz {DATA_DIR} 2>&1"
   subprocess.run(command, shell=True, capture_output=True, text=True, timeout=20)
   ```

   Tidak ada escaping, validasi karakter, atau pemisahan argumen. Payload
   `x; <command> #` langsung dieksekusi sebagai root.

### 2.5 Mengapa `user.txt` tidak bisa dibaca langsung

`/home/deploy` memiliki mode `0711` dan dimiliki `deploy:deploy`.
`/home/deploy/user.txt` adalah mode `400`, owner `deploy`. `www-data` bukan
owner dan bukan group, sehingga tidak punya izin baca. Ini sebabnya langkah
akhir challenge User memanfaatkan automation root untuk membaca file tersebut.
Dengan kata lain, "User" dan "Root" di lab ini berbagi satu rantai: foothold
`www-data` lalu eskalasi ke root, dan user flag dibaca setelah berada di
konteks root.
