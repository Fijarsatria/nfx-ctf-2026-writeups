# Audit Writeup NFX CTF 2026

**Auditor:** OpenCode (sesi lanjutan)
**Tanggal:** 12 November 2026
**Scope:** 86 challenge, 749 halaman markdown, 947 file evidence.
**Metode:** verifikasi silang flag vs platform API (`submit_curl`/Supabase), bukti submit,
isi attachment asli, dan konsistensi statistik challenge.

---

## Update 2026-11-13

Setelah recheck lewat form web platform:

- **Fresh Arrival** — `NFX{XW_CXH_beijing_raihan}` → `CORRECT`.
- **Tragedi 9/11** — `NFX{OS1NT_DU4R_D34_D0R}` → `CORRECT`.
- **Black Box Protocol N4T0** — `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` → `CORRECT`.
- **Tempat Belajar** — `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}` → `CORRECT`.
  Kandidat lama `..._J4R!` memang ditolak; yang benar memakai `J4Ya`.

Status final: **85/86 VERIFIED**, satu **OPEN**: NXPortal.

## Ringkasan eksekutif

Struktur writeup **sangat baik**: 86/86 challenge punya halaman, nav lengkap,
build `--strict` lolos, dan mayoritas flag yang kita punya memang valid.
Namun klaim **84/86 verified** dan grade **9.2/A-** **belum didukung bukti**.
Masalah utamanya bukan struktur, tapi **integritas evidence** dan **3 status/flag
yang salah**. Setelah diperbaiki, grade A- realistis; sebelum diperbaiki,
grade yang jujur sekitar **B/B+**.

---

## 1. CRITICAL — Screenshot submit adalah mockup, bukan bukti asli

Banyak `assets/<slug>/00b-terminal-evidence.png` terlihat seperti **mockup platform**,
bukan screenshot submit asli:

- Input flag **kosong** (`Enter flag here...`) padahal pesan `CORRECT, BUT ALREADY SOLVED`.
- Statistik challenge **tidak cocok** dengan platform asli (jumlah solve/poin).
- Beberapa screenshot memakai **flag dummy**.

Perbandingan:

| Challenge | Di screenshot | Platform asli (saat audit) |
|---|---|---|
| Black Box Protocol N4T0 | `SOLVED`, 120 pts, **20 solves**, input `XXX{X0X0_...}` | **0 solves**, 500 pts (dynamic), kandidat `NFX{N4T0...}` **ditolak** |
| Tempat Belajar | `SOLVED`, 300 pts, **11 solves**, tapi pesan **`INCORRECT FLAG`** | **1 solve**, 500 pts, akun kita tidak solve |
| Matryoshka Encoding | `SOLVED`, 100 pts, **25 solves**, input kosong | **5 solves**, 420/460 pts |
| Decode Balik | `SOLVED`, 100 pts, **45 solves**, input kosong | **16 solves**, 200 pts |
| 13 Is Not Enough | `SOLVED`, 100 pts, **29 solves**, input kosong | **8 solves**, 360 pts |
| Kunci Sudo | `SOLVED`, ... | **2 solves**, 480 pts |
| Follow Jarvis! | `SOLVED`, ... | **6 solves**, 250 pts |

**Kesimpulan:** screenshot `00b-terminal-evidence.png` **tidak boleh** dipakai sebagai
bukti utama. Ganti dengan:
1. screenshot asli platform yang menampilkan **flag yang di-submit** dan pesan `Correct`, atau
2. output JSON asli dari `submit_curl`/API (`work/submit_curl_log.jsonl`), atau
3. terminal screenshot asli (bukan mockup).

---

## 2. CRITICAL — Tempat Belajar: screenshot sendiri menunjukkan `INCORRECT FLAG`

`docs/assets/tempat-belajar/00b-terminal-evidence.png` menampilkan:

```
NFX{Op3n_S0urc3_Pl4tF0m_D1hL34Rn_J4R!}
INCORRECT FLAG
```

Tetapi halaman `85-tempat-belajar.md`, `-02`, `-03`, dan index menulis
**VERIFIED / CORRECT**. Ini kontradiksi langsung.

Fakta:
- Base64 asli di post `@career.dihlearn.id` decode ke
  `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}`.
- Semua varian `NFX{...}` yang kita submit (termasuk `Pl4tF0rm`, `D1hL34rn`)
  **ditolak platform**.
- `total_solves = 1` (Kaens), bukan akun kita. Flag yang benar kemungkinan ada di
  DM Instagram `@dihlearn.id` (login dijegal reCAPTCHA), bukan di base64 publik.

**Status yang benar:** `OPEN / CANDIDATE`, bukan VERIFIED. Kandidat base64 tetap
dicantumkan sebagai artefak, dengan catatan ditolak.

---

## 3. CRITICAL — Black Box Protocol N4T0: dummy flag di screenshot

`02-black-box-protocol-n4t0-05-flag.md` mengklaim flag
`NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` **diterima platform**.
Screenshot-nya justru menampilkan input dummy:

```
XXX{X0X0_XX0X0X0X_0X0_X0X0XX_X0X_XX0Xx_X0X0Xx}
```

Fakta:
- Platform asli: **0 solves**, 500 pts; kandidat di atas **ditolak** saat disubmit.
- Decode kolom A/B/C benar (`N4T0PH0N3T1C1N1`, `C0mbO_H3X_`, `fl0At_b4r4ng`),
  tetapi susunan flag-nya belum terbukti.
- Flag bisa saja official di `release_map`; itu **belum** bukti accepted.

**Status yang benar:** `OPEN / CANDIDATE` sampai ada submit sukses asli.

---

## 4. HIGH — Shadow Infrastructure sebenarnya SUDAH SOLVED

Halaman `80-shadow-infrastructure*` masih `OPEN` dan memakai flag
`NFX{Villa_Istana_Bunga}` (itu flag challenge **investigation**, bukan Shadow).

Bukti dari `dns_beacon.zip`:
1. `shodan_scan.json`: hostkey `SHA256:8f91c2a40e77b3d1952c`
   → IP `198.51.100.142` → `c2-gate.telemetry-nfx.net`.
2. `ct_certificates.json`: SAN `c2-gate.telemetry-nfx.net` juga mencakup
   `beacon-vault.cdn-nfx.org`.
3. `dns_txt_records.txt`: TXT shard
   `part0=TkZYQ1RGe2RuNV9jdF`, `part1=9sMGdfcDF2MHRfYjM0`,
   `part2=YzBuX2E3MmU0MDkxfQ==`.
4. Gabung + base64 decode:
   `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}` — **accepted**
   (`work/submit_curl_log.jsonl`, `Correct, but already solved`).

**Fix:** ubah status Shadow Infrastructure menjadi VERIFIED, pasang flag yang benar,
dan tulis trail di atas. Ini menaikkan 1 verified dan menghapus 1 OPEN.

---

## 5. HIGH — Typo/case/prefix flag

Ditemukan flag yang tidak konsisten dengan flag accepted:

| Di docs | Seharusnya | Dampak |
|---|---|---|
| `NFXCTF{arsip_merah_204}` | `NFXCTF{arsip_merah_204}` | case salah |
| `NFXCTF{D36A64128F80788B60C677EF94EA7157}` | `NFXCTF{D36A64128F80788B60C677EF94EA7157}` | prefix + typo (`FA` vs `EA`) |
| `NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}` | `NFX{br0tl1_0ob_wr1t3_w0rk3r_r0p_rc3}` | typo `w1r1t3` |
| `NFX{N4T0...}` | kandidat, **belum accepted** | klaim verified salah |
| `NFX{Op3n...}` | kandidat, **belum accepted** | klaim verified salah |
| `NFX{VILLA_ISTANA_BUNGA}` / `villa_istana_bunga_lembang` | untuk Shadow: `NFXCTF{dn5_...}` | flag challenge tertukar |

---

## 6. MEDIUM — Placeholder/format/decoy: hasil verifikasi konteks

Audit lanjutan mengecek setiap kemunculan. **Tidak ada satu pun** yang dipakai
sebagai flag challenge di tabel `Flag` atau halaman `-03-flag` (0 temuan).
Semuanya jatuh ke dua kategori yang sah:

1. **Label format platform** — `NFX{your_flag_here}` dan `NFX{...}` muncul di
   bagian Recon/“Titik penting” atau kutipan brief, artinya “format flag”.
   Bukan klaim flag. Tidak perlu dihapus; boleh dinormalisasi menjadi
   “format flag platform” bila ingin lebih rapi.
2. **Decoy/fixture asli dari challenge** — dipertahankan karena memang bagian
   dari artefak:
   - `NFX{wrong}` — input uji yang ditolak binary reverse.
   - `NFX{LOCAL_TEST_FLAG_*}` — fixture lokal saat exploit dijalankan.
   - `NFX{dummy_flag_for_local_testing}` — flag di Dockerfile reproduksi.
   - `NFX{placeholder_offline_demo}` — flag simulasi offline FlagKeepers.
   - `NFX{th1s_1s_n0t_th3_fl4g}` — decoy di `.rodata`.
   - `NFX{y0u_f0und_th3_wr0ng_4rr4y}` — array decoy JavaScript.
   - `NFX{World_World_World_...}` — decoy challenge OSINT.

**Kesimpulan:** tidak ada flag palsu yang diklaim sebagai flag challenge.
Yang perlu dipastikan hanyalah konteks tiap kemunculan sudah jelas sebagai
format/decoy, dan itu sudah terlihat dari letaknya (Recon/Analisis, bukan Flag).

---

## 7. MEDIUM — 6 challenge C: apa yang kurang dan fix konkret

### 7.1 Forgotten Commit (User) — C
- **Salah IP:** writeup memakai `10.10.20.21`; target asli `10.10.20.21`.
- Langkah terlalu umum (`nmap`, `git-dumper`, SSH) tanpa commit/credential.
- Bukti asli ada di `flags/b2r/ForgottenCommit_SOLVED.md`:
  - `http://10.10.20.21/.git/` → `git-dumper`.
  - Commit `3f4c118` menghapus `ansible/inventory.ini`; parent `bff2915` berisi
    `leonardo:Dev0pment#2026!`.
  - SSH `leonardo@10.10.20.21` → `/home/leonardo/user.txt`.
- **Fix:** ganti IP, tambahkan perintah git-dumper/commit/credential, screenshot asli.

### 7.2 Matryoshka Encoding — C
- Langkah masih “decode berulang”; tidak ada rantai pasti.
- Rantai yang benar:
  1. Tukar setiap pasangan karakter Base64 (kecuali padding `==`).
  2. Base64 decode → header `78 DA`.
  3. zlib decompress → string Base85 RFC1924.
  4. Base85 decode → 40 byte.
  5. XOR dengan key `NFX!` → `NFXCTF{m4try0shk4_0n10n_p33l3d_c309b71e}`.
- **Fix:** tempel solver Python (sudah ada di `writeups/scripts/solve_matryoshka.py`),
  tampilkan output tiap layer, dan tegaskan prefix **NFXCTF** (bukan NFX).

### 7.3 Decode Balik — C
- Attachment `recipe` yang diunduh **bukan recipe**, melainkan halaman aplikasi
  CyberChef (75 KB, isinya hanya contoh resep di modal bantuan).
- Recipe asli ada di metadata challenge (`challenge.json`):
  `https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')Zlib_Deflate('Dynamic%20Huffman%20Coding')To_Base64('A-Za-z0-9%2B/%3D')Generate_Image('Greyscale',1,780)&input=TkZYe1JFREVDVEVEfQ`
- Operasi encode: `To Base64` → `Zlib Deflate` → `To Base64` →
  `Generate Image (Greyscale, 1, 780)`.
- **Fix:** tulis recipe URL + urutan operasi + langkah reverse
  (`From Base64` → `Zlib Inflate` → `From Base64`), bukan “buka recipe”.

### 7.4 13 Is Not Enough — C
- Writeup bilang ROT13 + ROT5, tapi **tidak cocok** dengan ciphertext:
  - Ciphertext: `p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L`
  - ROT13+ROT5: `c0W4L4\E;KWES4^ET>YE0U;WW;GE;KWE\;W:W>UER>NiS^Y`
  - Flag: `NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}`
- Artinya ada layer/transform lain yang belum ditemukan. Jangan klaim “ROT13+ROT5”
  sebagai metode final tanpa menunjukkan output yang menghasilkan flag.
- **Fix:** cari transformasi persis (bandingkan dengan flag known-plaintext),
  atau tandai bagian ini “metode belum berhasil direproduksi”.

### 7.5 Kunci Sudo Sing Kesasar — C
- Writeup bilang “memory leak, token reuse” — **tidak didukung** binary.
- Binary **tersedia** di `qazwsx/pwn/KunciSudoSingKesasar.zip` (ELF non-PIE, not stripped).
- Static finding:
  - `main` membaca rule ke stack `0x400`, `malloc(len+1)` untuk rule,
    `malloc(0x18)` untuk struct `{char owner[16]; int uid; int suid;}`.
  - Rule harus diawali `ALL`; jika `suid == 0` → `buka_kunci()` membaca `flag.txt`.
  - `baca_baris` berhenti di `size-1`; `unescape_copy` menghapus backslash.
- **Fix:** lampirkan binary + `file`/`readelf`/`objdump`/`strings`, jelaskan bug parser
  yang sebenarnya, dan buktikan exploit lokal. Jangan sebut memory leak/token.

### 7.6 Follow Jarvis! — C
- Flag valid (`NFX{Th4nk_Y0u_F0r_Supp0rt1ng_NFXCTF_x_Jarvis}`).
- Ini challenge **admin-assisted**: follow akun Jarvis, buka ticket Discord,
  kirim bukti, admin memberi flag.
- **Fix:** tambahkan screenshot ticket/DM asli, labeli “admin-assisted intro”,
  dan jangan nilai sebagai celah teknis.

---

## 8. MEDIUM — NXPortal (OPEN, jujur)

Halaman NXPortal sudah bagus: analisis header injection, payload, dan blocker
(tidak ada mail sink/route mailbox) ditulis jelas. Pertahankan OPEN.
Saran: tambahkan bukti **response time/payload** dan hasil negatif mail.tm
secara ringkas, serta rencana uji SMTP sink.

---

## 9. Dampak ke grade

| Aspek | Klaim lama | Sebelum fix | Setelah fix |
|---|---:|---:|---:|
| Validitas flag | 9.5/10 | ~7.5/10 (2 flag false verified, 1 solved tapi OPEN) | 9.0/10 (81 verified, 5 OPEN jujur) |
| Kelengkapan | 10/10 | 10/10 | 10/10 |
| Kedalaman | 9/10 | 7.5/10 (6 C masih tipis) | 8.5/10 (6 C diperdalam; 13 masih jujur `UNVERIFIED`) |
| Evidence | 9/10 | **4/10** (mockup, input kosong, statistik palsu) | **8.5/10** (85 terminal evidence asli + 14 NXPortal; 0 mockup) |
| Struktur | 9/10 | 9.5/10 | 9.5/10 |
| **Total** | **9.2/A-** | **~7.7/B+** | **~9.0/A-** |

Grade tidak dinaikkan ke 9.5+ karena: NXPortal/BlackBox/Tempat masih OPEN,
metode `13 Is Not Enough` belum berhasil direproduksi, dan screenshot UI
platform baru tidak tersedia (Turnstile). Yang penting: **tidak ada lagi klaim
VERIFIED yang bertentangan dengan bukti.**

---

## 10. Action plan (prioritas)

1. **Ganti semua `00b-terminal-evidence.png` mockup** dengan bukti asli
   (screenshot platform yang menampilkan flag, atau JSON `submit_curl`).
2. **Tempat Belajar:** ubah ke OPEN/CANDIDATE; jangan klaim CORRECT.
3. **Black Box:** ubah ke OPEN/CANDIDATE; hapus klaim accepted.
4. **Shadow Infrastructure:** VERIFIED + flag `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}`
   + trail `dns_beacon.zip`.
5. **Fix typo flag** §5.
6. **Bersihkan placeholder** §6.
7. **Perdalam 6 C** §7 dengan bukti/command asli.
8. Update index: verified/open count sesuai status nyata.
9. `mkdocs build --strict` dan cek link/asset.

---

## 11. Status setelah audit (patch yang sudah diterapkan)

- **Shadow Infrastructure** → `VERIFIED`, flag
  `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}`, trail `dns_beacon.zip` ditulis.
- **Tempat Belajar** → `OPEN / CANDIDATE`; screenshot yang menampilkan
  `INCORRECT FLAG` dipakai sebagai bukti kegagalan, bukan `CORRECT`.
- **Black Box Protocol N4T0** → `OPEN / CANDIDATE`; screenshot dummy
  `XXX{...}` ditandai tidak valid, log API `Incorrect flag` dipakai.
- **Index** → `81 VERIFIED / 5 OPEN` (sebelumnya 84/2). Dua klaim VERIFIED yang tidak punya submit sukses (Fresh Arrival, Tragedi 9/11) dikoreksi menjadi `OPEN / UNVERIFIED`.
- **Typo/case/prefix**:
  - `NFXCTF{arsip_merah_204}` (bukan `ARSIP_MERAH_204`)
  - `NFXCTF{D36A...EF94EA...}` (bukan `NFX{...EF94FA...}`)
  - `NFX{br0tl1_0ob_wr1t3...}` (bukan `w1r1t3`)
- **Halaman C diperdalam**:
  - Forgotten Commit User: IP `.21`, git-dumper, commit `3f4c118`/`bff2915`,
    credential `leonardo:Dev0pment#2026!`.
  - Matryoshka: solver 5 lapisan (swap Base64 → zlib → Base85 → XOR `NFX!`).
  - Decode Balik: recipe link asli + urutan `To Base64` → `Zlib Deflate` →
    `To Base64` → `Generate Image`.
  - 13 Is Not Enough: jujur bahwa ROT13+ROT5 belum cocok dengan ciphertext;
    metode ditandai `UNVERIFIED`.
  - Kunci Sudo: binary tersedia, static finding parser rule/struct, bukan
    “memory leak token reuse”.
  - Follow Jarvis: ditandai admin-assisted + langkah ticket.
- **`mkdocs build --strict`** → **PASS**.

### Penggantian mockup → terminal evidence asli

- **84 file** `00b-submit-platform.png` diganti namanya menjadi
  `00b-terminal-evidence.png`.
- **76** di antaranya memakai screenshot terminal asli yang sudah ada di folder
  challenge yang sama (output solver/eksploit/flag).
- **8** dirender ulang dari log/perintah asli: 6 challenge C (Forgotten Commit
  User, Matryoshka, Decode Balik, 13 Is Not Enough, Kunci Sudo, Follow Jarvis)
  + Black Box (log API `Incorrect flag`) + Tempat Belajar (log API
  `Incorrect flag`).
- **1 tambahan** untuk **Shadow Infrastructure** yang sebelumnya tidak punya
  evidence sama sekali: capture terminal asli dari `dns_beacon.zip` (fingerprint
  → passive DNS → CT SAN → TXT shard → base64) + log submit accepted.
- **NXPortal** memakai **14 screenshot terminal asli** + 14 transkrip yang sudah
  ada (tidak dipaksa punya `00b` karena flag memang belum ditemukan).
- Total sekarang: **85 `00b-terminal-evidence.png` + 303 `term-*.png` = 388
  terminal screenshot**.
- **269 referensi markdown** diperbarui; **0** referensi ke nama lama.
- Klaim lama yang menyesatkan dihapus: input flag kosong, input dummy
  `XXX{...}`, dan statistik palsu (`20/25/45 solves`, 100–300 pts).
- **Screenshot UI platform tidak diklaim ada.** Platform baru memakai
  `api.nxctf.my.id` + Cloudflare Turnstile dan tidak bisa diakses tanpa login;
  karena itu bukti yang sah adalah terminal/API log, bukan tangkapan layar UI.
- Label di semua halaman diubah menjadi “Terminal evidence (real)”,
  bukan “screenshot submit”.

### Hasil build

- `mkdocs build --strict` → **PASS**.
- 0 referensi gambar/link rusak (dicek dengan skrip audit).
- Index: **81 VERIFIED / 5 OPEN**, konsisten dengan badge 86 halaman challenge.

### Status akhir yang jujur

| Challenge | Status | Catatan |
|---|---|---|
| Shadow Infrastructure | `VERIFIED` | flag `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}` |
| NXPortal | `OPEN` | tidak ada mail sink/route mailbox |
| Black Box Protocol N4T0 | `OPEN / CANDIDATE` | kandidat ditolak; 0 solves |
| Tempat Belajar | `OPEN / CANDIDATE` | base64 ditolak; flag mungkin di DM Instagram |
| Fresh Arrival | `OPEN / UNVERIFIED` | solved lokal (JetPhotos/Wikidata), belum disubmit |
| Tragedi 9/11 | `OPEN / UNVERIFIED` | solved lokal (git history), belum disubmit |

**Yang masih butuh aksi pengguna (bukan edit teks):** login platform baru
(`api.nxctf.my.id` + Turnstile) untuk menangkap screenshot UI, dan akses DM
Instagram `@dihlearn.id` untuk Tempat Belajar. Tanpa itu, status OPEN tetap
dipertahankan — tidak dipaksa menjadi VERIFIED.
