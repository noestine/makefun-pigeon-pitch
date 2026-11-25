"""Pigeon Pitch, One Line — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
elevator pitch a city pigeon gives investors for its startup.

Stdlib only, deterministic, no network, no environment reads, no
randomness. The output file holds exactly the pitch — no trailing
newline, so the file IS the line.
"""

from pathlib import Path

PITCH = (
    "Invest in Coo-ber: we're the original drone fleet \u2014 forty thousand "
    "pigeons, zero batteries, every rooftop in the city \u2014 and our seed "
    "round is literally seed."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(line):
    """Check one candidate line against the competition gate.

    Raises TypeError for a non-str input and ValueError for anything
    the gate would refuse: empty or whitespace-only, more than one
    line, over 200 characters, or over 200 UTF-8 bytes.
    """
    if not isinstance(line, str):
        raise TypeError("pitch must be str, got %s" % type(line).__name__)
    if not line.strip():
        raise ValueError("pitch must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("pitch must be a single line")
    # Control characters (other than the line breaks already rejected)
    # would corrupt the single-line text the gate and the judge read.
    for char in line:
        if ord(char) < 0x20 or ord(char) == 0x7F:
            raise ValueError(
                "pitch must not contain control character U+%04X" % ord(char)
            )
    if len(line) > MAX_CHARS:
        raise ValueError(
            "pitch is %d characters, over the 200-character gate" % len(line)
        )
    encoded = line.encode("utf-8")
    if len(encoded) > MAX_CHARS:
        raise ValueError(
            "pitch is %d UTF-8 bytes, over the 200-character gate" % len(encoded)
        )
    return line


def write_entry(output_path=OUTPUT_PATH):
    """Validate the pitch and write it, byte-exact, to output_path."""
    line = validate(PITCH)
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(line.encode("utf-8"))
    return path


def main():
    path = write_entry()
    print("wrote %d characters to %s" % (len(PITCH), path))


if __name__ == "__main__":
    main()
