# Left Behind in the Metadata — Cara mendapatkan flag

[← Overview](86-left-behind-in-the-metadata.md) · [Index](index.md)

> **Langkah 2/5.** Key lima field. Konstruksi cipher sama dengan Commit yang kehapus.
>
> **Berikutnya:** [Flag](86-left-behind-in-the-metadata-03-flag.md)

```python
import hashlib
ct = bytes.fromhex("98e8be19a5ebb50b8d0ed72cadf4801a01753252bbf0d97d0cc0a76145185f9096be3f15df61ae22")
ks = "NFX-Imaging-Corp|FieldCam-X9|@nfx_courier_07|NFX-SN-8842109|-6.1753,106.8269"
k = hashlib.sha256(ks.encode()).digest()
stream = b"".join(hashlib.sha256(k + i.to_bytes(4, "big")).digest() for i in range(2))
print(bytes(a ^ b for a, b in zip(ct, stream)).decode())
```

```text
NFXCTF{3x1f_gp5_m3t4_tr4c3_9f41c8b2e70d}
```

Urutan field dan format GPS (`-6.1753,106.8269`, tanpa spasi) harus persis. Hasil dekripsi berawalan `NFXCTF`, bukan `NFX`.

### Evidence langkah ini

![00b-terminal-evidence.png](assets/left-behind-in-the-metadata/00b-terminal-evidence.png)

*Terminal evidence (arsip/log asli) — `00b-terminal-evidence.png`.*

**Berkas mentah terkait:**

- [`01-solve.txt`](assets/left-behind-in-the-metadata/01-solve.txt)
