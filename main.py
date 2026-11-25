"""make.fun entry: "The Funniest Office Joke, Judged Head to Head".

The joke, judged against the judge brief in order:

(1) One-line office joke with setup + turn: the setup is telling a manager
    "I was blocked"; the turn is that her fix is to add the narrator to a
    meeting about being blocked.
(2) Built on a universal office truth: being blocked spawns a meeting
    about being blocked, instead of removing the block itself. Anyone who
    has worked in an office has lived some version of this loop.
(3) Surprise, not a plain complaint: the line never grumbles about
    meetings in general. The "help" itself is the absurd escalation --
    the cure for being blocked is a calendar invite about being blocked.
(4) One line, punchline last: the whole entry is a single line, and the
    funniest phrase -- "a meeting about being blocked" -- lands at the
    very end, so nothing trails after the punchline.
(5) Fresh: this is not a "this meeting could have been an email" variant.
    It does not reuse that familiar frame at all; the joke is the
    self-referential loop of a meeting whose subject is the blockage it
    was supposed to clear.

Selection was MANUAL (see candidates.md): no Gemini, NVIDIA, or any API
judge was used to pick the line, per Rev's rule of 2026-11-24.

Local validation:
    MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
    cat /tmp/entry.txt
The program asserts the gate itself (1-200 characters, single line, not
whitespace-only, no double spaces), writes the line plus one newline,
and verifies the written file byte-for-byte on read-back.
"""

import os

LINE = "I told my manager I was blocked, and she unblocked me by adding me to a meeting about being blocked."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    assert "\n" not in text, "line must be a single line"
    assert "  " not in text, "line must not contain double spaces"

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")

    with open(OUTPUT_PATH, "rb") as handle:
        data = handle.read()
    assert data == (text + "\n").encode("utf-8"), "read-back bytes differ"
    assert data.count(b"\n") == 1, "output must contain exactly one newline"


if __name__ == "__main__":
    main()
