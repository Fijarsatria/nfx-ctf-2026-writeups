# Career Tempat Belajar — Eksploitasi / Solver

[← Overview](09-career-tempat-belajar.md) · [Index](index.md)

### 3.1 Strategi

1. Baca metadata PNG untuk mendapatkan nama perusahaan (“Dih Office”).
2. Cari “Digital Hour Learning” / “Dihlearn” di media sosial.
3. Temukan email rekrutmen dari post karier.
4. Ubah email menjadi MD5, buka profil Gravatar.
5. Baca flag di `aboutMe`.

### 3.2 Script verifikasi

```python
#!/usr/bin/env python3
# verifikasi hash -> profil Gravatar
import hashlib, json, urllib.request

email = "dihlearn.id@gmail.com"
h = hashlib.md5(email.strip().lower().encode()).hexdigest()
print("email:", email)
print("md5  :", h)

req = urllib.request.Request(
    f"https://gravatar.com/{h}.json",
    headers={"User-Agent": "Mozilla/5.0"},
)
data = json.load(urllib.request.urlopen(req, timeout=30))
profile = data["entry"][0]
print("displayName:", profile.get("displayName"))
print("company    :", profile.get("company"))
print("aboutMe    :", profile.get("aboutMe"))
```

### 3.3 Output asli

```text
$ python3 gravatar_check.py
email: dihlearn.id@gmail.com
md5  : 7149a84591149f4933058779e485a3c9
displayName: Dihlearn.id
company    : Digital Hour Learning
aboutMe    : NFX{Gr4v4t4r_0s1nt_R3cru1t3r_D1hL34Rn}
```
