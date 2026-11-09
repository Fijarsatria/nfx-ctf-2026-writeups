# Record Keeper (User) — Setelah RCE

[← Overview](17-record-keeper-user.md) · [Index](index.md)

## 2.5 Setelah RCE

Shell berjalan sebagai `node`. File flag:

```text
/home/node/user.txt
size   : 37 bytes
mode   : 0400
owner  : node
```

Hanya ada satu user flag dan satu root flag di target:

```text
/home/node/user.txt
/root/root.txt
```

Tidak diperlukan privesc untuk challenge User: begitu RCE sebagai `node`
didapat, `/home/node/user.txt` bisa dibaca langsung (mode 0400, owner `node`).
Privesc ke root adalah challenge terpisah (`record-keeper-root.md`).
