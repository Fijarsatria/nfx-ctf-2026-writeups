# Shadow Infrastructure

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Osint</span><span class="nx-chip">Easy</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Osint` |
| Difficulty | `Easy` |
| Poin (snapshot) | `300` |
| Author | `Illal` |
| Tools | unzip, jq, grep, base64 |
| Flag | `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/shadow-infrastructure/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Hostkey `SHA256:8f91c2a40e77b3d1952c` adalah satu-satunya petunjuk.
Dari situ kita pivot ke scanner publik (Shodan), lalu ke Certificate Transparency
untuk menemukan domain `beacon-vault.cdn-nfx.org`. DNS TXT record domain itu
menyimpan tiga shard base64 yang harus digabung. Hasilnya adalah flag.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Jejak Awal | hostkey `SHA256:8f91c2a40e77b3d1952c` + `dns_beacon.zip` | [Buka](80-shadow-infrastructure-01-jejak-awal.md) |
| 2 | Cara Mendapatkan Flag | shodan → CT log → DNS TXT → base64 | [Buka](80-shadow-infrastructure-02-cara-mendapatkan-flag.md) |
| 3 | Flag | `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}` | [Buka](80-shadow-infrastructure-03-flag.md) |
| 4 | Bukti / Evidence | isi `dns_beacon.zip` + log submit | [Buka](80-shadow-infrastructure-04-bukti-evidence.md) |
| 5 | Referensi | Shodan, crt.sh/CT, DNS TXT, base64 | [Buka](80-shadow-infrastructure-05-referensi.md) |

## TL;DR

- `shodan_scan.json`: fingerprint `SHA256:8f91c2a40e77b3d1952c` cocok dengan
  IP `198.51.100.142` dan domain `c2-gate.telemetry-nfx.net`.
- `ct_certificates.json`: sertifikat `c2-gate.telemetry-nfx.net` juga memiliki
  SAN `beacon-vault.cdn-nfx.org`.
- `dns_txt_records.txt`: TXT shard target:
  `part0=TkZYQ1RGe2RuNV9jdF`, `part1=9sMGdfcDF2MHRfYjM0`,
  `part2=YzBuX2E3MmU0MDkxfQ==`.
- Gabung + `base64 -d` →
  `NFXCTF{dn5_ct_l0g_p1v0t_b34c0n_a72e4091}`.
- Record `health-check.cdn-nfx.org` (`password=decoy12345`,
  `user=admin678901`) adalah **decoy**; yang benar `beacon-vault`.

## Terminal evidence (real)

![00b-terminal-evidence.png](assets/shadow-infrastructure/00b-terminal-evidence.png)

*Capture terminal asli: fingerprint → passive DNS → CT SAN → DNS TXT shard →
base64 → flag, ditutup dengan log submit `Correct, but already solved`.*

## Catatan audit

Halaman ini sebelumnya berstatus `OPEN` dan memakai flag challenge lain
(`NFX{Villa_Istana_Bunga}`). Audit 2026-11-12 mengoreksi status, flag, dan
metode berdasarkan isi `dns_beacon.zip` serta log submit asli
`Correct, but already solved`.
