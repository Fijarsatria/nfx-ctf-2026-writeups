# PageStream — Flag & Verifikasi

[← Overview](51-pagestream.md) · [Index](index.md)

> **Langkah 9/11 — Flag.** Flag yang sama diperoleh dari /view dan dari /readflag setelah RCE.
>
> **Titik penting:** NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}
>
> **Berikutnya:** [Bukti / Evidence](51-pagestream-10-bukti-evidence.md)

> **Flag:** `NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}`
> **Status:** `VERIFIED`

```text
NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}
```

Verifikasi:

```bash
cat flags/web/PageStream.txt
# NFX{f3w_n_d4y_ch41ns_f0r_w3b_pwn_1s_n0t_th4t_h4rd_7734a1}
```

Flag yang sama diperoleh dari `/view` dan dari `/readflag` setelah RCE. Tidak ada submit ke platform.

### Bukti submit di platform

![00b-submit-platform.png](assets/pagestream/00b-submit-platform.png)

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

> **Bukti submit:** screenshot form challenge di atas menampilkan `CORRECT, BUT ALREADY SOLVED.`
