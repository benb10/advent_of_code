from pathlib import Path

from . import p05_a, p05_b


def test_p05a_small():
    s = "1, 0, 3, 3, 104, 10, 99"

    assert p05_a.run(s) == 10


def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == 10987514


def test_p05b_small():
    s = "3, 0, 4, 0, 99"

    assert p05_b.run(s) == 5


def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == 14195011
