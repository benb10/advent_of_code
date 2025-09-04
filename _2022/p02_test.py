from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """A Y
    B X
    C Z"""

    assert p02_a.run(s) == 15


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 17189


def test_p02b_small():
    s = """A Y
    B X
    C Z"""

    assert p02_b.run(s) == 12


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 13490
