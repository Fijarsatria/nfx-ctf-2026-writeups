# The Alchemist's Sandbox — Flag & Verifikasi

[← Overview](32-the-alchemists-sandbox.md) · [Index](index.md)

> **Flag:** `NFXCTF{pyj41l_4st_4lch3my_vm_pwn_d84f216a}`
> **Status:** `VERIFIED`

```text
NFXCTF{pyj41l_4st_4lch3my_vm_pwn_d84f216a}
```

Verifikasi:

- Payload lolos `verify_ast` (tanpa angka/kutip, tanpa node terlarang).
- `run_sandbox(PAYLOAD)` mengembalikan `_VAULT_STATE` yang sama.
- Hasil dekripsi 42 byte.
- `_encrypt_vault(flag) == _VAULT_STATE` (round-trip PASS).
- Flag sama dengan `flags/wave2/The_Alchemists_Sandbox.txt`.

### Bukti submit di platform

![00b-submit-platform.png](assets/the-alchemists-sandbox/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Verifikasi platform:** flag sudah diterima. Recheck 2026-11-09 mengembalikan `Correct, but already solved.`
