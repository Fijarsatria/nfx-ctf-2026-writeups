# Dead Drop — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">4 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>


[← Overview](81-dead-drop.md) · [Index](index.md)

> **Langkah 4/5 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](81-dead-drop-05-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/dead-drop/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/dead-drop/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/dead-drop/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/dead-drop/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/dead-drop/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/dead-drop/term-01-solve.png" target="_blank" rel="noopener"><img src="assets/dead-drop/term-01-solve.png" alt="term-01-solve.png" loading="lazy"></a><figcaption>term-01-solve.png</figcaption></figure>
</div>

*Terminal evidence — `01-solve.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/dead-drop/term-10-git-ls-remote.png" target="_blank" rel="noopener"><img src="assets/dead-drop/term-10-git-ls-remote.png" alt="git ls-remote dan handover" loading="lazy"></a><figcaption>term-10-git-ls-remote.png</figcaption></figure>
</div>

*Terminal evidence — token dari `.git/config` dipakai untuk membaca hidden branch `archive/q3-handover` dan tag `incident-0914`.*

### Transkrip mentah & script

- [`01-solve.txt`](assets/dead-drop/01-solve.txt)
- [`10-git-ls-remote.txt`](assets/dead-drop/10-git-ls-remote.txt)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/dead-drop/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

- Challenge brief: `assets/dead-drop/00-challenge-platform.png`
- Terminal evidence (real): `assets/dead-drop/00b-terminal-evidence.png`
- Catatan mentah: lihat folder `assets/dead-drop/`

## Bukti tambahan (Dead Drop)

![Bukti Dead Drop](assets/dead-drop/10-bukti.png)

*Terminal evidence — config leak dan analisis awal.*

- `.git/config` menyimpan `http.extraheader` berisi token GitHub (disensor di writeup).
- Token masih valid saat snapshot; `git ls-remote` membaca ref tersembunyi
  `refs/heads/archive/q3-handover` dan tag `incident-0914` (commit `67e53bf`).
- `git fetch --tags` lalu `git show incident-0914:notes/handover.txt`
  menampilkan flag.
- Ini melengkapi langkah yang sebelumnya tidak ada di zip: branch tersembunyi
  hanya bisa dibaca lewat token dari config.

**Berkas mentah:** [ANALYSIS.md](assets/dead-drop/10-ANALYSIS.md) ·
[git-config-redacted.txt](assets/dead-drop/10-git-config-redacted.txt) ·
[10-git-ls-remote.txt](assets/dead-drop/10-git-ls-remote.txt) ·
[public-api-404.json](assets/dead-drop/10-public-api-404.json) ·
[org-repos.json](assets/dead-drop/10-org-repos.json)
