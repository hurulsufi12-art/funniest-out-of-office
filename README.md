# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/hurulsufi12-art/funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/hurulsufi12-art/funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the [make.fun bounty "The Funniest Out-of-Office"](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf): one single-line out-of-office auto-reply, at most 140 characters.

## The reply

> I'm out of the office and my inbox has unionised: it refuses to answer until I return, and frankly, it's winning.

(113 characters, one line, plain ASCII.)

## How it works

`main.py` (Python 3.13, standard library only) validates the text against the bounty gate — 1–140 characters, not whitespace-only, a single line, no leading/trailing whitespace, no control characters, pure ASCII — and then writes it verbatim, with no trailing newline, to `$OUTPUT_DIR/entry.txt` (default `/output`). The program is fully deterministic: no randomness, no clock, no network, no external input.
