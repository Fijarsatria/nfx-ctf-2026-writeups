# The Ghost Operator — Analisis

[← Overview](35-the-ghost-operator.md) · [Index](index.md)

### 2.1 Commit dan tanda tangan GPG

```bash
$ cd investigation/investigation
$ git log --all --oneline --decorate
d2627a7 (HEAD -> main) audit: final system integrity verification before handoff

$ git log --show-signature -1
gpg: Signature made Mon Oct 26 01:49:05 2026 WIB
gpg:                using RSA key B17171D40DE252F193E79707E6BE71CA2BD84A4E
gpg: Good signature from "Dimas Wirawan
     (rentry.co/ghost-route-0914)
     <ghost.operator.rentry@veloxphantom.net>" [unknown]
```

Commit mentah:

```text
tree 9c66f5f6c7a0e9d97984a6ee7d14d3aaab7c7922
author Dimas Wirawan <dimas.wirawan@netmetrics-net.example> 1792954132 +0700
committer Dimas Wirawan <dimas.wirawan@netmetrics-net.example> 1792954132 +0700
gpgsig -----BEGIN PGP SIGNATURE-----
...
```

`git config` juga menyimpan `signingkey = E6BE71CA2BD84A4E`.

### 2.2 Enumerasi keyserver

Key ID `E6BE71CA2BD84A4E` dapat diambil dari keyserver. UID-nya membocorkan
URL:

```text
Dimas Wirawan (rentry.co/ghost-route-0914)
<ghost.operator.rentry@veloxphantom.net>
```

Pencarian keyserver untuk domain `veloxphantom.net` menemukan **tiga key**:

| Fingerprint | UID |
|---|---|
| `A0BE3884C3DA0ED27A6D627338353AD29DC58103` | `Dimas Wirawan (telegra.ph/Field-Notes-0914-Escape-Route-10-25-2) <ghost.operator@veloxphantom.net>` |
| `BE7BB77BC5DC29E31149C1F9C92E23B3427F0BBC` | `Dimas Wirawan (telegra.ph/Field-Notes-0914-Escape-Route-10-25) <ghost.operator@veloxphantom.net>` |
| `B17171D40DE252F193E79707E6BE71CA2BD84A4E` | `Dimas Wirawan (rentry.co/ghost-route-0914) <ghost.operator.rentry@veloxphantom.net>` |

Ketiganya self-signed, dibuat dalam rentang waktu berdekatan
(2026-10-25). Ini menunjukkan operator membuat beberapa relay mirror.

### 2.3 Field notes di telegra.ph

Dua URL telegra.ph dapat diakses langsung. Ternyata ada juga varian `-3`
yang tidak direferensikan key mana pun. Isi ketiganya sama:

```text
[TIMESTAMP: 2026-10-24 03:15 UTC]
[STATUS: CODE ORANGE - OPERATOR BURN NOTICE]
...
Log Pelarian & Rute Safehouse:
Keluar dari Jakarta via Tol Cipularang menuju Bandung Barat.
Exit Pasteur, potong rute via Jl. Sersan Bajuri ke arah
Parongpong - Lembang untuk menghindari monitoring kamera ETLE di jalur
arteri utama.
Titik persembunyian: Komplek villa pegunungan di kaki Gunung Burangrang,
sepanjang Jl. Kolonel Masturi KM 9, Parongpong, kawasan Lembang.
Area dingin berkabut dengan arsitektur villa bertaman bunga tematik.
Sinyal seluler teredam lembah, aman dari pelacakan BTS.
Catatan: Lokasi safehouse dikenal warga lokal dan wisatawan sebagai
kompleks villa terbesar di Parongpong-Lembang.
Menunggu instruksi lebih lanjut via dead-drop GPG.
Over and out. // Velox Ghost
```

### 2.4 Snapshot rentry

`rentry.co/ghost-route-0914` sekarang menampilkan:

```text
[NODE DECOMMISSIONED - TRACES PURGED BY OPERATOR]
Status: Content shredded using DoD 5220.22-M sanitization.
```

Namun snapshot Wayback `20261025190602` masih menyimpan isi asli
`[BURST TRANSMISSION - 0914]`. Isinya sama dengan telegra.ph: rute Jakarta →
Tol Cipularang → Exit Pasteur → Jl. Sersan Bajuri → Parongpong/Lembang →
Jl. Kolonel Masturi KM 9, safehouse di kompleks villa kaki Gunung
Burangrang dengan taman bunga tematik, kompleks villa terbesar di
Parongpong–Lembang.

### 2.5 Identifikasi tempat

Empat elemen kunci:

1. **Jl. Kolonel Masturi KM 9**, Parongpong/Lembang.
2. **Kaki Gunung Burangrang**.
3. **Kompleks villa dengan taman bunga tematik**.
4. **Kompleks villa terbesar di Parongpong–Lembang**.

Sumber publik yang cocok:

- **Villa Istana Bunga (VIB)** — `penginapan.net` (15 Mei 2024) menyebut
  “kompleks villa seluas 42 hektar ... di bawah kaki Gunung Tangkuban
  Perahu yang bersebelahan dengan Gunung Burangrang”, alamat
  “Jl. Kolonel Masturi Km. 9, Parongpong, Cisarua, Lembang”, dan judul
  “Komplek Villa Terbesar di Lembang”.
- **villalembang09.com** menyebut “Villa Istana Bunga Lembang ... di
  jl. kolonel masturi km 9 parongpong lembang merupakan kawasan komplek
  villa terbesar di lembang”, luas ±42 hektar, ±300 unit villa.
- **sewavillabdg.com** (6 Mei 2026) menyebut “salah satu kompleks villa
  terbesar di kawasan Lembang ... Jl. Kolonel Masturi Km-9”.

Belum ditemukan kandidat lain di KM 9 yang memenuhi keempat elemen
sekaligus. Jadi safehouse yang dimaksud paling mungkin adalah
**Villa Istana Bunga (VIB)**.

### 2.6 Mengapa lowercase ditolak?

Deskripsi challenge meminta “huruf kecil semua, spasi diganti underscore”,
sehingga secara logis jawabannya:

```text
NFX{villa_istana_bunga}
```

Namun kandidat ini **ditolak** oleh platform. Kemungkinan penyebab:

1. **Author memakai ulang flag wave 1 tanpa normalisasi**: string yang
   pernah accepted adalah `NFX{Villa_Istana_Bunga}` (huruf kapital).
   Platform membandingkan case-sensitive.
2. **Ejaan “Vila” vs “Villa”**: bahasa Indonesia sering menulis “Vila”
   (satu L), sedangkan nama resmi kompleks memakai “Villa” (dua L).
3. **Nama yang diharapkan lebih pendek**: `NFX{istana_bunga}` atau
   `NFX{istanabunga}`.
4. **Nama lengkap dengan lokasi**: `NFX{villa_istana_bunga_lembang}`.

Verifikasi akhir: `NFX{villa_istana_bunga_lembang}` diterima platform
(`Correct! +380 points.`). Kandidat `NFX{villa_istana_bunga}` dan
`NFX{Villa_Istana_Bunga}` ditolak. Jadi author memakai nama tempat +
lokasi `lembang`, bukan hanya nama kompleks villa.
