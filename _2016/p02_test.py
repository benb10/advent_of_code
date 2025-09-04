from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """ULL
    RRDDD
    LURDL
    UUUUD"""

    assert p02_a.run(s) == 1985


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 84452


def test_p02b_small():
    s = """ULL
    RRDDD
    LURDL
    UUUUD"""

    assert p02_b.run(s) == "5DB3"


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == "D65C3"
