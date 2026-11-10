# PageStream — Upload filename traversal

[← Overview](51-pagestream.md) · [Index](index.md)

> **Langkah 5/11 — Upload filename traversal.** Upload filename traversal
>
> **Titik penting:** NFX{dummy_flag_for_local_testing}
>
> **Berikutnya:** [Analisis](51-pagestream-06-analisis.md)

## 2.3 Upload filename traversal

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

### Evidence langkah ini

![term-source-notes.png](assets/pagestream/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`source-notes.txt`](assets/pagestream/source-notes.txt)
