# NFX CTF 2026 — Writeup Medium–Hard

**368 halaman** untuk **52 challenge**. Setiap challenge dipecah menjadi Overview, Recon, Analisis, Eksploitasi, Flag, Evidence, dan Referensi (jika ada).

## Ringkasan

- Challenge: **52** — Medium **33**, Hard **18**, Insane **1** (bonus)
- Total halaman: **368**
- Status: **51 verified/candidate**, **1 open** (NXPortal)
- Format flag: `NFX{...}`

## Cara pakai

1. **GitHub Pages**: pakai folder `writeups/github-pages/` (MkDocs Material, 368 halaman, screenshot ikut ter-build).
2. **HackMD Book**: import folder ini; `SUMMARY.md` sudah berisi urutan semua halaman.
3. **Satu note**: `ALL_IN_ONE.md` (backup; ukurannya besar).

## Daftar challenge

Status: `VERIFIED` = flag diterima platform; `CANDIDATE` = flag dari artefak, cek halaman verifikasi; `OPEN` = belum solved.

| No | Challenge | Difficulty | Poin | Status | Halaman |
|---:|---|---|---:|---|---:|
| 1 | Forgotten Commit (Root)<br><sub>NF · Boot To Root</sub> | Medium | 100 | VERIFIED | [7](01-forgotten-commit-root.md) |
| 2 | Black Box Protocol N4T0<br><sub>NF · Crypto</sub> | Medium | 280 | CANDIDATE | [7](02-black-box-protocol-n4t0.md) |
| 3 | Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh<br><sub>NF · Crypto</sub> | Medium | 200 | VERIFIED | [7](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh.md) |
| 4 | Feistel Differential<br><sub>NF · Crypto</sub> | Medium | 100 | VERIFIED | [7](04-feistel-differential.md) |
| 5 | Heker Tersenyum - Art Evidence Secret<br><sub>NF · Forensics</sub> | Medium | 280 | VERIFIED | [7](05-heker-tersenyum-art-evidence-secret.md) |
| 6 | insider<br><sub>NF · Forensics</sub> | Medium | 100 | VERIFIED | [7](06-insider.md) |
| 7 | Perimeter Breach<br><sub>NF · Forensics</sub> | Medium | 100 | VERIFIED | [7](07-perimeter-breach.md) |
| 8 | Frekuensi Sunyi<br><sub>NF · Misc</sub> | Medium | 180 | VERIFIED | [7](08-frekuensi-sunyi.md) |
| 9 | Career Tempat Belajar<br><sub>NF · Osint</sub> | Medium | 380 | VERIFIED | [7](09-career-tempat-belajar.md) |
| 10 | NFXCTF Convention<br><sub>NF · Pwn</sub> | Medium | 280 | VERIFIED | [7](10-nfxctf-convention.md) |
| 11 | NexaIdentity<br><sub>NF · Web</sub> | Medium | 120 | VERIFIED | [7](11-nexaidentity.md) |
| 12 | NexaPartner<br><sub>NF · Web</sub> | Medium | 200 | VERIFIED | [7](12-nexapartner.md) |
| 13 | NXPortal<br><sub>NF · Web</sub> | Medium | 480 | OPEN | [8](13-nxportal.md) |
| 14 | Progress Bar (Root)<br><sub>Extend · Boot To Root</sub> | Hard | 460 | VERIFIED | [7](14-progress-bar-root.md) |
| 15 | Progress Bar (User)<br><sub>Extend · Boot To Root</sub> | Hard | 460 | CANDIDATE | [7](15-progress-bar-user.md) |
| 16 | Record Keeper (Root)<br><sub>Extend · Boot To Root</sub> | Medium | 460 | VERIFIED | [7](16-record-keeper-root.md) |
| 17 | Record Keeper (User)<br><sub>Extend · Boot To Root</sub> | Medium | 460 | VERIFIED | [7](17-record-keeper-user.md) |
| 18 | Broken Signature Scheme<br><sub>Extend · Crypto</sub> | Hard | 180 | VERIFIED | [7](18-broken-signature-scheme.md) |
| 19 | ECDSA Nonce Bias<br><sub>Extend · Crypto</sub> | Hard | 260 | VERIFIED | [7](19-ecdsa-nonce-bias.md) |
| 20 | FlagKeepers<br><sub>Extend · Crypto</sub> | Hard | 440 | VERIFIED | [7](20-flagkeepers.md) |
| 21 | RSA Coppersmith cihuy<br><sub>Extend · Crypto</sub> | Medium | 120 | VERIFIED | [7](21-rsa-coppersmith-cihuy.md) |
| 22 | Static IV Offline<br><sub>Extend · Crypto</sub> | Medium | 140 | VERIFIED | [7](22-static-iv-offline.md) |
| 23 | Unbreakable Delay<br><sub>Extend · Crypto</sub> | Medium | 360 | VERIFIED | [7](23-unbreakable-delay.md) |
| 24 | Access Remains<br><sub>Extend · Forensics</sub> | Hard | 360 | VERIFIED | [8](24-access-remains.md) |
| 25 | Bluebird Session<br><sub>Extend · Forensics</sub> | Hard | 420 | VERIFIED | [8](25-bluebird-session.md) |
| 26 | Panggilan Terakhir<br><sub>Extend · Forensics</sub> | Medium | 380 | VERIFIED | [7](26-panggilan-terakhir.md) |
| 27 | Weak Handshake<br><sub>Extend · Forensics</sub> | Medium | 360 | VERIFIED | [7](27-weak-handshake.md) |
| 28 | Dokodemo Door<br><sub>Extend · Misc</sub> | Medium | 160 | VERIFIED | [7](28-dokodemo-door.md) |
| 29 | My Lovely Freya<br><sub>Extend · Misc</sub> | Hard | 320 | VERIFIED | [7](29-my-lovely-freya.md) |
| 30 | Stay<br><sub>Extend · Misc</sub> | Medium | 340 | VERIFIED | [7](30-stay.md) |
| 31 | SymHell<br><sub>Extend · Misc</sub> | Medium | 340 | VERIFIED | [7](31-symhell.md) |
| 32 | The Alchemist's Sandbox<br><sub>Extend · Misc</sub> | Medium | 240 | VERIFIED | [7](32-the-alchemists-sandbox.md) |
| 33 | Fresh Arrival<br><sub>Extend · Osint</sub> | Medium | 340 | VERIFIED | [7](33-fresh-arrival.md) |
| 34 | S3rvice K3reta<br><sub>Extend · Osint</sub> | Hard | 480 | VERIFIED | [7](34-s3rvice-k3reta.md) |
| 35 | The Ghost Operator<br><sub>Extend · Osint</sub> | Medium | 380 | VERIFIED | [7](35-the-ghost-operator.md) |
| 36 | Tragedi 9/11<br><sub>Extend · Osint</sub> | Hard | 380 | VERIFIED | [7](36-tragedi-9-11.md) |
| 37 | Gateway Under Pressure<br><sub>Extend · Pwn</sub> | Medium | 300 | VERIFIED | [7](37-gateway-under-pressure.md) |
| 38 | NarrowGate<br><sub>Extend · Pwn</sub> | Insane | 380 | VERIFIED | [7](38-narrowgate.md) |
| 39 | Pipa Nu Kotor<br><sub>Extend · Pwn</sub> | Medium | 300 | VERIFIED | [7](39-pipa-nu-kotor.md) |
| 40 | Starved<br><sub>Extend · Pwn</sub> | Medium | 380 | VERIFIED | [7](40-starved.md) |
| 41 | Talatah Ti Peuntas<br><sub>Extend · Pwn</sub> | Hard | 440 | VERIFIED | [7](41-talatah-ti-peuntas.md) |
| 42 | THE FORGOTTEN STATE<br><sub>Extend · Pwn</sub> | Hard | 340 | VERIFIED | [7](42-the-forgotten-state.md) |
| 43 | Castaway<br><sub>Extend · Reverse</sub> | Hard | 100 | VERIFIED | [7](43-castaway.md) |
| 44 | Hard Feistel<br><sub>Extend · Reverse</sub> | Hard | 230 | VERIFIED | [7](44-hard-feistel.md) |
| 45 | Hard VM Bytecode<br><sub>Extend · Reverse</sub> | Hard | 100 | VERIFIED | [7](45-hard-vm-bytecode.md) |
| 46 | Medium RC4<br><sub>Extend · Reverse</sub> | Medium | 100 | VERIFIED | [7](46-medium-rc4.md) |
| 47 | Medium TEA<br><sub>Extend · Reverse</sub> | Medium | 100 | VERIFIED | [7](47-medium-tea.md) |
| 48 | ChangeTrack<br><sub>Extend · Web</sub> | Medium | 300 | VERIFIED | [7](48-changetrack.md) |
| 49 | LinkVault<br><sub>Extend · Web</sub> | Hard | 360 | VERIFIED | [7](49-linkvault.md) |
| 50 | NexusGate<br><sub>Extend · Web</sub> | Hard | 320 | VERIFIED | [7](50-nexusgate.md) |
| 51 | PageStream<br><sub>Extend · Web</sub> | Hard | 320 | VERIFIED | [7](51-pagestream.md) |
| 52 | Wujud Aseli Atmin<br><sub>NF · Misc</sub> | Medium | 420 | VERIFIED | [8](52-wujud-aseli-atmin.md) |

## Catatan

- **NXPortal** masih OPEN; halaman-halamannya berisi analisis/blocker, bukan flag.
- **Black Box Protocol N4T0** dan **Progress Bar (User)** berstatus `CANDIDATE`; cek halaman Flag masing-masing.
- **NarrowGate** adalah bonus Insane dan tetap disertakan.
