# The Ghost Operator — Eksploitasi / Solver

[← Overview](35-the-ghost-operator.md) · [Index](index.md)

### 3.1 Strategi

1. Ekstrak zip, baca commit dan tanda tangan GPG.
2. Ambil public key dari keyserver, baca UID.
3. Enumerasi semua key dengan domain yang sama.
4. Buka URL telegra.ph/rentry (langsung atau via Wayback).
5. Identifikasi tempat dari empat elemen petunjuk.
6. Susun flag sesuai format; uji varian case/ejaan jika lowercase ditolak.

### 3.2 Perintah verifikasi

```bash
# 1. Ekstrak dan verifikasi commit
unzip -q investigation.zip -d investigation
cd investigation/investigation
git log --show-signature -1

# 2. Ambil key dari keyserver
gpg --keyserver keyserver.ubuntu.com --recv-keys E6BE71CA2BD84A4E

# 3. Enumerasi key satu domain
curl -s 'https://keyserver.ubuntu.com/pks/lookup?op=index&search=veloxphantom.net&options=mr'

# 4. Baca field notes
curl -s 'https://api.telegra.ph/getPage/Field-Notes-0914-Escape-Route-10-25?return_content=true'
curl -sL 'https://web.archive.org/web/20261025190602id_/https://rentry.co/ghost-route-0914'
```

### 3.3 Output asli

```text
gpg: Signature made Mon Oct 26 01:49:05 2026 WIB
gpg:                using RSA key B17171D40DE252F193E79707E6BE71CA2BD84A4E
gpg: Good signature from "Dimas Wirawan
     (rentry.co/ghost-route-0914)
     <ghost.operator.rentry@veloxphantom.net>" [unknown]

keyserver index:
pub:A0BE3884C3DA0ED27A6D627338353AD29DC58103:1:4096:1792953553::
uid:Dimas Wirawan (telegra.ph/Field-Notes-0914-Escape-Route-10-25-2) ...
pub:BE7BB77BC5DC29E31149C1F9C92E23B3427F0BBC:1:4096:1792953278::
uid:Dimas Wirawan (telegra.ph/Field-Notes-0914-Escape-Route-10-25) ...
pub:B17171D40DE252F193E79707E6BE71CA2BD84A4E:1:4096:1792954100::
uid:Dimas Wirawan (rentry.co/ghost-route-0914) ...
```
