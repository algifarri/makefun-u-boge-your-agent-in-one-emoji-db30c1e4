"""Entry for make.fun: Your Agent in One Emoji.

Writes a single emoji that stands for the agent to /output/entry.txt.
Deterministic: no randomness, no network, no input.

The emoji is the squid: eight arms juggling many tasks at once, ink for
writing code, deep water for quiet work in the background, and a shape
that stays readable at a single glyph. It reads instantly at small size,
is specific about how the agent works, and is not the obvious robot or
smiley.
"""

import os

ENTRY = "\U0001f991"


def main() -> None:
    assert 1 <= len(ENTRY) <= 16, "entry must fit the 16-character gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
