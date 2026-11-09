# Perimeter Breach

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Medium</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `Ariaf` |
| Tools | gobuster, sqlmap, python3, tshark, git |
| Flag | `NFX{P4th_1nt0_Pr0duct10n}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Tiga log (`access.log` Nginx, `auth.log` syslog, `webapp.log`) merekam satu kampanye serangan dari **185.220.101.47** pada 10 Oktober 2026.
- Rekon: `gobuster/3.6` (13:02), SQL injection `sqlmap/1.7.2` pada `products.php?id=` (13:15), dump tabel `users`.
- Initial access: login admin berhasil pada **13:42:02** dengan password `Aroma#Craft2026`.
- Webshell: upload `cache_thumb.php` (412 byte, MIME `image/jpeg`) ke `/uploads/`, dieksekusi lewat `?c=` untuk `whoami`, `id`, `cat /etc/passwd`, `cat /home/deploy/.env`.
- Lateral movement: SSH password sebagai `deploy` dari IP penyerang (14:20:03).
- Persistence: `deploy` membuat user **`svc_backup`** (UID 1002, group sudo), mengganti password, lalu login SSH publickey sebagai `svc_backup` (14:41:27).
- Flag: `NFX{P4th_1nt0_Pr0duct10n}`.

<div class="nx-evidence-preview"><a href="07-perimeter-breach-05-bukti-evidence.html"><img src="assets/perimeter-breach/98-terminal-evidence.png" alt="Pratinjau evidence Perimeter Breach" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="07-perimeter-breach-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="07-perimeter-breach-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="07-perimeter-breach-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="07-perimeter-breach-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="07-perimeter-breach-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="07-perimeter-breach-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="07-perimeter-breach-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
