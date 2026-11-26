"""Deadpan Forecasts entry for make.fun bounty
u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.

Writes one absurd but believable weather line for an invented city
(at most 160 characters) to /output/entry.txt. Blortvale gets a light
rain of small frogs at 14 degrees with 30 km/h winds — a concrete
temperature, a concrete wind speed, and frogs that are polite but
persistent, delivered in the flat tone of a real broadcast.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "Blortvale tonight: light rain of small frogs, 14 degrees, winds 30 km/h. Umbrellas advised. The frogs are polite but persistent."

MAX_CHARS = 160


def validate(line):
    """Gate: 1-160 characters, a single line, one complete sentence."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.endswith("."):
        raise SystemExit("line must be one complete sentence")


def main():
    line = LINE.strip()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
