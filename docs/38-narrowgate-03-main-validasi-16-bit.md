# NarrowGate — `main()` — validasi 16-bit

[← Overview](38-narrowgate.md) · [Index](index.md)

## 2.2 `main()` — validasi 16-bit

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
