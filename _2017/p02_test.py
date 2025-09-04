from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """5 1 9 5
    7 5 3
    2 4 6 8"""

    assert p02_a.run(s) == 18


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 47136


def test_p02b_small():
    s = """5 9 2 8
    9 4 7 3
    3 8 6 5"""

    assert p02_b.run(s) == 9


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 250
