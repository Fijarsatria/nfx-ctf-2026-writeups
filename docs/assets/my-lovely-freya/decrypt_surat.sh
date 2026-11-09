#!/usr/bin/env bash
# My Lovely Freya - decrypt surat_untuk_freya.enc.
# Password comes from the appended PNG rows: <!HayamGoreng45@/>
# The metadata secret ("AyamgGoreng45") is a decoy: it is missing the
# leading H, the trailing @, and the <!/> wrapper.
set -euo pipefail

IN=/tmp/opencode/nfx/freya/surat_untuk_freya.enc
OUT=/home/bocil/ctf/nfx/writeups/assets/my-lovely-freya/03-surat-decrypted.txt

xxd "$IN" | head -4
echo "--- openssl decrypt ---"
openssl enc -d -aes-256-cbc -md sha256 -pbkdf2 -iter 100000 \
  -in "$IN" -pass 'pass:<!HayamGoreng45@/>' -out "$OUT"
echo "exit=$?"
echo "--- plaintext ---"
cat "$OUT"
echo "--- plaintext hex ---"
xxd "$OUT"
