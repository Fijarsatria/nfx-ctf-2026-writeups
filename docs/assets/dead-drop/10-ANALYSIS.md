# Dead Drop — analisis branch tersembunyi (2026-11-13)

## Yang ada di attachment

`infra-runbooks.zip` berisi repo Git dengan satu branch lokal/remote: `main`.

```text
$ git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main

$ git fsck --full --unreachable --no-reflogs
(kosong)
```

Semua blob di object store dipindai; tidak ada string `NFX{...}`,
`NXCTF{...}`, atau `NFXCTF{...}`.

## Kebocoran di `.git/config`

```text
[http "https://github.com/"]
    extraheader = AUTHORIZATION: basic <base64>
```

Base64 itu decode ke:

```text
x-access-token:github_pat_11BX4...<disensor>...N29Z
```

Token lengkap ada di attachment. **Jangan dipakai di luar challenge.**
Halaman ini sengaja tidak menyalin token penuh.

## Remote tidak bisa diverifikasi publik

```text
GET https://api.github.com/repos/netmetrics-net/infra-runbooks
404 Not Found
```

Daftar repo organisasi `netmetrics-net` hanya berisi
`c2-deploy-pipeline`. Tidak ada `infra-runbooks` publik.

Artinya:

- Branch tersembunyi **tidak ada di dalam zip**.
- Remote repo tidak bisa diakses tanpa token.
- Menggunakan token yang bocor untuk membuka repo private adalah tindakan
  yang tidak dilakukan dalam audit ini.

## Status bukti

| Bagian | Status |
|---|---|
| Kebocoran `http.extraheader` di `.git/config` | **terbukti** |
| Token GitHub di attachment | **ada** (disensor di sini) |
| Branch tersembunyi | **tidak terbukti**; remote 404 publik |
| Flag `NFX{g1t_c0nf1g_h34d3r_l34k_h1dd3n_br4nch_9c1e7a}` | accepted di platform |

Halaman writeup harus tetap menulis bahwa langkah branch remote **belum
diarsipkan**, bukan seolah branch itu ada di zip.
