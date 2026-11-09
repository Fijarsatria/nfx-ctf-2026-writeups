#!/usr/bin/env bash
# Reproduksi alur Access Remains (Linux: impacket + 7z).
set -e
EV=Evidence
CFG=$EV/Windows/System32/config
SID=S-1-5-21-3304503823-3980900213-1333018566-1005
MASTER=$EV/Users/ariaf/AppData/Roaming/Microsoft/Protect/$SID/bb24f650-d046-439c-a88b-ab8f89ba61a4
CRED=$EV/Users/ariaf/AppData/Roaming/Microsoft/Credentials/B0294E9651990C1435CA6300E4BB2378
ZIP=$EV/Users/ariaf/Documents/Kumiko.zip
DPAPI=$(python3 -c 'import impacket,os; print(os.path.join(os.path.dirname(impacket.__file__),"..","..","..","share","doc","python3-impacket","examples","dpapi.py"))' 2>/dev/null || true)
if [ ! -f "$DPAPI" ]; then DPAPI=/usr/share/doc/python3-impacket/examples/dpapi.py; fi

echo "[1] SAM/SYSTEM/SECURITY -> NTLM"
impacket-secretsdump -sam "$CFG/SAM" -system "$CFG/SYSTEM" -security "$CFG/SECURITY" local | \
  grep -E 'aria|Target system bootKey|dpapi_'

echo
echo "[2] DPAPI masterkey dengan password ariaf"
python3 "$DPAPI" masterkey -file "$MASTER" -sid "$SID" -password 'ariafe006'

MK=0x2cbc5b2e483dae00c5593617eb517b8cabec639f354ca8f75b4296e82f3c8d2e83f2ce9a6ae64e3f1f849098f985b2d64e74e81affd37021392b7ba7b4635b55
echo
echo "[3] Credential Manager (roaming)"
python3 "$DPAPI" credential -file "$CRED" -key "$MK"

echo
echo "[4] Buka Kumiko.zip"
7z x -y -p'KumikoOumae2107!@' "$ZIP" -o/tmp/kumiko_out

echo
echo "[5] note.txt"
cat /tmp/kumiko_out/note.txt
