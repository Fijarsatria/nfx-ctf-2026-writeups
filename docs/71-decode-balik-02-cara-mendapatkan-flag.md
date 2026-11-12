# Decode Balik — Cara Mendapatkan Flag

[← Overview](71-decode-balik.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.**
>
> **Flag:** `NFX{CuM4_D3c0D3_B4L!k_Aj4_H4Ru5Ny4_G4mP4nG}`
> **Status:** `VERIFIED`

## Recipe asli

`challenge.json` menyimpan recipe sebagai **link**, bukan file:

```text
https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')Zlib_Deflate('Dynamic%20Huffman%20Coding')To_Base64('A-Za-z0-9%2B/%3D')Generate_Image('Greyscale',1,780)&input=TkZYe1JFREVDVEVEfQ
```

Urutan operasi encoding:

1. `To Base64` (`A-Za-z0-9+/=`)
2. `Zlib Deflate` (`Dynamic Huffman Coding`)
3. `To Base64` (`A-Za-z0-9+/=`)
4. `Generate Image` (`Greyscale`, width 1, height 780)

Input awal: `TkZYe1JFREVDVEVEfQ` → `NFX{REDECTED}` (decoy/placeholder).

## Catatan penting

File `recipe` yang diunduh dari platform hanyalah **halaman aplikasi CyberChef**
(75 KB), bukan recipe-nya. Recipe asli harus diambil dari link di atas.

## Reverse

Untuk membalik:

1. `From Base64`
2. `Zlib Inflate`
3. `From Base64`
4. Bandingkan hasil dengan input/decoy.

Flag challenge yang accepted:

```text
NFX{CuM4_D3c0D3_B4L!k_Aj4_H4Ru5Ny4_G4mP4nG}
```

## Bukti submit

Gunakan log API asli:

```json
{"name":"decode_balik","flag":"NFX{CuM4_D3c0D3_B4L!k_Aj4_H4Ru5Ny4_G4mP4nG}","result":{"success":true,"message":"Correct, but already solved."}}
```
