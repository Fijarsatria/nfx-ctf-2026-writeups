# Commit yang kehapus — Jejak awal

[← Overview](84-commit-yang-kehapus.md) · [Index](index.md)

> **Langkah 1/5.** Commit `a9e13b2` menghapus key. Blob `21d5a194` masih dangling.
>
> **Berikutnya:** [Cara Mendapatkan Flag](84-commit-yang-kehapus-02-cara-mendapatkan-flag.md)

```bash
tar -xzf shadow_repo.tar.gz
cd shadow_repo
git log --oneline --all
git show 706f270:.env.staging
git fsck --lost-found
```

```text
706f270 Initial staging configuration
a9e13b2 Remove sensitive staging key before public release
dangling blob 21d5a194fb6a627b1702cbf74b51589789988b72
AWS_ACCESS_KEY_ID=AKIA-NFX-99204811
```

Author kedua commit: `k.vance@ops-shadow-nfx.internal`.
