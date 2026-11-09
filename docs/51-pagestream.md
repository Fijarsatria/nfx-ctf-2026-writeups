# PageStream

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Web</span><span class="nx-chip">Hard</span><span class="nx-chip">320 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Web` |
| Difficulty | `Hard` |
| Poin | `320` |
| Author | `Ariaf` |
| Solves | `10` |
| Tools | curl, docker |
| Flag | `NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- **PageStream** adalah aplikasi Express/EJS + MySQL untuk komunitas pembaca. Role `user`/`verified`/`admin` disimpan di session.
- **Mass assignment**: `POST /profile` melakukan `Object.assign({}, req.session.user, req.body)`, sehingga user biasa dapat mengubah `role` menjadi `admin` (dan `id`/field lain).
- Setelah role menjadi admin, `requireAdmin` lolos. Endpoint `/view?file=` memakai `path.resolve(__dirname, '../uploads', fileParam)` tanpa pengecekan containment → **path traversal file read**, cukup dengan `../../root/flag.txt`.
- **Upload path traversal**: multer `diskStorage` memakai `file.originalname` sebagai filename dan `preservePath: true`; nama file `../views/dashboard.ejs` menulis ke `/app/views/dashboard.ejs`. Karena aplikasi berjalan sebagai **root** (supervisord `user=root`), file di `/app` bisa ditimpa meski mode 555.
- EJS yang ditimpa dieksekusi saat `GET /dashboard` → **RCE root**. Kami menjalankan `id` dan `/readflag $(cat /etc/pagestream.key)` dan mendapatkan flag.
- Flag: `NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}`.

<div class="nx-evidence-preview"><a href="51-pagestream-05-bukti-evidence.html"><img src="assets/pagestream/98-terminal-evidence.png" alt="Pratinjau evidence PageStream" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="51-pagestream-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="51-pagestream-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="51-pagestream-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="51-pagestream-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="51-pagestream-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="51-pagestream-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="51-pagestream-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
