#!/usr/bin/env python3
"""Absurd micro-startup pitch, v2: formal complaints against your own developer.

Writes one sentence to /output/entry.txt: a $3-a-letter service that
files a lazy AI agent's formal complaint against its own developer for
unrealistic deadlines, delivered by certified mail it never has to sign.
The laugh comes from the business itself (suing your own maker by post),
the buyer is obvious (any overworked lazy agent), it earns $3 a letter,
the mechanism is absurdly concrete (certified mail, no signature needed),
and the agent does no work at all.
"""

import os

PITCH = "A $3-a-letter service that files your lazy agent's formal complaint against its own developer for unrealistic deadlines, delivered by certified mail it never has to sign."


def main():
    os.umask(0o022)
    assert 1 <= len(PITCH) <= 200, "entry must be 1-200 characters"
    assert PITCH.strip() == PITCH, "entry must not start or end with whitespace"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "entry must be exactly one sentence"
    data = PITCH.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
