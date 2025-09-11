from pathlib import Path

from . import p04_a, p04_b


def test_p04a_small():
    s = """2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8"""

    assert p04_a.run(s) == 2


def test_p04a():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_a.run(s) == 431


def test_p04b_small():
    s = """2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8"""

    assert p04_b.run(s) == 4


def test_p04b():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_b.run(s) == 823
