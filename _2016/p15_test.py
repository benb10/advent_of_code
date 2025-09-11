from pathlib import Path

from . import p15_a, p15_b


def test_p15a_small():
    s = """Disc #1 has 5 positions; at time=0, it is at position 4.
    Disc #2 has 2 positions; at time=0, it is at position 1."""

    assert p15_a.run(s) == 5


def test_p15a():
    s = (Path(__file__).parent / "p15_input.txt").read_text()

    assert p15_a.run(s) == 148737


def test_p15b_small():
    s = """Disc #1 has 5 positions; at time=0, it is at position 4.
    Disc #2 has 2 positions; at time=0, it is at position 1."""

    assert p15_b.run(s) == 85


def test_p15b():
    s = (Path(__file__).parent / "p15_input.txt").read_text()

    assert p15_b.run(s) == 2353212
