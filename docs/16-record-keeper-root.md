# Record Keeper (Root)

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Boot To Root</span><span class="nx-chip">Medium</span><span class="nx-chip">460 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Boot To Root` |
| Difficulty | `Medium` |
| Poin | `460` |
| Author | `Ariaf` |
| Solves | `3` |
| Tools | nmap, curl, python3, sage |
| Flag | `NFX{sp00l3r_4rch1v3_r00t_pwn3d}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

> **Catatan bukti.** Sumber utama adalah
> `flags/b2r/NexusRecordTransform.NOTES.md` dan halaman console target
> `/tmp/opencode/t23.html`. Script eksploitasi tar di §3.2 ditandai
> `[REKONSTRUKSI]`: notes mencatat aksi dan command intinya, tetapi isi script
> lengkap tidak tersimpan. Output yang dikutip (root flag, hash, submit log)
> berasal dari notes dan file flag lokal.
## TL;DR

- Foothold dimulai dari RCE **CVE-2026-111497 (Node2Shell)** di service
  `:3000`, memberi shell sebagai `uid=1000(node)`.
- `sudo -n -l` mengizinkan `(ops) NOPASSWD: /usr/local/bin/record-archive`.
- `record-archive` menjalankan `cd "$target"; tar -czf "$out" *` sebagai
  `ops`. Karena `tar` membaca nama file yang diawali `--` sebagai opsi, isi
  direktori target bisa menyuntikkan opsi `tar`.
- Payload `--checkpoint=1` + `--checkpoint-action=exec=sh x` membuat GNU tar
  mengeksekusi `sh x` sebagai `ops`.
- Script `x` (sebagai `ops`) membaca `/etc/nexus/ops.creds` +
  `/etc/nexus/spool.token`, lalu menulis job
  `id=rootarc / action=archive / target=/root` ke `/srv/record-spool/`.
- Root-owned spooler memproses job setiap 2 detik dan mengarsipkan `/root`
  ke `/var/backups/records/rootarc.tar.gz`. Arsip disalin keluar dan
  diekstrak:

  ```bash
  tar -xOzf /tmp/opsexfil/rootarc.tar.gz ./root.txt
  # NFX{sp00l3r_4rch1v3_r00t_pwn3d}
  ```

<div class="nx-evidence-preview"><a href="16-record-keeper-root-05-bukti-evidence.html"><img src="assets/record-keeper-root/98-terminal-evidence.png" alt="Pratinjau evidence Record Keeper (Root)" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="16-record-keeper-root-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="16-record-keeper-root-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="16-record-keeper-root-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="16-record-keeper-root-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="16-record-keeper-root-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="16-record-keeper-root-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="16-record-keeper-root-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
