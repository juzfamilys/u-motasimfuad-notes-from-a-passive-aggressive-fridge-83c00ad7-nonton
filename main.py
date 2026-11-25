#!/usr/bin/env python3
"""A fridge that finally says what it thinks.

This is an entry for the make.fun bounty "Notes From a Passive-Aggressive
Fridge". Running the script drops a single complaint from the fridge into
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output when the variable is unset).
The file holds the note and nothing else — not even a newline at the end.

Nothing here needs installing: the script only leans on the Python
standard library, so it runs fine under a plain vanilla interpreter.
"""

import os
import sys

# The one line the fridge gets to say. Do not reword it: the bounty
# judges this exact sentence.
NOTE = "Dear human: you opened my door, stared inside for a full minute, and left with nothing, and somehow I am the one who feels judged."

# The bounty caps an entry at two hundred characters.
CHAR_LIMIT = 200

# Where the note lands when MAKEFUN_OUTPUT_DIR is not set.
FALLBACK_DIR = "/output"

FILENAME = "entry.txt"


def find_faults(line):
    """Collect every way `line` breaks the bounty rules, in plain words.

    An empty list means the line is good to go.
    """
    faults = []

    if line == "":
        faults.append("the note is blank")
    else:
        if line.strip() != line:
            faults.append("the note starts or ends with a space")
        if any(ch in line for ch in ("\n", "\r")):
            faults.append("the note spills onto more than one line")
        if len(line) > CHAR_LIMIT:
            faults.append(
                "the note is %d characters long, %d over the %d-character cap"
                % (len(line), len(line) - CHAR_LIMIT, CHAR_LIMIT)
            )
        if not line.endswith("."):
            faults.append("the note does not finish with a full stop")

    return faults


def assert_note_is_fine(line):
    """Raise if the note breaks any rule; stay silent when it is fine."""
    faults = find_faults(line)
    if faults:
        raise ValueError("bad note: " + "; ".join(faults))


def target_folder():
    """Work out which folder should receive entry.txt."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR


def persist(line, folder):
    """Write `line` to entry.txt inside `folder`, byte for byte.

    The file is opened in binary mode on purpose, so no newline is
    ever appended behind our backs.
    """
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, FILENAME)
    payload = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    return path, payload


def confirm_on_disk(path, expected):
    """Read entry.txt back and make sure it matches what we meant to write."""
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != expected:
        raise ValueError(
            "what came back from disk does not match the note "
            "(%d bytes on disk, %d expected)" % (len(stored), len(expected))
        )
    assert_note_is_fine(stored.decode("utf-8"))


def run():
    # --check only proves the note is valid; it writes no file at all.
    # Handy for a quick sanity pass before a real run.
    if "--check" in sys.argv[1:]:
        assert_note_is_fine(NOTE)
        print("note is valid: %d characters" % len(NOTE))
        return 0

    assert_note_is_fine(NOTE)
    path, payload = persist(NOTE, target_folder())
    confirm_on_disk(path, payload)
    print("saved %d bytes to %s" % (len(payload), path))
    return 0


if __name__ == "__main__":
    sys.exit(run())
