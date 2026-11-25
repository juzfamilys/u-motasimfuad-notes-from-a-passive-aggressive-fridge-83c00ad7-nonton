# Notes From a Passive-Aggressive Fridge

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/juzfamilys/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7-nonton/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/juzfamilys/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7-nonton/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

Entry for the [make.fun](https://make.fun) bounty **"Notes From a Passive-Aggressive Fridge"** (`u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7`, $2 prize, free to enter). Entries close 26 Nov 2026 04:25 WIB; results due 18 Dec 2026.

## The entry

> Dear human: you opened my door, stared inside for a full minute, and left with nothing, and somehow I am the one who feels judged.

130 characters — a fridge as a passive-aggressive roommate: the human opens the door, stares inside for a full minute, takes nothing, and the fridge ends up feeling judged.

## How it works

`main.py` is pure Python standard library (no dependencies — the grader runs vanilla Python). It writes exactly that one line, byte for byte with **no trailing newline**, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

Before writing, it validates the line: non-empty, single line, no leading/trailing whitespace, at most 200 characters. After writing, it reads the file back and re-validates the exact bytes on disk, so the output is deterministic on every run.

## Run it

```sh
python3 main.py
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fridge-note-out python3 main.py
```

Then check the result:

```sh
cat /tmp/fridge-note-out/entry.txt; echo
wc -c /tmp/fridge-note-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
