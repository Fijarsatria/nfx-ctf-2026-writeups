# PageStream — Path traversal di `/view`

[← Overview](51-pagestream.md) · [Index](index.md)

> **Langkah 4/11 — Path traversal di `/view`.** Path traversal di `/view`
>
> **Titik penting:** —
>
> **Berikutnya:** [Upload filename traversal](51-pagestream-05-upload-filename-traversal.md)

## 2.2 Path traversal di `/view`

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

### Evidence langkah ini

![term-source-notes.png](assets/pagestream/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`source-notes.txt`](assets/pagestream/source-notes.txt)
