# Starved — Analisis

[← Overview](40-starved.md) · [Index](index.md)

## 2.3 Seccomp — `read` hanya fd 0

`setup_seccomp()` memakai `seccomp_init(KILL)` lalu `seccomp_rule_add()` untuk:

```text
write=1, open=2, openat=0x101, pread64=0x11, close=3, lseek=8,
fstat=5, newfstatat=0x106, brk=0xc, exit=0x3c, exit_group=0xe7
read=0 dengan arg0 == 0 (SCMP_CMP_EQ)
```

Detail decode ada di `writeups/assets/starved/02b-seccomp.txt`. Konsekuensinya:

- `execve` diblokir → tidak bisa `system("/bin/sh")`.
- `read(3, ...)` diblokir karena arg0 ≠ 0.
- Tetapi `close(0)` lalu `open("flag.txt")` mengembalikan **fd 0**, sehingga `read(0, buf, n)` diizinkan.

## 2.4 Offset libc/gadget (libc 2.35 bawaan)

| Item | Offset |
|---|---|
| `main` return → libc | `0x29d90` |
| `close` | `0x1150a0` |
| `open` | `0x114630` |
| `read` | `0x114920` |
| `write` | `0x1149c0` |
| `exit` | `0x455f0` |
| `pop rdi ; ret` | `0x2a3e5` |
| `pop rsi ; ret` | `0x2be51` |
| `pop rdx ; pop rbx ; ret` | `0x90469` |
| `ret` | `0x29cd6` |
