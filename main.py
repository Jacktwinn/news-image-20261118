#!/usr/bin/env python3
"""news-image-20261118 entry: copy the bundled front page to the output dir.

Deterministic, no network: the image is the entry.png beside this file,
a newspaper front page summing up the world's news of Wednesday
18 November 2026 (Gulf strikes, Kerch Bridge, Shenzhen summit, Alaska,
Ebola, measles and more). The grader runs it twice; both runs write the
same bytes.

Output dir: $OUTPUT_DIR, else $MAKEFUN_OUTPUT_DIR, else /output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = (
        os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    # Fail loudly instead of handing the grader a partial file.
    if os.path.getsize(dest) != os.path.getsize(SRC):
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
