"""Funniest Time Machine Warning Label — a straight-faced safety
notice for a time machine, 120 characters or fewer.

REVISION (v1 -> v2): the v1 line ("Do not meet your past self... he
will ask to borrow money") named the hazard and stopped at a familiar
annoyance. The v2 line stages the hazard instead: a wave, a wave back,
a follower home — and the surprise lands in the last few words, where
the paradox becomes a household bill: now there are two of you paying
rent. Same straight-faced notice format, sharper payoff.
"""

import os

LINE = (
    "WARNING: Never wave at your past self. He waves back, follows "
    "you home, and now there are two of you paying rent."
)

assert 1 <= len(LINE) <= 120, len(LINE)
assert "\n" not in LINE.strip()

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT") or "/output"
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(f"wrote entry ({len(LINE)} chars)")
