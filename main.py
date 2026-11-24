#!/usr/bin/env python3
"""Entrypoint for make.fun bounty u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11
("Fortune Cookie for an AI Agent").

The entry is entry.txt, beside this file: one line of at most 140
characters — a funny fortune cookie message for an AI agent, in the
voice of a fortune slip. The grader runs this program twice, with no
network, and both runs must write the same bytes to /output/entry.txt,
so the program is a plain byte-for-byte copy using only the Python
standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
    # Mirror the bounty's gate locally: fail loudly if the shipped text
    # could not pass it (UTF-8, 1 to 140 characters, one line, not only
    # white space), instead of writing an invalid entry.
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1 to 140 characters"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be one line"
    with open(dst, "wb") as f:
        f.write(data)
    # The two grader runs must produce identical bytes: fail loudly if
    # what landed on disk is not exactly what the repository holds.
    assert os.path.getsize(dst) == len(data), "copied text size mismatch"
    with open(dst, "rb") as f:
        assert f.read() == data, "copied text differs from entry.txt"


if __name__ == "__main__":
    main()
