import hashlib, json
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

MASTER = b"\x13\x37" * 16
d = json.load(open(Path(__file__).resolve().parent / "output.txt"))
ct = bytes.fromhex(d["ct_hex"])
iv = bytes.fromhex(d["iv_hex"])
counter = d["counter"]

key = hashlib.sha256(MASTER + counter.to_bytes(4, "little")).digest()[:32]
pt = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(ct), 16)
assert b"|" in pt
flag = pt.split(b"|", 1)[1].decode()
print("FLAG =", flag)
