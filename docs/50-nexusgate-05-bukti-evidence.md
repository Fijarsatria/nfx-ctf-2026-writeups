# NexusGate — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">2 screenshot</span><span class="nx-chip">9 transkrip / script</span></div>


[← Overview](50-nexusgate.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/nexusgate/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/nexusgate/01-cached-ticket.png" target="_blank" rel="noopener"><img src="assets/nexusgate/01-cached-ticket.png" alt="01-cached-ticket.png" loading="lazy"></a><figcaption>01-cached-ticket.png</figcaption></figure>
<figure><a href="assets/nexusgate/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/nexusgate/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`01-recon-acl.txt`](assets/nexusgate/01-recon-acl.txt)
- [`02-acl-bypass.txt`](assets/nexusgate/02-acl-bypass.txt)
- [`03-exploit-run.txt`](assets/nexusgate/03-exploit-run.txt)
- [`04-ticket-attempt.txt`](assets/nexusgate/04-ticket-attempt.txt)
- [`04b-sandbox-probe.txt`](assets/nexusgate/04b-sandbox-probe.txt)
- [`04c-node-local-repro.txt`](assets/nexusgate/04c-node-local-repro.txt)
- [`05-cached-ticket.html`](assets/nexusgate/05-cached-ticket.html)
- [`exploit_nexusgate.py`](assets/nexusgate/exploit_nexusgate.py)
- [`source-notes.txt`](assets/nexusgate/source-notes.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon + ACL 403 | `assets/nexusgate/01-recon-acl.txt` | `/`, `/health`, `/internal` 403 |
| ACL bypass | `assets/nexusgate/02-acl-bypass.txt` | `/./internal/...` + raw socket |
| Transcript exploit | `assets/nexusgate/03-exploit-run.txt` | Token, nonce, ticket, flag |
| Probe permission tree | `assets/nexusgate/04b-sandbox-probe.txt` | `/app/data/bot` vs sibling paths |
| Local Node repro | `assets/nexusgate/04c-node-local-repro.txt` | Node 24.14.0 permission tree |
| Cached ticket HTML | `assets/nexusgate/05-cached-ticket.html` | `<meta name="nx-ticket">` |
| Screenshot | `assets/nexusgate/01-cached-ticket.png` | Halaman admin “Service Access Tickets” dari cache |
| Source snippet | `assets/nexusgate/source-notes.txt` | Proxy ACL, cursor, permission, cache |
| Exploit | `assets/nexusgate/exploit_nexusgate.py` | Script lengkap |
| Hash source | lihat §1.2 | SHA-256 `proxy.js`, `routes.js` |