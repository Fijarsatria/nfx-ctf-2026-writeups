# Unbreakable Delay — Output asli simulasi

[← Overview](23-unbreakable-delay.md) · [Index](index.md)

## 3.3 Output asli simulasi

```text
$ python3 writeups/assets/unbreakable-delay/sim_vdf.py
[instance] N bits       = 1023
[instance] p ^ q        = 0x1000000000000000000000000000000000000000000000000000000000000000000000000000
[instance] p            = 0x8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005eedbeef123477cdf
[attack]  factored N    = True  p == p2: True
[attack]  y = 2^(2^256) mod N computed instantly with the phi shortcut
[attack]  challenge l    = 0x6d4871162202f4d5
[attack]  proof pi       = 0x14277737e84f6d07280a6a28165b9d1217a4c3f735635f ...
[verify]  pi^l * x^(T%l) == y mod N : True
```

**Label:** output di atas berasal dari **instance sintetis**, bukan dari
service NFX. Yang dibuktikan adalah kebenaran matematis serangan
(`factored N = True`, `verify = True`), bukan flag.
