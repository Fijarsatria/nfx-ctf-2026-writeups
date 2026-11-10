# LinkVault — Internal import tidak memvalidasi `filter`

[← Overview](49-linkvault.md) · [Index](index.md)

## 2.2 Internal import tidak memvalidasi `filter`

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

### Evidence langkah ini

![term-source-notes.png](assets/linkvault/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`source-notes.txt`](assets/linkvault/source-notes.txt)
