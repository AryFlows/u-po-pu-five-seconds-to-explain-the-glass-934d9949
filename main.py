#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — writes the cat's one-sentence defence."""
import os

LINE = "It was already leaning, so I gave it the little push it was clearly begging for — gravity did the paperwork and I merely supervised the landing."

def main():
    text = LINE.strip()
    assert text and text == LINE.strip(), "line must not be blank or padded"
    assert text.endswith("."), "entry must be one complete sentence"
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "read-back mismatch"
    print(f"wrote {len(text)} chars to {path}")

if __name__ == "__main__":
    main()
