# Progress Bar (Root) — Analisis

[← Overview](14-progress-bar-root.md) · [Index](index.md)

### 2.1 Foothold: PHP2Shell CVE-2026-109618

`session.upload_progress` membuat PHP memproses multipart session sebelum kode
aplikasi. Pada PHP 8.4.26, OOM saat inisialisasi session meninggalkan pointer
`PS(http_session_vars)` / `PS(id)` yang dangling. Request berikutnya di worker
yang sama memakai pointer itu.

Chain exploit:

1. **Worker rotation** — field live 3 MB + field OOM 12 MB, lalu request
   session; worker baru mewarisi address space yang bersih.
2. **Heap leak** — 1001 field memicu `max_input_vars`; field 12 MB OOM di
   `php_session_initialize()`; `php_url_encode()` over-read chunk pointer ke
   `Set-Cookie` → Zend MM chunk base.
3. **libphp leak** — HashTable 56 byte membuat `ZSTR_LEN(PS(id))` membaca
   `nTableSize`, mengekspos `pDestructor = ZVAL_PTR_DTOR` → libphp base.
4. **RCE** — fake `reference` + fake `HashTable` dengan
   `pDestructor = zif_system`; cleanup memanggil `zif_system(command)`.

Offset official PHP 8.4.26 trixie amd64:

```text
zif_system       0x465370
ZVAL_PTR_DTOR    0x65eb60
htdata           0x690d8
```

Karena command di `zend_string` dibatasi 14 byte, script payload di-upload ke
`/out/c` dan dijalankan dengan `sh</out/c`.

### 2.2 Enumerasi sumber service

Dari `www-data`, file `/opt/*/app.py` dibaca. Tiga service menjadi rantai:

#### Watchtower `127.0.0.1:3000`

`/opt/watchtower/app.py` membaca `/home/svc-watch/config.json` dan menyajikan
`/api/config`. Config berisi kredensial UCP:

```json
{
  "telephony_user": "ucp-template",
  "telephony_pass": "Pr0gr3ssB4r_2026"
}
```

#### Telephony UCP `127.0.0.1:8080`

`/opt/telephony/app.py` login memakai kredensial di atas. Setelah login, user
bisa menambahkan widget `voicemail` lewat `POST /ucp/widgets`. Halaman
`/ucp/inbox` menampilkan automation key:

```text
PB_AUTO_7b3f9a1c4e0d2f6a
```

#### Automation `127.0.0.1:9000` (root)

`/opt/automation/app.py` dijalankan sebagai root oleh entrypoint:

```bash
python3 -u /opt/automation/app.py &
start_as svc-watch python3 -u /opt/watchtower/app.py
start_as svc-telephony python3 -u /opt/telephony/app.py
```

Handler `POST /jobs/export` memvalidasi bearer key, lalu menyusun command:

```python
command = f"tar czf {EXPORT_DIR}/{report}.tgz {DATA_DIR} 2>&1"
subprocess.run(command, shell=True, capture_output=True, text=True, timeout=20)
```

`report` berasal dari JSON body dan masuk langsung ke shell. Ini command
injection klasik. Karena proses berjalan sebagai root, hasilnya root shell.

### 2.3 Rantai eskalasi

```text
www-data
  -> baca /home/svc-watch/config.json via /api/config
  -> login UCP, tambah widget voicemail, baca automation key
  -> POST /jobs/export dengan report berisi "; command #"
  -> root
```

Tidak ada exploit memory corruption di tahap privesc; semuanya adalah
kebocoran kredensial + command injection.
