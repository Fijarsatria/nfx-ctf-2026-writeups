# THE FORGOTTEN STATE — Catatan jalur UAF

[← Overview](42-the-forgotten-state.md) · [Index](index.md)

## 3.4 Catatan jalur UAF

Selain overflow di atas, binary ini juga meninggalkan **dangling pointer** (`table[idx]` tidak di-null-kan) dan `view`/`edit` tidak memeriksa `active[idx]`. Jalur alternatif yang mungkin adalah membuat ulang chunk record yang sudah di-free dengan data yang dikendalikan (mis. memanfaatkan tcache `0x30`), lalu memakai `view`/`edit` pada indeks lama untuk arbitrary read/write. Writeup ini memakai jalur overflow karena itulah yang diuji dan menghasilkan shell pada binary `state` yang disediakan; jalur UAF didokumentasikan sebagai akar masalah tambahan.
