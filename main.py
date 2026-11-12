#!/usr/bin/env python3
"""make.fun cutest-picture-01 entry: copy the picture to /output/entry.png.

The picture is the entry.jpg beside this file (JPEG bytes; the gate reads
the file by its first bytes and the name stays entry.png either way). Runs
offline, standard library only, and writes the same bytes every time:
a plain byte copy, so two runs are always identical.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.jpg", OUT / "entry.png")


if __name__ == "__main__":
    main()
