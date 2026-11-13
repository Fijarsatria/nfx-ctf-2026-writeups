# Metadata & Snapshot — NFX CTF 2026

**Snapshot:** 2026-11-13. Halaman ini menjelaskan metadata challenge dan membedakan **status flag** dari **status metode**.

## Dynamic scoring

Platform memakai *dynamic scoring*: `max_points`, `decay_per_solve`, dan `min_points`. Artinya poin challenge berubah mengikuti jumlah solve. Kolom **Poin snapshot** adalah poin yang tercatat saat writeup disusun; kolom **Poin live** adalah poin di API saat snapshot. Keduanya bisa berbeda.

## Status metode

| Badge | Arti |
|---|---|
| **FULL** | Metode utama berhasil direproduksi dari artefak/writeup. |
| **PARTIAL** | Flag valid, tetapi satu atau lebih langkah metode belum sepenuhnya direproduksi. |
| **ADMIN** | Flag diperoleh dengan bantuan admin/event staff. |
| **OPEN** | Flag belum ditemukan. |

## Tabel metadata 86 challenge

| Challenge | Track | Kategori | Difficulty | Poin snapshot | Poin live | Solves live | Author | Metode |
|---|---|---|---|---:|---:|---:|---|---|
| NXPortal | NF | Web | Medium | 480 | 480 | 2 | Ariaf | **OPEN** |
| S3rvice K3reta | Extend | Osint | Hard | 480 | 440 | 4 | Kada | **FULL** |
| Left Behind in the Metadata | NF | Osint | Baby | 440 | 440 | 4 | — | **FULL** |
| Progress Bar (Root) | Extend | Boot To Root | Hard | 460 | 420 | 5 | Ariaf | **FULL** |
| Progress Bar (User) | Extend | Boot To Root | Hard | 460 | 420 | 5 | Ariaf | **FULL** |
| Record Keeper (User) | Extend | Boot To Root | Medium | 460 | 400 | 6 | Ariaf | **FULL** |
| Record Keeper (Root) | Extend | Boot To Root | Medium | 460 | 400 | 6 | Ariaf | **FULL** |
| Career Tempat Belajar | NF | Osint | Medium | 380 | 380 | 7 | Kada | **FULL** |
| Talatah Ti Peuntas | Extend | Pwn | Hard | 440 | 360 | 8 | Amablex | **FULL** |
| THE FORGOTTEN STATE | Extend | Pwn | Hard | 340 | 300 | 11 | Amablex | **FULL** |
| Bluebird Session | Extend | Forensics | Hard | 420 | 300 | 11 | Ariaf | **FULL** |
| Tempat Belajar | NF | Osint | Easy | 300 | 300 | 11 | Kada | **PARTIAL** |
| Commit yang kehapus | NF | Osint | Baby | 260 | 260 | 13 | — | **FULL** |
| Follow Jarvis! | NF | Linux | Easy | 250 | 250 | 41 | — | **ADMIN-ASSISTED** |
| Starved | Extend | Pwn | Medium | 380 | 240 | 14 | Kesatria Baja Ringan | **FULL** |
| NexusGate | Extend | Web | Hard | 320 | 240 | 14 | Ariaf | **FULL** |
| NarrowGate | Extend | Pwn | Insane | 380 | 240 | 14 | Kesatria Baja Ringan | **FULL** |
| LinkVault | Extend | Web | Hard | 360 | 240 | 14 | Ariaf | **FULL** |
| The Ghost Operator | Extend | Osint | Medium | 380 | 220 | 15 | Ariaf | **FULL** |
| Access Remains | Extend | Forensics | Hard | 360 | 220 | 15 | Ariaf | **FULL** |
| Panggilan Terakhir | Extend | Forensics | Medium | 380 | 200 | 16 | Candelena | **FULL** |
| NFXCTF Convention | NF | Pwn | Medium | 280 | 200 | 16 | Kada | **FULL** |
| Fresh Arrival | Extend | Osint | Medium | 340 | 200 | 16 | Ariaf | **FULL** |
| Unbreakable Delay | Extend | Crypto | Medium | 360 | 180 | 17 | Kad | **FULL** |
| FlagKeepers | Extend | Crypto | Hard | 440 | 180 | 17 | Ariaf | **FULL** |
| SymHell | Extend | Misc | Medium | 340 | 180 | 17 | Ariaf | **FULL** |
| Weak Handshake | Extend | Forensics | Medium | 360 | 180 | 17 | Ariaf | **FULL** |
| Gateway Under Pressure | Extend | Pwn | Medium | 300 | 180 | 17 | Amablex | **FULL** |
| ChangeTrack | Extend | Web | Medium | 300 | 180 | 17 | Ariaf | **FULL** |
| Pipa Nu Kotor | Extend | Pwn | Medium | 300 | 160 | 18 | Amablex | **FULL** |
| Heker Tersenyum - Art Evidence Secret | NF | Forensics | Medium | 280 | 140 | 19 | salep88 | **FULL** |
| PageStream | Extend | Web | Hard | 320 | 140 | 19 | Ariaf | **FULL** |
| Tragedi 9/11 | Extend | Osint | Hard | 380 | 140 | 19 | salep88 | **FULL** |
| My Lovely Freya | Extend | Misc | Hard | 320 | 140 | 19 | salep88 | **FULL** |
| Hard Feistel | Extend | Reverse | Hard | 230 | 125 | 26 | cypera | **FULL** |
| Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh | NF | Crypto | Medium | 200 | 120 | 20 | Illal | **PARTIAL** |
| Pipeline Phantom | NF | Misc | Easy | 120 | 120 | 20 | Ariaf | **FULL** |
| Black Box Protocol N4T0 | NF | Crypto | Medium | 280 | 120 | 20 | Kada | **FULL** |
| Forgotten Commit (Root) | NF | Boot To Root | Medium | 100 | 100 | 29 | Ariaf | **FULL** |
| File Analysis: The Suspicious Invoice | NF | Forensics | Easy | 100 | 100 | 38 | Zer0 | **FULL** |
| Invoice | NF | Forensics | Easy | 100 | 100 | 48 | Kesatria Baja Ringan | **FULL** |
| Dokodemo Door | Extend | Misc | Medium | 160 | 100 | 21 | Kada | **FULL** |
| Castaway | Extend | Reverse | Hard | 100 | 100 | 27 | Kesatria Baja Ringan | **FULL** |
| Easy Config Decoy | NF | Reverse | Easy | 260 | 100 | 53 | cypera | **FULL** |
| Baby Python | NF | Reverse | Baby | 200 | 100 | 59 | cypera | **FULL** |
| Baby Strings | NF | Reverse | Baby | 200 | 100 | 59 | cypera | **FULL** |
| ECDSA Nonce Bias | Extend | Crypto | Hard | 260 | 100 | 21 | rio | **FULL** |
| Twin Prime Lattice | NF | Crypto | Easy | 100 | 100 | 52 | rio | **FULL** |
| Kebakaran | NF | Osint | Easy | 100 | 100 | 47 | KBR | **PARTIAL** |
| 13 Is Not Enough | NF | Crypto | Easy | 100 | 100 | 29 | Ariaf | **FULL** |
| Kunci Sudo Sing Kesasar | NF | Pwn | Easy | 100 | 100 | 22 | Amablex | **PARTIAL** |
| NexaDocs | NF | Web | Easy | 100 | 100 | 37 | Ariaf | **FULL** |
| NexaPartner | NF | Web | Medium | 200 | 100 | 23 | Ariaf | **FULL** |
| NexaIdentity | NF | Web | Medium | 120 | 100 | 26 | Ariaf | **FULL** |
| Broken Signature Scheme | Extend | Crypto | Hard | 180 | 100 | 24 | rio | **FULL** |
| Medium RC4 | Extend | Reverse | Medium | 100 | 100 | 32 | cypera | **FULL** |
| Shadow Infrastructure | NF | Osint | Easy | 300 | 100 | 43 | Illal | **FULL** |
| Dead Drop | NF | Forensics | Baby | 100 | 100 | 32 | Ariaf | **FULL** |
| NexaDeploy | NF | Web | Easy | 100 | 100 | 36 | Ariaf | **FULL** |
| Omah Buffer Kebak | NF | Pwn | Baby | 100 | 100 | 32 | Amablex | **FULL** |
| Easy JS Obfuscation | NF | Reverse | Easy | 260 | 100 | 53 | cypera | **FULL** |
| THE BROKEN RESOURCE PARSER | NF | Pwn | Easy | 100 | 100 | 33 | Amablex | **FULL** |
| Cleartext Sniffing | NF | Forensics | Baby | 180 | 100 | 60 | Candelena | **FULL** |
| Image Metadata | NF | Forensics | Easy | 220 | 100 | 61 | Candelena | **FULL** |
| Perimeter Breach | NF | Forensics | Medium | 100 | 100 | 39 | Ariaf | **FULL** |
| Forgotten Commit (User) | NF | Boot To Root | Easy | 100 | 100 | 37 | Ariaf | **FULL** |
| Frekuensi Sunyi | NF | Misc | Medium | 180 | 100 | 24 | syahril | **FULL** |
| Wujud Aseli Atmin | NF | Misc | Medium | 420 | 100 | 30 | Syahril | **FULL** |
| Baby XOR | NF | Reverse | Baby | 260 | 100 | 58 | cypera | **FULL** |
| Medium TEA | Extend | Reverse | Medium | 100 | 100 | 30 | cypera | **FULL** |
| NexaCommerce | NF | Web | Easy | 100 | 100 | 35 | Ariaf | **FULL** |
| Titipan Akhir Tahun | NF | Misc | Easy | 100 | 100 | 50 | Syahril | **FULL** |
| insider | NF | Forensics | Medium | 100 | 100 | 34 | Zer0 | **FULL** |
| Matryoshka Encoding | NF | Misc | Easy | 100 | 100 | 25 | Illal | **FULL** |
| RSA Coppersmith cihuy | Extend | Crypto | Medium | 120 | 100 | 26 | Illal | **FULL** |
| Ghost XOR | NF | Crypto | Baby | 100 | 100 | 67 | Candelena | **FULL** |
| NexaRewards | NF | Web | Easy | 100 | 100 | 38 | Ariaf | **FULL** |
| Static IV Offline | Extend | Crypto | Medium | 140 | 100 | 29 | rio | **FULL** |
| Stay | Extend | Misc | Medium | 340 | 100 | 21 | Kesatria Baja Ringan | **FULL** |
| Decode Balik | NF | Crypto | Easy | 100 | 100 | 45 | Ariaf | **FULL** |
| The Alchemist's Sandbox | Extend | Misc | Medium | 240 | 100 | 24 | Illal | **FULL** |
| Notulen Senin Pagi | NF | Misc | Baby | 100 | 100 | 58 | Syahril | **FULL** |
| NexaSupply | NF | Web | Baby | 100 | 100 | 52 | Ariaf | **FULL** |
| Easy Bash Layers | NF | Reverse | Easy | 260 | 100 | 54 | cypera | **FULL** |
| Feistel Differential | NF | Crypto | Medium | 100 | 100 | 31 | Illal | **FULL** |
| Hard VM Bytecode | Extend | Reverse | Hard | 100 | 100 | 27 | cypera | **FULL** |

## Catatan konsistensi

- **Follow Jarvis!** dikategorikan `Linux` di API. Halaman overview tetap menampilkan track Mahasiswa NF; kategori di tabel ini mengikuti API.
- **Poin** di halaman challenge adalah snapshot, bukan poin live. Perbedaan dengan API wajar karena dynamic scoring.
- **Solves live** diambil saat snapshot 2026-11-13; bisa bertambah setelahnya.
- **Author** diambil dari deskripsi challenge di platform. Jika tidak ada, ditulis `—`.
