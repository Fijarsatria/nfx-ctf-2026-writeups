# PageStream

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Web</span><span class="nx-chip">Hard</span><span class="nx-chip">320 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Web` |
| Difficulty | `Hard` |
| Poin (snapshot) | `320` |
| Author | `Ariaf` |
| Solves | `10` |
| Tools | curl, docker |
| Flag | `NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/pagestream/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. **PageStream** adalah aplikasi Express/EJS + MySQL untuk komunitas pembaca. Role `user`/`verified`/`admin` disimpan di session. Terus, **Mass assignment**: `POST /profile` melakukan `Object.assign({}, req.session.user, req.body)`, sehingga user biasa dapat mengubah `role` menjadi `admin` (dan `id`/field lain). Lalu, setelah role menjadi admin, `requireAdmin` lolos. Endpoint `/view?file=` memakai `path.resolve(__dirname, '../uploads', fileParam)` tanpa pengecekan containment → **path traversal file read**, cukup dengan `../../root/flag.txt`. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Deskripsi challenge | — | [Buka](51-pagestream-01-deskripsi-challenge.md) |
| 2 | Recon | curl -sS -i http://s1.nfx.my.id:43659/health | [Buka](51-pagestream-02-recon.md) |
| 3 | Mass assignment role | Setelah role=admin, semua route requireAdmin (/post/new, /view) dapat diakses. | [Buka](51-pagestream-03-mass-assignment-role.md) |
| 4 | Path traversal di `/view` | — | [Buka](51-pagestream-04-path-traversal-di-view.md) |
| 5 | Upload filename traversal | NFX{dummy_flag_for_local_testing} | [Buka](51-pagestream-05-upload-filename-traversal.md) |
| 6 | Analisis | EJS dirender oleh Express: | [Buka](51-pagestream-06-analisis.md) |
| 7 | Eksploitasi / Solver | curl -sS -c cj -X POST -d "username=$USER&password=pw12345" "$BASE/register" | [Buka](51-pagestream-07-eksploitasi-solver.md) |
| 8 | Output asli | NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1} | [Buka](51-pagestream-08-output-asli.md) |
| 9 | Flag | NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1} | [Buka](51-pagestream-09-flag.md) |
| 10 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](51-pagestream-10-bukti-evidence.md) |
| 11 | Referensi | — | [Buka](51-pagestream-11-referensi.md) |

## TL;DR

- **PageStream** adalah aplikasi Express/EJS + MySQL untuk komunitas pembaca. Role `user`/`verified`/`admin` disimpan di session.
- **Mass assignment**: `POST /profile` melakukan `Object.assign({}, req.session.user, req.body)`, sehingga user biasa dapat mengubah `role` menjadi `admin` (dan `id`/field lain).
- Setelah role menjadi admin, `requireAdmin` lolos. Endpoint `/view?file=` memakai `path.resolve(__dirname, '../uploads', fileParam)` tanpa pengecekan containment → **path traversal file read**, cukup dengan `../../root/flag.txt`.
- **Upload path traversal**: multer `diskStorage` memakai `file.originalname` sebagai filename dan `preservePath: true`; nama file `../views/dashboard.ejs` menulis ke `/app/views/dashboard.ejs`. Karena aplikasi berjalan sebagai **root** (supervisord `user=root`), file di `/app` bisa ditimpa meski mode 555.
- EJS yang ditimpa dieksekusi saat `GET /dashboard` → **RCE root**. Kami menjalankan `id` dan `/readflag $(cat /etc/pagestream.key)` dan mendapatkan flag.
- Flag: `NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}`.

<div class="nx-evidence-preview"><a href="51-pagestream-10-bukti-evidence.html"><img src="assets/pagestream/00b-terminal-evidence.png" alt="Pratinjau evidence PageStream" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="51-pagestream-10-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="51-pagestream-01-deskripsi-challenge.html"><b>Deskripsi challenge</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="51-pagestream-02-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="51-pagestream-03-mass-assignment-role.html"><b>Mass assignment role</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="51-pagestream-04-path-traversal-di-view.html"><b>Path traversal di `/view`</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="51-pagestream-05-upload-filename-traversal.html"><b>Upload filename traversal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="51-pagestream-06-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="51-pagestream-07-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="51-pagestream-08-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="51-pagestream-09-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="51-pagestream-10-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="51-pagestream-11-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
