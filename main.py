# The Internet in One Word — make.fun entry (Python 3.13, stdlib only).
#
# The program writes exactly one word to /output/entry.txt: the single
# word that describes the whole internet. The word lives in word.txt
# beside this file; main.py reads it, strips it, checks the gate
# (1-30 chars, one word, not only whitespace) and writes exactly those
# bytes, with no trailing newline — the judge reads exactly the bytes
# written.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    with open(os.path.join(HERE, "word.txt"), encoding="utf-8") as f:
        word = f.read().strip()
    # One word, letters only: the judge brief rules out sentences,
    # explanations and punctuation tricks, so the entry must not lean
    # on any of those — the humour has to live in the word itself.
    if (not word or len(word) > 30 or len(word.split()) != 1
            or not word.isalpha() or not word.isascii()):
        print("word.txt must hold exactly one ASCII word of 1-30 letters",
              file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
