from pathlib import Path

from . import p03_a, p03_b


def test_p03a_small():
    s = """5 10 25
    3 4 5
    3 4  3"""

    assert p03_a.run(s) == 2


def test_p03a():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_a.run(s) == 993


def test_p03b_small():
    s = """5 3 3
    10 4 4
    25 5  3"""

    assert p03_b.run(s) == 2


def test_p03b():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_b.run(s) == 1849
