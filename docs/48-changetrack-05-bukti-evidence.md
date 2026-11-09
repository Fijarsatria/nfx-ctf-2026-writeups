# ChangeTrack — Evidence / Bukti

[← Overview](48-changetrack.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/changetrack/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Transkrip / file pendukung

- [`01-recon.txt`](assets/changetrack/01-recon.txt)
- [`02-dashboard-pages.txt`](assets/changetrack/02-dashboard-pages.txt)
- [`03-benign-save.txt`](assets/changetrack/03-benign-save.txt)
- [`04-test-benign.txt`](assets/changetrack/04-test-benign.txt)
- [`05-ssti-run.txt`](assets/changetrack/05-ssti-run.txt)
- [`06-enum-run.txt`](assets/changetrack/06-enum-run.txt)
- [`07-enum2-run.txt`](assets/changetrack/07-enum2-run.txt)
- [`08-dynamic-target.txt`](assets/changetrack/08-dynamic-target.txt)
- [`09-enum3-run.txt`](assets/changetrack/09-enum3-run.txt)
- [`10-enum4-run.txt`](assets/changetrack/10-enum4-run.txt)
- [`11-enum5-run.txt`](assets/changetrack/11-enum5-run.txt)
- [`12-enum6-run.txt`](assets/changetrack/12-enum6-run.txt)
- [`13-enum-cmds.txt`](assets/changetrack/13-enum-cmds.txt)
- [`14-flag-capture.txt`](assets/changetrack/14-flag-capture.txt)
- [`exploit_changetrack.py`](assets/changetrack/exploit_changetrack.py)
- [`oob-capture.log`](assets/changetrack/oob-capture.log)
- [`oob-server.out`](assets/changetrack/oob-server.out)
- [`oob_server.py`](assets/changetrack/oob_server.py)
- [`wh_requests.json`](assets/changetrack/wh_requests.json)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon | `assets/changetrack/01-recon.txt` | `/`, `/login` |
| Halaman watcher | `assets/changetrack/02-dashboard-pages.txt` | Dashboard, manifest, edit/test |
| Save benign | `assets/changetrack/03-benign-save.txt` | Manifest `{{ 7*7 }}` |
| Test benign | `assets/changetrack/04-test-benign.txt` | `POST /test` |
| SSTI proof | `assets/changetrack/05-ssti-run.txt` | `{{ 7*7 }}` → `49` |
| Enumerasi | `assets/changetrack/13-enum-cmds.txt` | `cat /flag.txt` → flag |
| Capture flag | `assets/changetrack/14-flag-capture.txt` | JSON webhook.site |
| OOB server (opsional) | `assets/changetrack/oob_server.py` | Sink lokal untuk uji konektivitas |
| Exploit | `assets/changetrack/exploit_changetrack.py` | Script lengkap |
