# Pipa Nu Kotor — Analisis

[← Overview](39-pipa-nu-kotor.md) · [Index](index.md)

### 2.1 Struct pipa

`op_buka()` mengalokasikan `malloc(0x18)` untuk struct, lalu mengisi:

```asm
1746: mov edi, 0x18
174b: call malloc
...
; mode rw
17b5: mov [rax+0x8], 0x40        # capacity
17c1: mov DWORD PTR [rax+0x10], 0 # readonly = 0
; mode ro
17d2: lea rdx, [rip+0x2907]      # shadow_page
17d9: mov [rax], rdx             # data = shadow_page
17e0: mov QWORD PTR [rax+0x8], 0x40
17e8: mov DWORD PTR [rax+0x10], 1 # readonly = 1
```

Perhatikan: **`+0x14` (flags) tidak pernah di-set saat open**. Layout efektif:

```text
+0x00  char  *data
+0x08  size_t capacity   (0x40)
+0x10  int    readonly    (rw=0, ro=1)
+0x14  int    flags       (tidak diinisialisasi)
```

### 2.2 `op_tulis()` — pengecekan read-only yang bisa dibypass

```asm
19e4: mov rax, [rbp-0x10]        # pipe*
19e8: mov eax, [rax+0x10]        # readonly
19eb: test eax, eax
19ed: je  401a11                 # rw -> langsung tulis
19ef: mov rax, [rbp-0x10]
19f3: mov eax, [rax+0x14]        # flags
19f6: and eax, 0x10
19f9: test eax, eax
19fb: jne 401a11                 # flags & 0x10 -> diizinkan (BUG)
19fd: ... "halaman dilindungi"
```

Jika `readonly == 1` dan `flags & 0x10 == 0`, tulis ditolak. Namun jika `flags` masih bernilai `0x10` dari pemakaian sebelumnya, tulis **diizinkan**.

Setelah `memcpy`, kode melakukan:

```asm
1a47: mov rax, [rbp-0x10]
1a4b: mov eax, [rax+0x14]
1a4e: or  eax, 0x10
1a51: mov edx, eax
1a53: mov rax, [rbp-0x10]
1a57: mov [rax+0x14], edx        # flags |= 0x10
```

Jadi setiap penulisan sukses menyalakan bit `0x10`.

### 2.3 `op_tutup()` — chunk kembali ke tcache

```asm
18a1: mov rax, [rbp-0x10]
18a5: mov eax, [rax+0x10]
18a8: test eax, eax
18aa: jne 18c7                   # ro -> jangan free data
18b8: mov rax, [rbp-0x10]
18bc: mov rax, [rax]
18bf: mov rdi, rax
18c2: call free                  # free(data)
18c7: mov rax, [rbp-0x10]
18ce: call free                  # free(struct)
```

Saat `free(struct)` pada chunk `0x20`, glibc menulis `tcache->next` di offset 0 dan `tcache key` di offset 8. Offset `0x10` dan `0x14` **tidak disentuh**, sehingga `readonly` dan `flags` tetap.

### 2.4 Reuse tcache

Urutan yang dipakai:

1. Buka pipa `rw` → `malloc(0x18)` mengambil chunk dari tcache/top.
2. Tulis sekali → `flags = 0x10`.
3. Tutup → `free(data)` lalu `free(struct)`; chunk struct masuk tcache `0x20` (LIFO).
4. Buka pipa `ro` → `malloc(0x18)` mengembalikan chunk yang sama. `op_buka` menulis `data = shadow_page`, `capacity = 0x40`, `readonly = 1`, tetapi **tidak menimpa `flags`** → `flags` tetap `0x10`.
5. `op_tulis` melihat `readonly=1` tapi `flags & 0x10 != 0` → lolos, lalu `memcpy(shadow_page, input, len)`.

### 2.5 `shadow_page` dan login

`isi_shadow()` (dipanggil dari `main`) mengisi `shadow_page` dengan password acak berformat `$6$%02x...$` dari `/dev/urandom` (atau `ZZZZZZZZ` jika gagal). `op_login()` membandingkan input dengan `shadow_page`:

```asm
1b79: lea rdx, [rip+0x2560]      # shadow_page
1b8d: call strcmp
1b94: jne  login gagal
1b96: ... "login sebagai root"
1ba5: call cetak_flag
```

`cetak_flag()` membuka `flag.txt`, membaca dengan `fgets`, dan `printf("FLAG: %s")`.
