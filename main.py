#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is one line of error copy: the brutal truth about what broke,
delivered with a laugh. Deterministic, offline, no arguments.
"""
import os


ERROR_LINE = "Error 418: the database did not crash, it simply gave up after reading your migration and decided to become a spreadsheet."
# One line, 122 characters, written for this bounty only.


def write_entry():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ERROR_LINE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
