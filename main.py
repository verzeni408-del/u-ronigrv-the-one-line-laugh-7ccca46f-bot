"""The One-Line Laugh — entry v2.

Writes the one-line joke to /output/entry.txt exactly, no trailing newline.
Stdlib only, no network.
"""

import os

ENTRY = "My smart fridge judges my midnight snacks out loud, so now I eat standing up so it thinks I'm exercising."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
