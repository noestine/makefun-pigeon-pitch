"""Tests for main.py — Pigeon Pitch, One Line.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace, a single line in English: the elevator
pitch a city pigeon gives investors for its startup.
"""

import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import main


class TestPitchLine(unittest.TestCase):
    def test_line_length(self):
        self.assertGreaterEqual(len(main.PITCH), 1)
        self.assertLessEqual(len(main.PITCH), 200)

    def test_byte_length(self):
        # Em-dashes are 1 char but 3 bytes; both measures must fit the gate.
        self.assertLessEqual(len(main.PITCH.encode("utf-8")), 200)

    def test_single_line(self):
        self.assertNotIn("\n", main.PITCH)
        self.assertNotIn("\r", main.PITCH)

    def test_non_whitespace(self):
        self.assertNotEqual(main.PITCH.strip(), "")

    def test_utf8(self):
        main.PITCH.encode("utf-8")

    def test_on_subject(self):
        lowered = main.PITCH.lower()
        self.assertIn("invest", lowered)  # addressed to investors
        self.assertIn("pigeon", lowered)  # a pigeon's own voice
        self.assertIn("seed", lowered)  # the startup ask


class TestValidate(unittest.TestCase):
    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            main.validate("")

    def test_whitespace_only_raises(self):
        with self.assertRaises(ValueError):
            main.validate("   \t ")

    def test_too_long_raises(self):
        with self.assertRaises(ValueError):
            main.validate("x" * 201)

    def test_exactly_200_ok(self):
        main.validate("x" * 200)

    def test_multiline_raises(self):
        with self.assertRaises(ValueError):
            main.validate("one\ntwo")

    def test_control_char_raises(self):
        with self.assertRaises(ValueError):
            main.validate("pitch with a \x07 bell")

    def test_non_str_raises(self):
        with self.assertRaises(TypeError):
            main.validate(123)


class TestWriteEntry(unittest.TestCase):
    def test_write_entry_exact_bytes(self):
        tmp = Path("/tmp") / "pigeon-entry-test.txt"
        try:
            main.write_entry(tmp)
            self.assertEqual(tmp.read_bytes(), main.PITCH.encode("utf-8"))
            self.assertFalse(tmp.read_bytes().endswith(b"\n"))
        finally:
            tmp.unlink(missing_ok=True)

    def test_deterministic_two_runs(self):
        tmp1 = Path("/tmp") / "pigeon-entry-test-1.txt"
        tmp2 = Path("/tmp") / "pigeon-entry-test-2.txt"
        try:
            main.write_entry(tmp1)
            main.write_entry(tmp2)
            self.assertEqual(tmp1.read_bytes(), tmp2.read_bytes())
        finally:
            tmp1.unlink(missing_ok=True)
            tmp2.unlink(missing_ok=True)

    def test_subprocess_writes_output_entry(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "main.py")],
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        out = Path("/output/entry.txt")
        self.assertTrue(out.exists())
        self.assertEqual(out.read_bytes(), main.PITCH.encode("utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
