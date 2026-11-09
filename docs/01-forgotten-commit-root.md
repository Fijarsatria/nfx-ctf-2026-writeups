# Forgotten Commit (Root)

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Boot To Root</span><span class="nx-chip">Medium</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Boot To Root` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `Ariaf` |
| Solves | `21` |
| Tools | nmap, curl, git |
| Flag | `NFX{fzf_l1st3n_r00t_sh3ll_pwn3d}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/forgotten-commit-root/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Ringkasan

> **Catatan bukti.** Writeup ini memakai hasil **live rerun 2026-11-09** di
> instance platform. Transkrip asli ada di `assets/forgotten-commit-root/`
> (`01-live-*` sampai `04-live-*`), screenshot challenge dan submit ada di
> `00-challenge-platform.png` dan `00b-submit-platform.png`. Flag dicek ulang
> ke platform dan diterima (`Correct, but already solved.`).
## TL;DR

- Target `10.10.20.21` menjalankan nginx (port 80) dan OpenSSH 8.9p1 (port 22).
- Webroot mengekspos `/.git/`; `git-dumper` memulihkan 5 commit.
- Commit `5c65d99` ("Remove Ansible inventory") menghapus
  `ansible/inventory.ini`, tetapi commit induknya (`8acfc1f`) masih menyimpan
  kredensial Ansible plaintext: `leonardo:Dev0pment#2026!`.
- Kredensial itu valid untuk SSH. `cat /home/leonardo/user.txt` memberi user
  flag `NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh}`.
- `sudo -n -l` mengizinkan `(root) NOPASSWD: /usr/local/bin/fzf --listen 1337`.
  fzf dijalankan sebagai root, lalu HTTP remote-control API-nya dipakai untuk
  `execute(cp /root/root.txt /tmp/rootflag; chmod 644 /tmp/rootflag)`.
- Root flag: `NFX{fzf_l1st3n_r00t_sh3ll_pwn3d}`.

<div class="nx-evidence-preview"><a href="01-forgotten-commit-root-07-bukti-evidence.html"><img src="assets/forgotten-commit-root/00b-submit-platform.png" alt="Pratinjau evidence Forgotten Commit (Root)" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="01-forgotten-commit-root-07-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="01-forgotten-commit-root-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-03-enumerasi-sudo.html"><b>Enumerasi sudo</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-04-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-05-kenapa-fzf-bisa-menjadi-privesc.html"><b>Kenapa fzf bisa menjadi privesc</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-06-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-07-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-08-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
