# PageStream — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">7 screenshot</span><span class="nx-chip">6 transkrip / script</span></div>


[← Overview](51-pagestream.md) · [Index](index.md)

> **Langkah 10/11 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](51-pagestream-11-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/pagestream/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/pagestream/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/pagestream/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/term-01-recon.png" target="_blank" rel="noopener"><img src="assets/pagestream/term-01-recon.png" alt="term-01-recon.png" loading="lazy"></a><figcaption>term-01-recon.png</figcaption></figure>
</div>

*Terminal evidence — `01-recon.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/term-02-exploit-run.png" target="_blank" rel="noopener"><img src="assets/pagestream/term-02-exploit-run.png" alt="term-02-exploit-run.png" loading="lazy"></a><figcaption>term-02-exploit-run.png</figcaption></figure>
</div>

*Terminal evidence — `02-exploit-run.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/term-03-write-proof.png" target="_blank" rel="noopener"><img src="assets/pagestream/term-03-write-proof.png" alt="term-03-write-proof.png" loading="lazy"></a><figcaption>term-03-write-proof.png</figcaption></figure>
</div>

*Terminal evidence — `03-write-proof.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/term-04-rce-proof.png" target="_blank" rel="noopener"><img src="assets/pagestream/term-04-rce-proof.png" alt="term-04-rce-proof.png" loading="lazy"></a><figcaption>term-04-rce-proof.png</figcaption></figure>
</div>

*Terminal evidence — `04-rce-proof.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/term-source-notes.png" target="_blank" rel="noopener"><img src="assets/pagestream/term-source-notes.png" alt="term-source-notes.png" loading="lazy"></a><figcaption>term-source-notes.png</figcaption></figure>
</div>

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`01-recon.txt`](assets/pagestream/01-recon.txt)
- [`02-exploit-run.txt`](assets/pagestream/02-exploit-run.txt)
- [`03-write-proof.txt`](assets/pagestream/03-write-proof.txt)
- [`04-rce-proof.txt`](assets/pagestream/04-rce-proof.txt)
- [`exploit_pagestream.py`](assets/pagestream/exploit_pagestream.py)
- [`source-notes.txt`](assets/pagestream/source-notes.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon | `assets/pagestream/01-recon.txt` | `/health`, `/`, `/dashboard` |
| Transcript exploit | `assets/pagestream/02-exploit-run.txt` | Mass assignment, LFI, flag |
| Arbitrary write | `assets/pagestream/03-write-proof.txt` | Upload traversal + readback |
| RCE | `assets/pagestream/04-rce-proof.txt` | `uid=0`, `/readflag`, flag |
| Source snippet | `assets/pagestream/source-notes.txt` | Auth, posts, Dockerfile, helper |
| Exploit | `assets/pagestream/exploit_pagestream.py` | Script lengkap |
| Hash source | lihat §1.2 | SHA-256 `auth.js`, `posts.js` |