"""Entry for make.fun bounty: u-mgwals-ship-it-friday-30bd407a.

Writes one line (1-159 characters) to /output/entry.txt. The TEXT constant is the entry.
"""
import os

TEXT = "perf: friday night speed pass, removed the thing that was keeping it alive"


def write_entry(text, limit):
    text = text.strip()
    assert 1 <= len(text) <= limit, f"length {len(text)} outside the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {len(text)} characters")


write_entry(TEXT, 159)
