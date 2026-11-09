# insider

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `Zer0` |
| Tools | python3, exiftool, git |
| Flag | `NFX{wraithbyte_cve202421412_20250314_zenvpn271}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Artefak hanya berupa profil Chrome (`ChromeProfile/`), tanpa disk image dan tanpa log server.
- `History` menunjukkan riset UAC bypass, CVE-2024-21412, download `uacme.zip`, dan login ke `0x00sec.org` dengan username **wraithbyte**.
- `Login Data` menyimpan password `v10` (AES-GCM + DPAPI), tetapi **tidak ada master key DPAPI** di paket; password tidak perlu dipecahkan untuk mendapatkan flag.
- Extension non-webstore **ZenVPN 2.7.1** dan timestamp bookmark/search **20250314** melengkapi komponen flag.
- Flag disusun dari empat artefak: `wraithbyte` + `cve202421412` + `20250314` + `zenvpn271`.

## Navigasi Halaman

- [Recon](06-insider-01-recon.md)
- [Analisis](06-insider-02-analisis.md)
- [Eksploitasi / Solver](06-insider-03-eksploitasi-solver.md)
- [Flag](06-insider-04-flag.md)
- [Bukti / Evidence](06-insider-05-bukti-evidence.md)
- [Referensi](06-insider-06-referensi.md)
