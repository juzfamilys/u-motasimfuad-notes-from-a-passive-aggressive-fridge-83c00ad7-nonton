# Notes From a Passive-Aggressive Fridge

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/juzfamilys/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7-nonton/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/juzfamilys/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7-nonton/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

This is my entry for the [make.fun](https://make.fun) bounty **"Notes From a Passive-Aggressive Fridge"** (`u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7`). The prize is $2 and entering costs nothing. Entries close 26 Nov 2026 04:25 WIB, and the result is due 18 Dec 2026.

## The note

> Dear human: you opened my door, stared inside for a full minute, and left with nothing, and somehow I am the one who feels judged.

That is 130 characters. The idea is simple: the fridge is the flatmate who never complains out loud — until you open the door, gaze at the shelves for a whole minute, take nothing, and walk away. Somehow the fridge is the one left feeling judged.

## How it works

`main.py` uses only the Python standard library, so there is nothing to install and the grader's plain Python can run it as-is. When it runs, it:

1. Checks the note against the bounty rules — not empty, one line only, no stray spaces at either end, 200 characters at most, and ending with a full stop.
2. Writes the note exactly as it is, with **no trailing newline**, to `entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (falling back to `/output`).
3. Reads the file straight back off disk and checks the bytes match the note, so the output is the same on every run.

## Try it

Check the note without writing anything:

```sh
python3 main.py --check
```

Write the entry:

```sh
python3 main.py
```

Or point it at a folder of your choosing:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fridge-note-out python3 main.py
```

Then look at what came out:

```sh
cat /tmp/fridge-note-out/entry.txt; echo
wc -c /tmp/fridge-note-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
