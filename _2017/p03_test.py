from pathlib import Path

from . import p03_a, p03_b


def test_p03a_small():
    s = "1024"

    assert p03_a.run(s) == 31


def test_p03a():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_a.run(s) == 552


def test_p03b_small():
    s = "800"

    assert p03_b.run(s) == 806


def test_p03b():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_b.run(s) == 330785
