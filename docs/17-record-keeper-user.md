# Record Keeper (User)

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Boot To Root` |
| Difficulty | `Medium` |
| Poin | `460` |
| Author | `Ariaf` |
| Solves | `3` |
| Flag | `NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## Ringkasan

> **Catatan kejujuran bukti.** Sumber utama adalah
> `flags/b2r/NexusRecordTransform.NOTES.md`, halaman console target yang
> tersimpan di `/tmp/opencode/t23.html`, dan artefak eksploit di
> `/tmp/opencode/arkango/` + `/tmp/opencode/rce_pkg/`. Raw `nmap` dan stdout
> penuh exploit tidak diarsipkan; langkah `[REKONSTRUKSI]` adalah rekonstruksi
> perintah dari temuan yang terdokumentasi, bukan output palsu. Flag dan hash
> dicek ulang terhadap `flags/b2r/`.
## TL;DR

- Target `10.10.20.23` mengekspos empat service: console `:8080`,
  framed-TCP Brotli record transform `:3000`, OpenSSH `:22`, dan spool API
  `:9090`.
- Service `:3000` berjalan di **Node.js 24.9.0**, memakai
  `zlib.createBrotliDecompress({chunkSize: 0x330})`,
  `Buffer.allocUnsafeSlow(0x330)`, satu Worker per koneksi, dan
  `UV_THREADPOOL_SIZE=1`.
- Node.js 24.9.0 rentan **CVE-2026-111497 (Node2Shell)**: malformed Brotli
  stream memicu out-of-bounds write di decoder. Fixed di Node.js 24.22.1.
- Exploit `Arkango/CVE-2026-111497` dengan profile
  `node-24.9.0-worker-record-rce-bookworm-x86_64` melakukan heap grooming,
  menimpa return address, pivot ke ROP chain, lalu `execvp("/bin/bash", ...)`.
- Reverse shell balik ke bastion berjalan sebagai `uid=1000(node)`.
  `cat /home/node/user.txt` memberi flag:
  `NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}`.
- Submit pertama ditolak karena typo `w1r1t3` (kelebihan `1`); setelah
  dikoreksi menjadi `wr1t3`, platform menerima `+500 points`.

## Navigasi Halaman

- [Recon](17-record-keeper-user-01-recon.md)
- [Analisis](17-record-keeper-user-02-analisis.md)
- [Eksploitasi / Solver](17-record-keeper-user-03-eksploitasi-solver.md)
- [Flag](17-record-keeper-user-04-flag.md)
- [Bukti / Evidence](17-record-keeper-user-05-bukti-evidence.md)
- [Referensi](17-record-keeper-user-06-referensi.md)
