# LinkVault — SSRF guard dan bypass IPv6 loopback

[← Overview](49-linkvault.md) · [Index](index.md)

> **Langkah 4/12 — SSRF guard dan bypass IPv6 loopback.** Jadi http://[::1]:8081/internal/import?...
>
> **Titik penting:** http://[::1 · 127.0.0.1 · 127.0.0.1:8081
>
> **Berikutnya:** [Internal import tidak memvalidasi `filter`](49-linkvault-05-internal-import-tidak-memvalidasi-filter.md)

## 2.1 SSRF guard dan bypass IPv6 loopback

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

### Evidence langkah ini

![term-source-notes.png](assets/linkvault/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`source-notes.txt`](assets/linkvault/source-notes.txt)
