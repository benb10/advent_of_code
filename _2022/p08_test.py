from pathlib import Path

from . import p08_a, p08_b


def test_p08a_small():
    s = """30373
    25512
    65332
    33549
    35390"""

    assert p08_a.run(s) == 21


def test_p08a():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_a.run(s) == 1662


def test_p08b_small():
    s = """30373
    25512
    65332
    33549
    35390"""

    assert p08_b.run(s) == 8


def test_p08b():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_b.run(s) == 537600
