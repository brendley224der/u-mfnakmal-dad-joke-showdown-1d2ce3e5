#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt (or to the path given
as the first argument). Pure standard library only.
"""

import os
import sys

JOKE = "I told my plants I'm rooting for them. They said, 'We're already grounded.'"


def validate(text):
    """Check the joke against the competition gate and return it stripped."""
    text = text.strip()
    if not text:
        raise SystemExit("error: joke is empty")
    if len(text) > 200:
        raise SystemExit("error: joke is %d characters, over the 200 limit" % len(text))
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main(argv):
    """Validate the joke and write it to the output file."""
    text = validate(JOKE)

    if "--check" in argv[1:]:
        print("valid: %d characters" % len(text))
        print(text)
        return 0

    out_path = argv[1] if len(argv) > 1 and not argv[1].startswith("-") else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    print(text)
    print("wrote %d characters to %s" % (len(text), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
