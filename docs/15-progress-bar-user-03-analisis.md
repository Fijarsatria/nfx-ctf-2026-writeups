# Progress Bar (User) — Analisis

[← Overview](15-progress-bar-user.md) · [Index](index.md)

> **Langkah 3/10 — Analisis.** CVE-2026-109618 adalah RCE via OOM corruption di PHP; fixed di 8.4.27 (8.5.12 / 8.3.36 / 8.2.35 untuk branch lain).
>
> **Titik penting:** CVE-2026-109618 adalah RCE via OOM corruption di PHP; fixed di 8.4.27 (8.5.12 / 8.3.36 / 8.2.35 untuk branch lain).
>
> **Berikutnya:** [Analisis](15-progress-bar-user-04-analisis-2.md)

## 2.2 CVE-2026-109618 / PHP2Shell

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

## 2.3 Batas 14 byte dan `/out`

Command yang dieksekusi disimpan di `zend_string` berukuran tetap; batas
praktisnya **14 byte**. Karena itu notes memakai trik:

1. Upload script enumerasi panjang ke `/out/c` lewat form upload biasa.
2. Jalankan `sh</out/c` (8 byte) sebagai command RCE.
3. Script menulis hasil ke `/out/*.txt`; file itu dibaca lewat HTTP.

Ini juga menunjukkan masalah desain: direktori upload `/out` bukan hanya
tempat file user, tetapi **web-served** dan writable oleh proses web.

### Evidence langkah ini

![term-02-php2shell.png](assets/progress-bar-user/term-02-php2shell.png)

*Terminal evidence — `02-php2shell.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`02-php2shell.txt`](assets/progress-bar-user/02-php2shell.txt)
