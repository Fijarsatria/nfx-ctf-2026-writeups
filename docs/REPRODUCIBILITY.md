# Reproducibility — Cara Menjalankan Solver

**Snapshot:** 2026-11-13. Halaman ini menjelaskan cara menjalankan solver yang
disertakan di repo, input yang dibutuhkan, dan output yang diharapkan.

## Konvensi path

- Di repo, semua evidence berada di `docs/assets/<slug>/`.
- Di situs, path yang sama tampil sebagai `assets/<slug>/`.
- Semua solver di halaman ini dijalankan **dari folder challenge**:

```bash
cd docs/assets/<slug>
python3 solve.py
```

- Placeholder `<repo>` berarti root repo writeup (folder yang berisi `docs/`).

## Prasyarat

```bash
python3 -m pip install pycryptodome fpylll z3-solver pwntools pillow numpy scipy matplotlib
```

- `pycryptodome` — AES/RSA helper.
- `fpylll` — lattice/LLL (ECDSA, LWE).
- `z3-solver` — model Feistel differential.
- `pwntools` — exploit Pwn.
- `pillow`, `numpy`, `scipy`, `matplotlib` — forensics/misc.

## Solver yang sudah diuji ulang

Semua perintah di bawah dijalankan ulang pada snapshot ini dan menghasilkan
flag yang sama dengan yang diterima platform.

| Challenge | Script | Input | Perintah | Output |
|---|---|---|---|---|
| ECDSA Nonce Bias | [`solve.py`](assets/ecdsa-nonce-bias/solve.py) | [`output.txt`](assets/ecdsa-nonce-bias/output.txt) | `cd docs/assets/ecdsa-nonce-bias && python3 solve.py` | `NXCTF{ecds4_hnp_n0nc3_b14s_8b1t_l4tt1c3_a3d2ae498097}` |
| Static IV Offline | [`solve.py`](assets/static-iv-offline/solve.py) | [`output.txt`](assets/static-iv-offline/output.txt) | `cd docs/assets/static-iv-offline && python3 solve.py` | `NXCTF{cbc_1v_r3u53_l34k5_k3y5tr34m_b0fbd4d35f80}` |
| Broken Signature Scheme | [`solve.py`](assets/broken-signature-scheme/solve.py) | [`output.txt`](assets/broken-signature-scheme/output.txt) | `cd docs/assets/broken-signature-scheme && python3 solve.py` | `NXCTF{mult1_l4y3r_l4tt1c3_r54_s1gn4tur3_hnp_8c211ad6b5a6}` |
| Feistel Differential | [`solve.py`](assets/feistel-differential/solve.py), [`cipher.py`](assets/feistel-differential/cipher.py) | [`pairs.txt`](assets/feistel-differential/pairs.txt), [`flag.enc`](assets/feistel-differential/flag.enc) | `cd docs/assets/feistel-differential && python3 solve.py` | `NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}` |
| Matryoshka Encoding | [`solve.py`](assets/matryoshka-encoding/solve.py) | [`capsule.dat`](assets/matryoshka-encoding/capsule.dat) | `cd docs/assets/matryoshka-encoding && python3 solve.py` | `NFXCTF{m4try0shk4_0n10n_p33l3d_c309b71e}` |
| Medium RC4 | [`solve_rc4.py`](assets/medium-rc4/solve_rc4.py) | [`medium_rc4`](assets/medium-rc4/medium_rc4) | `cd docs/assets/medium-rc4 && python3 solve_rc4.py` | `NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}` |
| Medium TEA | [`solve_tea.py`](assets/medium-tea/solve_tea.py) | [`medium_tea`](assets/medium-tea/medium_tea) | `cd docs/assets/medium-tea && python3 solve_tea.py` | `NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}` |
| Hard Feistel | [`solve_feistel.py`](assets/hard-feistel/solve_feistel.py) | [`hard_feistel`](assets/hard-feistel/hard_feistel) | `cd docs/assets/hard-feistel && python3 solve_feistel.py` | `NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}` |
| Hard VM Bytecode | [`solve_vm.py`](assets/hard-vm-bytecode/solve_vm.py) | [`hard_vm`](assets/hard-vm-bytecode/hard_vm) | `cd docs/assets/hard-vm-bytecode && python3 solve_vm.py` | `NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}` |
| Castaway | [`solve_castaway.py`](assets/castaway/solve_castaway.py) | [`castaway`](assets/castaway/castaway) | `cd docs/assets/castaway && python3 solve_castaway.py` | `NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}` |
| Decode Balik | [`solve_decode_balik.py`](assets/decode-balik/solve_decode_balik.py) | [`waifu.png`](assets/decode-balik/waifu.png) | `cd docs/assets/decode-balik && python3 solve_decode_balik.py` | JPEG `10-waifu-decoded.jpg`; flag terlihat di gambar |
| Omah Buffer Kebak | [`solve_omah.py`](assets/omah-buffer-kebak/solve_omah.py) | [`omah`](assets/omah-buffer-kebak/omah), `flag.txt` | `cd docs/assets/omah-buffer-kebak && python3 solve_omah.py` | `FLAG: NFX{OmahhKUuD0Ndoll_Uw0nggG}` |

### Contoh output nyata

```text
$ cd docs/assets/medium-rc4 && python3 solve_rc4.py
[*] binary      : .../docs/assets/medium-rc4/medium_rc4
[*] key (hex)   : 6e30745f7333637572335f6b33795f32303236  (b'n0t_s3cur3_k3y_2026')
[*] plaintext   : b'NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}'
[+] FLAG        : NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}
```

```text
$ cd docs/assets/matryoshka-encoding && python3 solve.py
base85: 0001D8UQ0qdNL|lel;*kdKqX>e|9#0K6PtNeIf@!eRg3(d3QZr
NFXCTF{m4try0shk4_0n10n_p33l3d_c309b71e}
```

## Script pendukung

Beberapa challenge punya script exploit/solver tambahan. Script-nya ada di
folder challenge, tetapi membutuhkan service, binary, atau attachment asli
yang tidak selalu bisa dijalankan ulang setelah event berakhir.

| Challenge | Script | Catatan |
|---|---|---|
| FlagKeepers | `assets/flagkeepers/offline_sim.py`, `exploit_live.py` | Butuh service live untuk oracle; simulasi offline disediakan. |
| Unbreakable Delay | `assets/unbreakable-delay/sim_vdf.py` | Protokol direkonstruksi; service historis sudah tidak aktif. |
| Stay | `assets/stay/solve_stay.py` | Butuh file/input challenge asli. |
| SymHell | `assets/symhell/app.py` | Source service; butuh runtime Python. |
| Pwn 37–42 | `assets/<slug>/exploit.py` | Butuh binary/service; script memakai pwntools. |
| Web 48–51 | `assets/<slug>/exploit_*.py` | Butuh instance web live; sudah tidak aktif setelah event. |
| Dead Drop | `assets/dead-drop/10-git-ls-remote.txt` | Token dari `.git/config`; pakai `git ls-remote` lalu `git fetch --tags` (read-only). Token diredaksi. |

## Attachment & binary

- Binary reverse yang dipakai di solver sudah disalin ke folder challenge:
  `medium_rc4`, `medium_tea`, `hard_feistel`, `hard_vm`, `castaway`.
- Attachment crypto yang dipakai sudah disalin: `output.txt`, `pairs.txt`,
  `flag.enc`, `capsule.dat`.
- Attachment besar/lain (zip Pwn, web source, pcap) mengikuti repo publik
  penyelenggara: <https://github.com/NFCC-Com/qazwsx>.
- Jika file tidak ada di folder challenge, cek halaman **Evidence** challenge
  tersebut; biasanya ada link ke file mentah atau repo publik.

## Troubleshooting

| Masalah | Solusi |
|---|---|
| `ModuleNotFoundError` | Install dependency di bagian Prasyarat. |
| `FileNotFoundError: output.txt` | Jalankan dari folder challenge (`cd docs/assets/<slug>`). |
| Binary tidak executable | `chmod +x <binary>`; pastikan arsitektur x86-64 Linux. |
| Path `<repo>` muncul di command | Ganti dengan path root repo lokal. |
| Service sudah mati | Gunakan output/transkrip arsip di halaman Evidence; service event sudah berakhir. |
