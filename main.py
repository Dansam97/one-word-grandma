#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to entry.txt in the output directory: the word
a grandma would text about AI. She means ChatGPT; her thumbs drop the
last letter, the way real grandma texts about new technology actually
go out — warm, baffled, and one keystroke short.
"""

import os

ENTRY_TEXT = "ChatGP"

MAX_CHARS = 30


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the gate rules.

    The gate accepts UTF-8 text of 1 to 30 characters that is not only
    white space; the task itself demands exactly one word, so the text
    must also be a single token with no white space anywhere in it.
    """
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not UTF-8 encodable
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text.split()) != 1 or any(ch.isspace() for ch in text):
        raise ValueError("entry must be exactly one word")
    if len(encoded) != len(text):
        raise ValueError("entry must be plain ASCII so it reads instantly")
    return text


def main() -> None:
    text = validated_text()
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("entry.txt read-back does not match what was written")


if __name__ == "__main__":
    main()
