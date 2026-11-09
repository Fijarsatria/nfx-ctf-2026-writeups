#!/usr/bin/env python3
"""Extract the visible text from the decrypted Dokodemo PDF.

ReportLab writes the page content as /Filter [/ASCII85Decode /FlateDecode].
We decode every such stream and print the PDF text-showing operators.
"""
from pathlib import Path
import base64
import re
import zlib

PDF = Path("/tmp/opencode/dokodemo_decrypted.pdf")


def decode_streams(data: bytes):
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        end = data.find(b"endstream", start)
        raw = data[start:end].rstrip(b"\r\n")
        header = data[max(0, m.start() - 400):m.start()].decode("latin1")
        try:
            a85 = base64.a85decode(raw, adobe=True)
        except Exception:
            continue
        try:
            out = zlib.decompress(a85)
        except Exception:
            continue
        yield header, out


def main() -> None:
    data = PDF.read_bytes()
    print(f"PDF bytes: {len(data)}")
    for header, out in decode_streams(data):
        if b"Tj" not in out:
            continue
        text = out.decode("latin1")
        for m in re.finditer(r"\(((?:[^()\\]|\\.)*)\)\s*Tj", text):
            s = m.group(1)
            s = re.sub(r"\\([()\\])", r"\1", s)
            print(s)


if __name__ == "__main__":
    main()
