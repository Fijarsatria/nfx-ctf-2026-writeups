# Progress Bar (Root)

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Boot To Root` |
| Difficulty | `Hard` |
| Poin | `460` |
| Author | `Ariaf` |
| Solves | `3` |
| Tools | nmap, curl, python3, sage |
| Flag | `NFX{fr0m_w4tcht0w3r_c0nf1g_t0_r00t_3xp0rt_j0b}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## Ringkasan

> **Catatan kejujuran bukti.** Sumber utama adalah
> `flags/b2r/ProgressBar.NOTES.md` dan source service yang tersimpan di
> `/tmp/opencode/src22.txt` (hasil enumerasi `/opt/*/app.py` dari target).
> Raw `nmap` dan stdout exploit tidak diarsipkan; langkah `[REKONSTRUKSI]`
> adalah rekonstruksi perintah dari temuan yang terdokumentasi, bukan output
> palsu. Flag dan hash dicek ulang terhadap `flags/b2r/`.
## TL;DR

- Target `10.10.20.22` adalah Apache prefork + mod_php **PHP 8.4.26** dengan
  `session.upload_progress` aktif, `memory_limit=8M`, `display_errors=On`, dan
  satu worker.
- PHP 8.4.26 rentan **CVE-2026-109618 (PHP2Shell)**. Chain 9bie/3em0 memakai
  OOM + dangling session pointer untuk membocorkan Zend MM chunk base dan
  libphp base via `Set-Cookie`, lalu memalsukan `HashTable` dengan
  `pDestructor = zif_system` → RCE sebagai `www-data`.
- Command RCE dibatasi 14 byte, jadi script enumerasi di-upload ke `/out/c`
  lewat `/upload.php` dan dijalankan dengan `sh</out/c`; hasilnya ditulis ke
  `/out/*.txt` yang web-served.
- Enumerasi `/opt` menemukan tiga service loopback: watchtower (config leak
  kredensial UCP), telephony (inbox berisi automation key), dan automation
  (berjalan sebagai **root**, memakai `shell=True`).
- Automation key `PB_AUTO_7b3f9a1c4e0d2f6a` + payload
  `x; id; echo ---CAT---; cat /root/root.txt ... #` memberi eksekusi root.
- Root flag: `NFX{fr0m_w4tcht0w3r_c0nf1g_t0_r00t_3xp0rt_j0b}`.

## Navigasi Halaman

- [Recon](14-progress-bar-root-01-recon.md)
- [Analisis](14-progress-bar-root-02-analisis.md)
- [Eksploitasi / Solver](14-progress-bar-root-03-eksploitasi-solver.md)
- [Flag](14-progress-bar-root-04-flag.md)
- [Bukti / Evidence](14-progress-bar-root-05-bukti-evidence.md)
- [Referensi](14-progress-bar-root-06-referensi.md)
