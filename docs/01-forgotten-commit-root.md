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

## Ringkasan

> **Catatan bukti.** Sumber utama writeup ini adalah
> `flags/b2r/ForgottenCommit_SOLVED.md` dan `ForgottenCommit_UNSOLVED.md`.
> Raw transcript `nmap`/SSH tidak diarsipkan. Perintah yang ditandai
> `[REKONSTRUKSI]` disusun dari temuan yang terdokumentasi dan metadata
> service, jadi bukan salinan transkrip mentah. Flag dan hash dicek ulang
> terhadap file di `flags/b2r/`.
## TL;DR

- Target `10.10.20.21` menjalankan nginx (port 80) dan OpenSSH 8.9p1 (port 22).
- Webroot mengekspos `/.git/`; `git-dumper` memulihkan 5 commit.
- Commit `3f4c118` ("Remove Ansible inventory") menghapus
  `ansible/inventory.ini`, tetapi commit induknya (`bff2915`) masih menyimpan
  kredensial Ansible plaintext: `leonardo:Dev0pment#2026!`.
- Kredensial itu valid untuk SSH. `cat /home/leonardo/user.txt` memberi user
  flag `NFX{g1t_h1story_s3cr3ts_l34d_t0_ssh}`.
- `sudo -n -l` mengizinkan `(root) NOPASSWD: /usr/local/bin/fzf --listen 1337`.
  fzf dijalankan sebagai root, lalu HTTP remote-control API-nya dipakai untuk
  `execute(cp /root/root.txt /tmp/rootflag; chmod 644 /tmp/rootflag)`.
- Root flag: `NFX{fzf_l1st3n_r00t_sh3ll_pwn3d}`.

<div class="nx-evidence-preview"><a href="01-forgotten-commit-root-05-bukti-evidence.html"><img src="assets/forgotten-commit-root/98-terminal-evidence.png" alt="Pratinjau evidence Forgotten Commit (Root)" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="01-forgotten-commit-root-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="01-forgotten-commit-root-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="01-forgotten-commit-root-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
