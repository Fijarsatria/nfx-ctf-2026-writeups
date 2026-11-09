# LinkVault — Analisis

[← Overview](49-linkvault.md) · [Index](index.md)

## 2.3 Admin bot dan template moderasi

`bot.go`:

```go
if err := chromedp.Run(cctx,
	network.SetCookie("session", adminSID).WithDomain("127.0.0.1").WithPath("/"),
	chromedp.Navigate("http://127.0.0.1:80/moderation"),
	chromedp.Sleep(5*time.Second),
); err != nil { ... }
```

Bot berjalan setiap 25 detik (setelah sleep 15 detik pertama), memakai cookie `adminSID`, dan membuka `/moderation`.

`templates/moderation.html`:

```html
{{range .Items}}
<div class="mb-4 ...">
  <h3 ...>{{.Title}}</h3>
  <div class="text-xs text-gray-500 mb-2">policy precheck</div>
  <script>if (true) { /{{.Filter}}/g.test("x") }</script>
</div>
{{else}}
...
{{end}}
```

`Filter` berada di dalam **regex literal** JavaScript. `html/template` melakukan escaping berdasarkan konteks; bug yang dipakai challenge adalah salah klasifikasi konteks setelah `{` sehingga `/` dan karakter pemecah regex tidak di-escape dengan benar. Payload dapat keluar dari regex dan menjalankan JavaScript biasa.

Catatan penting: escaper JS `html/template` meng-escape `>` menjadi `\u003e` pada konteks nilai JS. Karena itu payload harus menghindari `>` (mis. jangan pakai arrow function `=>`). Payload di bawah memakai `function(r){return r.text()}`.

## 2.4 Alur eksploitasi

1. Penyerang register user biasa.
2. Penyerang submit URL `http://[::1]:8081/internal/import?filter=<payload>`.
3. Server mem-fetch URL tersebut (SSRF), internal API menerima `filter` mentah dan memasukkan item ke queue.
4. Dalam ≤25 detik, bot admin membuka `/moderation`.
5. Browser bot merender `<script>` dengan payload; XSS berjalan sebagai admin di `http://127.0.0.1:80`.
6. Payload memanggil `fetch('/flag')` (cookie admin otomatis dikirim, same-origin), lalu mengirim body flag ke `/api/share?to=<username>&d=<flag>`.
7. `/api/share` menulis ke `inbox[to]`; penyerang membuka `/reports` dan membaca flag.
