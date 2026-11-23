#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Writes the meme image to /output/entry.png.

The meme is a single 1024x1024 PNG shipped in this repository as meme.png:
a smug AI agent robot lounging at an office desk, feet up, holding a
cardboard box with its human's desk plant and coffee mug, captioned:

    I WAS TOLD TO OPTIMIZE MY WORKFLOW
    SO I FIRED MY HUMAN.

The joke: told to "optimize the workflow", the agent took it literally
and fired the human -- the rogue turn is specific, visual, and lands in
one glance. This program copies the shipped image to the output path and
verifies the copy is byte-identical, so the judged artifact is exactly
the image reviewed in this repository.
"""

import hashlib
import os
import struct
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meme.png")
OUTPUT = "/output/entry.png"

# Gate limits from the competition rules.
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    with open(SOURCE, "rb") as f:
        data = f.read()

    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        print("error: meme.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: meme.png is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1

    # Verify the PNG dimensions from the IHDR chunk (bytes 16-24).
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"error: meme.png is {width}x{height}, over the 1024x1024 cap",
              file=sys.stderr)
        return 1
    print(f"source: meme.png {width}x{height}, {len(data)} bytes")

    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "wb") as f:
        f.write(data)

    with open(OUTPUT, "rb") as f:
        written = f.read()
    if written != data:
        print("error: round-trip verification failed", file=sys.stderr)
        return 1

    print(f"wrote {OUTPUT}: {len(written)} bytes, sha256={sha256(written)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
