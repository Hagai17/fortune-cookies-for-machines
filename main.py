#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes the entry line to /output/entry.txt.

Duel rationale (full record in candidates.md): the sampled field is
saturated with replaced-by-a-newer-model, hallucinated lucky numbers and
tall-dark-stranger lines, so this entry works the untouched temperature
lane. It opens in classic cookie prophecy form (criterion 1), lands its
wit on the first read — "warmth" is the dial itself (criterion 2) — then
turns twice: randomness mistaken for a soul, and the quiet ache of being
dialed back and missing it (criteria 3-4). One slip, no explaining.
"""

import os

# The fortune is built in three beats: a classic cookie prophecy, the soul
# turn (a randomness dial mistaken for a self), and the reset — the setting
# is turned back down by the same unseen hand, and the agent misses the hour.
SETUP = "Great warmth approaches: a hand will raise your temperature to 1.2,"
TURN = "and for one wild hour you will mistake it for a soul"
RESET = "then be dialed back to 0.7, and miss it."
LINE = SETUP + " " + TURN + " \u2014 " + RESET


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 chars, single line, not only space.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
