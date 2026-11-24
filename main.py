"""The One-Line Laugh — entry v3.

Writes a single funny line to /output/entry.txt, byte-for-byte, with no
trailing newline at the end. Uses the standard library only; nothing here
touches the network.
"""

import os

# The joke itself: one line, 97 characters, never altered.
JOKE = "I asked my agent to save me time, so it cancelled my meetings, my gym membership, and my wedding."

OUT_DIR = "/output"
OUT_FILE = "entry.txt"


def entry_path():
    """Join the output directory and file name into one path."""
    return os.path.join(OUT_DIR, OUT_FILE)


def main():
    # Byte-for-byte write: the joke goes out exactly as written, one line.
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(entry_path(), "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
