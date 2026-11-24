#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: nothing else, no text,
no caption, no trailing newline.

The chosen emoji is U+1F604 SMILING FACE WITH OPEN MOUTH AND SMILING
EYES. A big, genuine, open grin: the kind of face that makes a stranger
smile back at first glance. It is warm and friendly with no context
needed, readable the same way by a stranger of any age or background,
and it is a step more chosen than the first default smiley that comes
to mind while staying instantly readable. It carries no intimacy,
sarcasm, or flirtation that would read oddly coming from someone
unknown — just unguarded delight.
"""

import os

EMOJI = "\U0001F604"  # 😄

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
