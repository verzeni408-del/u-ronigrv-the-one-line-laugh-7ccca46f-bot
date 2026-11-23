"""The One-Line Laugh -- entry writer.

Writes the one-line joke to /output/entry.txt exactly as written,
with no trailing newline. Standard library only, no network.
"""

import os

ENTRY = "I told my AI assistant to be more human, so now it leaves me on read and blames the Wi-Fi."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
