# PageStream — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">1 screenshot</span><span class="nx-chip">6 transkrip / script</span></div>


[← Overview](51-pagestream.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/pagestream/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/pagestream/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/pagestream/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

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