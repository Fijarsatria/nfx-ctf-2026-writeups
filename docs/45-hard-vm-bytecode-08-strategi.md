# Hard VM Bytecode — Strategi

[← Overview](45-hard-vm-bytecode.md) · [Index](index.md)

## 3.1 Strategi

1. Ekstrak bytecode 498 byte dari `.rodata` `0x2080`.
2. Parse tiap 3 byte menjadi `(opcode, reg, arg)`.
3. Kelompokkan 5 instruksi per karakter, berhenti di opcode `0xff`.
4. Inversi `CMP → ROL⁻¹ → ADD⁻¹ → XOR⁻¹`.
5. Simulasikan ulang transformasi forward untuk memastikan setiap `CMP` terpenuhi.
6. Jalankan binary dengan flag hasil rekonstruksi.

### Evidence langkah ini

![term-03-strings.png](assets/hard-vm-bytecode/term-03-strings.png)

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*
