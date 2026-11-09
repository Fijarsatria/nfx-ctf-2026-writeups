# Bluebird Session — Analisis

[← Overview](25-bluebird-session.md) · [Index](index.md)

### 2.1 Identitas dua user

| User | UID | Peran | Petunjuk |
|---|---:|---|---|
| `mizore` | 1001 | “Liz” | keyring, `Ensemble.mp4`, history `secret-tool` |
| `nozomi` | 1002 | “blue bird” | `for_nozomi.zip`, history `7z a -p...` |
| `aria` | 1000 | user lama/default | tidak dipakai dalam alur flag |

`/etc/shadow`:

```text
mizore:$6$bluebird$DapjL6a0nzC4W7lGKYhAtHOEPMW06uuQOg4DiPxOWF3RKE6RRSKIumUGXj3QmER5G4ceko4QUsikFswkW330E1:20684:0:99999:7:::
nozomi:$y$j9T$DhVH4WQyNgEFCqIkUphFf1$q0BKoCWrbVK2X0hcG6HzpOhEua2qY2sATukNgvlK/C5:20684:0:99999:7:::
```

- `mizore`: SHA-512 crypt (`$6$`) dengan salt `bluebird`.
- `nozomi`: yescrypt (`$y$`).

Verifikasi password mizore:

```python
import crypt
h = '$6$bluebird$DapjL6a0nzC4W7lGKYhAtHOEPMW06uuQOg4DiPxOWF3RKE6RRSKIumUGXj3QmER5G4ceko4QUsikFswkW330E1'
for p in ['Bluebirds1927!', 'MizoreCanFly2077!@', 'bluebird', 'mizore']:
    print(p, crypt.crypt(p, h) == h)
```

Output:

```text
Bluebirds1927! True
MizoreCanFly2077!@ False
bluebird False
mizore False
```

Password login mizore: **`Bluebirds1927!`**.

### 2.2 Bash history

`mizore/.bash_history`:

```bash
whoami
id
ls -la /home/nozomi/Documents
secret-tool store --label="Mizore Promise Note" app bluebird target for_nozomi_note
secret-tool lookup app bluebird target for_nozomi_note
ls -la /home/nozomi/Documents/for_nozomi_content
pwd
ip addr
```

`nozomi/.bash_history`:

```bash
sudo bash -c 'cat > /home/nozomi/Documents/for_nozomi_content/README.txt' << 'EOF'
These memories were never meant to disappear.

Look through the performance, the pictures, and the sound that remains.
EOF
...
7z a -tzip ../for_nozomi.zip . -p'MizoreCanFly2077!@'
sudo chown nozomi:nozomi /home/nozomi/Documents/for_nozomi.zip
...
```

`root/.bash_history`:

```bash
cd /home/nozomi/
cd Documents/
ls
mv Ensemble.mp4 /home/mizore/Documents/
sudo chown -R mizore:mizore /home/mizore/Documents/Ensemble.mp4
...
rm -rf for_nozomi
rm -rf for_nozomi_content/
```

Root memindahkan `Ensemble.mp4` ke home mizore dan menghapus direktori kerja `for_nozomi_content`, tetapi ZIP sudah dibuat dan tertinggal.

### 2.3 GNOME Keyring `login.keyring`

Header:

```text
00000000: 476e 6f6d 654b 6579 7269 6e67 0a0d 000a  GnomeKeyring....
00000010: 0000 0000 0000 0005 4c6f 6769 6e00 0000  ........Login...
...
00000030: 0000 0000 0000 000d 5d87 1fa3 0523 eb6c  ........]....#.l
```

Parse:

```text
magic          : GnomeKeyring
version/crypto : 0.0 / crypto=0 (AES) / hash=0 (MD5)
keyring name   : Login
iterations     : 3421
salt           : 871fa30523eb6c6b
num_items      : 1

PLAINTEXT ITEM HEADER:
  id=1 type=0
    app        type=0 value=b'b30d2f4bbe6cbefbc0ab619d9af8b316'
    target     type=0 value=b'419727a1b15144e4e6b35d1e80f348ce'
```

Atribut adalah MD5 dari nilai:

```text
MD5('bluebird')        = b30d2f4bbe6cbefbc0ab619d9af8b316
MD5('for_nozomi_note') = 419727a1b15144e4e6b35d1e80f348ce
```

KDF GNOME Keyring lama:

```text
digest = SHA256(password || salt)
ulangi SHA256(digest) sebanyak iterations-1
key = digest[0:16], iv = digest[16:32]
AES-128-CBC decrypt ciphertext
```

Dengan password `Bluebirds1927!`:

```text
verify MD5     : 8b7b9e237395fb8d94877330300e1b3c == 8b7b9e237395fb8d94877330300e1b3c ? True

display_name   : Mizore Promise Note
secret         :
For Nozomi,

I promised I would keep playing, even if the sound could no longer reach you.
Every note we left behind still belongs to the same sky.

The archive is for you.
for_nozomi.zip password: MizoreCanFly2077!@
```

### 2.4 Membuka `for_nozomi.zip`

```bash
$ 7z x -y -p'MizoreCanFly2077!@' for_nozomi.zip
...
Everything is Ok

Files: 6
Size:       556921
Compressed: 554674
```

Isi:

```text
323411127236637529.jpg
423261422632617826.jpg
534380312034824810.jpg
674625219173977142.jpg
723461127636657826.jpg
README.txt
```

`README.txt`:

```text
These memories were never meant to disappear.

Look through the performance, the pictures, and the sound that remains.
```

Petunjuk: “performance, pictures, sound” — `Ensemble.mp4` adalah performance/audio, tetapi gambar juga memuat pesan. Pemeriksaan metadata/strings pada `Ensemble.mp4` tidak menghasilkan tambahan yang diperlukan untuk flag; jalur utama adalah gambar.

### 2.5 Gambar dengan flag

`423261422632617826.jpg` adalah JPEG 736×899. Bagian atas gambar memuat overlay teks:

```text
{3220D64291CDFA4B
26844C90690E8F1D}
```

Penggabungan:

```text
3220D64291CDFA4B + 26844C90690E8F1D
= 3220D64291CDFA4B26844C90690E8F1D
```

32 hex, 4 grup 8:

```text
3220D642  91CDFA4B  26844C90  690E8F1D
```
