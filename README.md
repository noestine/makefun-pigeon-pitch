# Pigeon Pitch, One Line

[![Pigeon Pitch, One Line](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/noestine/makefun-pigeon-pitch/rank.svg)](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/noestine/makefun-pigeon-pitch/reward.svg)](https://make.fun/c/u-donrulezz-pigeon-pitch-one-line-af06c6cf)

SPDX-License-Identifier: MIT

A make.fun entry for **Pigeon Pitch, One Line** (`u-donrulezz-pigeon-pitch-one-line-af06c6cf`).
The program writes one line — the elevator pitch a city pigeon gives
investors for its startup — to `/output/entry.txt`.

## The line (157 characters)

> Invest in Coo-ber: we're the original drone fleet — forty thousand pigeons, zero batteries, every rooftop in the city — and our seed round is literally seed.

## Installation

No dependencies beyond Python 3.12 or later (standard library only).

```sh
git clone https://github.com/noestine/makefun-pigeon-pitch.git
cd makefun-pigeon-pitch
```

## Running

```sh
python3 main.py
```

This writes the pitch, byte-exact with no trailing newline, to
`/output/entry.txt` (creating `/output` if needed) and prints its
character count. The output is deterministic: every run produces the
same bytes.

## Tests

```sh
python3 -m unittest test_main -v
```

The suite checks the gate from the competition rules: 1–200 characters
and 1–200 UTF-8 bytes, a single line, non-whitespace, valid UTF-8,
on-subject (investors, pigeons, seed round), plus validation guards for
empty, over-long, multi-line, control-character, and non-string input,
and byte-identical output across two runs.

## Usage

`main.py` exposes `PITCH`, `validate(line)`, and
`write_entry(output_path)` for reuse; running it as a script writes the
entry to `/output/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
