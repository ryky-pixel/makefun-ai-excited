#!/usr/bin/env python3
"""Write the entry image to the output directory, byte for byte.

The entry is a single image: a colossal golden chess knight bursting
through a glass ceiling above a night city, glass shards and light
trailing behind it. This program does not draw or alter anything; it
copies the bundled entry.png to $MAKEFUN_OUTPUT_DIR/entry.png
(default /output/entry.png), so every run produces identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
