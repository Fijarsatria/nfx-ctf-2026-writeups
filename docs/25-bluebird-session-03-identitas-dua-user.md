# Bluebird Session — Identitas dua user

[← Overview](25-bluebird-session.md) · [Index](index.md)

## 2.1 Identitas dua user

| User | UID | Peran | Petunjuk |
|---|---:|---|---|
| `mizore` | 1001 | “Liz” | keyring, `Ensemble.mp4`, history `secret-tool` |
| `nozomi` | 1002 | “blue bird” | `for_nozomi.zip`, history `7z a -p...` |
| `aria` | 1000 | user lama/default | tidak dipakai dalam alur flag |

`/etc/shadow`:

```text
mizore:$6$bluebird$DapjL6a0nzC4W7lGKYhAtHOEPMW06uuQOg4DiPxOWF3RKE6RRSKIumUGXj3QmER5G4ceko4QUsikFswkW330E1:20684:0:99999:7:::
nozomi:$y$j9T$DhVH4WQyNgEFCqIkUphFf1$q0BKoCWrbVK2X0hcG6HzpOhEua2qY2sATukNgvlK/C5:20684:0:99999:7:::
```

- `mizore`: SHA-512 crypt (`$6$`) dengan salt `bluebird`.
- `nozomi`: yescrypt (`$y$`).

Verifikasi password mizore:

```python
import crypt
h = '$6$bluebird$DapjL6a0nzC4W7lGKYhAtHOEPMW06uuQOg4DiPxOWF3RKE6RRSKIumUGXj3QmER5G4ceko4QUsikFswkW330E1'
for p in ['Bluebirds1927!', 'MizoreCanFly2077!@', 'bluebird', 'mizore']:
    print(p, crypt.crypt(p, h) == h)
```

Output:

```text
Bluebirds1927! True
MizoreCanFly2077!@ False
bluebird False
mizore False
```

Password login mizore: **`Bluebirds1927!`**.
