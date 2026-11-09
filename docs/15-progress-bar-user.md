# Progress Bar (User)

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Boot To Root</span><span class="nx-chip">Hard</span><span class="nx-chip">460 poin</span><span class="nx-badge nx-badge-candidate">CANDIDATE</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Boot To Root` |
| Difficulty | `Hard` |
| Poin | `460` |
| Author | `Ariaf` |
| Solves | `3` |
| Tools | nmap, curl, python3, sage |
| Flag | `NFX{pr0gr3ss_b4r_qu3u3_st4g1ng_pwn3d_4s_www_d4t4}` *(candidate)* |
| Status | `CANDIDATE` |

[← Kembali ke Index](index.md)

## Ringkasan

> **Catatan bukti.** Sumber utama adalah
> `flags/b2r/ProgressBar.NOTES.md`, source service yang tersimpan di
> `/tmp/opencode/src22.txt`, dan submit log read-only di `work/`. Raw output
> `nmap` dan stdout exploit tidak diarsipkan; langkah yang ditandai
> `[REKONSTRUKSI]` disusun dari temuan yang terdokumentasi, jadi bukan
> salinan transkrip mentah.
## TL;DR

- Target `10.10.20.22` menjalankan Apache prefork + **mod_php PHP 8.4.26**
  dengan `display_errors=On`, `memory_limit=8M`, `post_max_size=64M`, dan
  `session.upload_progress.enabled=On`. Versi ini rentan **CVE-2026-109618**
  (PHP2Shell), fixed di 8.4.27.
- Aplikasi mengekspos `/upload.php` (multipart upload) dan direktori `/out/`
  yang web-served serta writable oleh `www-data`.
- Chain PHP2Shell (9bie/3em0) memakai `PHP_SESSION_UPLOAD_PROGRESS` untuk
  memicu OOM, meninggalkan pointer session dangling, membocorkan Zend MM chunk
  base + libphp base lewat `Set-Cookie`, lalu memalsukan `HashTable` dengan
  `pDestructor = zif_system` → RCE sebagai `www-data`.
- Karena command dibatasi 14 byte, payload panjang di-upload sebagai script
  `/out/c` lewat form upload, lalu dijalankan dengan `sh</out/c`.
- `www-data` tidak bisa membaca `/home/deploy/user.txt` (mode 400,
  `deploy:deploy`, home 0711). Dari shell itu, enumerasi loopback menemukan
  kredensial UCP di watchtower, automation key di inbox voicemail, dan
  command injection `shell=True` di automation yang berjalan sebagai root.
- User flag dibaca sebagai root:
  `NFX{pr0gr3ss_b4r_qu3u3_st4g1ng_pwn3d_4s_www_d4t4}`.
- Nilai tersebut **byte-identik** dengan `user.txt` di target, tetapi platform
  menolaknya. Instance sudah di-redeploy dan dibaca ulang; hasilnya sama.

<div class="nx-evidence-preview"><a href="15-progress-bar-user-05-bukti-evidence.html"><img src="assets/progress-bar-user/98-terminal-evidence.png" alt="Pratinjau evidence Progress Bar (User)" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="15-progress-bar-user-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="15-progress-bar-user-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="15-progress-bar-user-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="15-progress-bar-user-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="15-progress-bar-user-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="15-progress-bar-user-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="15-progress-bar-user-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
