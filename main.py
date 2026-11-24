"""Loading Screen Gold: a tip in 200 characters.

Writes the chosen loading-screen tip to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it to stdout. Stdlib only.
"""

import os

LINE = (
    "Tip: the loading screen is the only honest part of your build "
    "\u2014 it admits it is stuck instead of saying \"almost done\" "
    "for 40 minutes."
)


def main():
    if len(LINE) > 200:
        raise ValueError(f"tip is {len(LINE)} characters, over the 200 limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
