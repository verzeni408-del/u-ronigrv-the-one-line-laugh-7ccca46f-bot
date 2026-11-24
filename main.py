"""The One-Line Laugh — entry v3.

Writes the one-line joke to /output/entry.txt exactly, no trailing newline.
Stdlib only, no network.
"""

import os

ENTRY = "I asked my agent to save me time, so it cancelled my meetings, my gym membership, and my wedding."

OUTPUT_PATH = "/output/entry.txt"


# The entry is written exactly as-is: one line, no trailing newline.
def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
