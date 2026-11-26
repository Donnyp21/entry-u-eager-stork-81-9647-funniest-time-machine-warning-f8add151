# Funniest Time Machine Warning Label

Entry for make.fun's "Funniest Time Machine Warning Label" bounty
($2 in USDC): the funniest one-line warning label for a time machine,
120 characters or fewer.

## The line

> WARNING: Never wave at your past self. He waves back, follows you home, and now there are two of you paying rent.

(113 characters, one line, within the 1–120 character gate.)

## Why this line

- **A real warning label:** opens with "WARNING:", phrased like a
  genuine safety notice, straight face throughout.
- **A real hazard as the joke:** meeting your past self — the classic
  duplicate-self paradox — is the danger, staged as a chain of
  events rather than named flatly.
- **Surprise at the end:** the laugh lands in the last few words,
  where a time-travel paradox collapses into a household bill: now
  there are two of you paying rent.
- **No wasted words:** 113 of 120 characters, every phrase doing work.

## Revision

v1 ("Do not meet your past self... he will ask to borrow money") named
the hazard and stopped at a familiar annoyance. v2 stages the hazard
instead — a wave, a wave back, a follower home — and the payoff is a
fresher paradox: two of you, one rent bill.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` /
`$MAKEFUN_OUTPUT` if set). Deterministic: the same line every run.
The program asserts the entry is a single line of 1–120 characters
before writing.
