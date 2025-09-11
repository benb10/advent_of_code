from pathlib import Path

from . import p03_a, p03_b


def test_p03a_small():
    s = """00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010"""

    assert p03_a.run(s) == 198


def test_p03a():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_a.run(s) == 4191876


def test_p03b_small():
    s = """00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010"""

    assert p03_b.run(s) == 230


def test_p03b():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_b.run(s) == 3414905
