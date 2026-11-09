# LinkVault — Analisis

[← Overview](49-linkvault.md) · [Index](index.md)

### 2.1 SSRF guard dan bypass IPv6 loopback

`handlers.go`:

```go
var blockedHosts = map[string]bool{
	"admin.internal": true,
	"localhost":      true,
	"127.0.0.1":      true,
}

func guardedFetch(rawURL string) (string, error) {
	u, err := url.Parse(rawURL)
	if err != nil {
		return "", errors.New("invalid url")
	}
	if u.Scheme != "http" && u.Scheme != "https" {
		return "", errors.New("unsupported scheme")
	}
	host := strings.ToLower(u.Hostname())
	if blockedHosts[host] {
		return "", errors.New("host is not allowed")
	}
	pretty, _ := idna.ToUnicode(host)
	port := u.Port()
	if port != "" {
		u.Host = net.JoinHostPort(pretty, port)
	} else {
		u.Host = pretty
	}
	resp, err := httpClient.Get(u.String())
	...
}
```

Masalah:
1. Denylist hanya tiga host literal. Tidak ada pemeriksaan `net.IP.IsLoopback()`, `IsPrivate()`, `IsLinkLocalUnicast()`, atau resolusi DNS.
2. `u.Hostname()` untuk `http://[::1]:8081/...` menghasilkan `::1`; `== "127.0.0.1"` tidak cocok.
3. `internal.go` justru mendengarkan di dua alamat loopback:

```go
log.Println("[linkvault] internal crawler API on 127.0.0.1:8081")
go http.ListenAndServe("127.0.0.1:8081", mux)
log.Println("[linkvault] internal crawler API on [::1]:8081")
log.Fatal(http.ListenAndServe("[::1]:8081", mux))
```

Jadi `http://[::1]:8081/internal/import?...` melewati denylist dan mencapai API internal.

### 2.2 Internal import tidak memvalidasi `filter`

`internal.go`:

```go
mux.HandleFunc("/internal/import", func(w http.ResponseWriter, r *http.Request) {
	ip, _, err := net.SplitHostPort(r.RemoteAddr)
	if err != nil || (ip != "127.0.0.1" && ip != "::1") {
		http.Error(w, "denied", http.StatusForbidden)
		return
	}
	filter := r.URL.Query().Get("filter")
	title := r.URL.Query().Get("title")
	if filter == "" {
		http.Error(w, `{"err":"filter required"}`, http.StatusBadRequest)
		return
	}
	internalAddItem(title, filter)
	...
})
```

- Pemeriksaan `RemoteAddr` lolos karena request datang dari loopback (SSRF dari proses yang sama).
- `filter` langsung diteruskan ke `internalAddItem` tanpa `safeFilter.MatchString(filter)`.
- Route publik `/submit` **memang** memvalidasi filter dengan `safeFilter`:

```go
var safeFilter = regexp.MustCompile(`^[a-zA-Z0-9 ._\-*+]{0,64}$`)
```

tetapi validasi itu tidak berlaku di jalur internal.

`internalAddItem` menyimpan item ke queue:

```go
func internalAddItem(title, filter string) {
	queueMu.Lock()
	queue = append(queue, &LinkItem{
		ID:        nextScanID(),
		Title:     title,
		URL:       "internal://crawler/sync",
		Preview:   `{"ok":true,"queued":true,"source":"crawler"}`,
		Filter:    filter,
		Status:    "Pending",
		Owner:     "crawler",
		...
	})
	queueMu.Unlock()
}
```

### 2.3 Admin bot dan template moderasi

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

### 2.4 Alur eksploitasi

1. Penyerang register user biasa.
2. Penyerang submit URL `http://[::1]:8081/internal/import?filter=<payload>`.
3. Server mem-fetch URL tersebut (SSRF), internal API menerima `filter` mentah dan memasukkan item ke queue.
4. Dalam ≤25 detik, bot admin membuka `/moderation`.
5. Browser bot merender `<script>` dengan payload; XSS berjalan sebagai admin di `http://127.0.0.1:80`.
6. Payload memanggil `fetch('/flag')` (cookie admin otomatis dikirim, same-origin), lalu mengirim body flag ke `/api/share?to=<username>&d=<flag>`.
7. `/api/share` menulis ke `inbox[to]`; penyerang membuka `/reports` dan membaca flag.
