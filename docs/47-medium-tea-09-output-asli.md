# Medium TEA — Output asli

[← Overview](47-medium-tea.md) · [Index](index.md)

## 3.3 Output asli

```text
$ python3 writeups/assets/medium-tea/solve_tea.py
[*] binary     : /home/bocil/ctf/nfx/reverse/Medium_02_TEA/medium_tea
[*] ciphertext : d08b910e9e3d818eeadab483cfc8fd8a083b44836a130476724d7205905af697db1395e7c74c5385
[*] key words  : 0x1337beef 0xcafebabe 0xdeadc0de 0x0badf00d
[*] delta      : 0x9e3779b9; sum akhir = 0xc6ef3720
[*] blok @00: 0e918bd0 8e813d9e -> 7b58464e 796e3174 ('NFX{t1ny')
[*] blok @08: 83b4daea 8afdc8cf -> 636e335f 74707972 ('_3ncrypt')
[*] blok @16: 83443b08 7604136a -> 5f6e3031 30676c34 ('10n_4lg0')
[*] blok @24: 05724d72 97f65a90 -> 68743172 32335f6d ('r1thm_32')
[*] blok @32: e79513db 85534cc7 -> 7530725f 7d35646e ('_r0und5}')
[*] enkripsi ulang == ciphertext: True
[+] FLAG       : NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}
[*] verifikasi : stdout='Correct! TEA terpecahkan.' rc=0
```

Perhatikan bahwa hasil dekripsi per blok membentuk teks yang dapat dibaca, dan enkripsi ulang menghasilkan ciphertext identik. Ini memastikan implementasi inverse sudah benar, bukan sekadar kebetulan.
