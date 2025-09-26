from pathlib import Path

from . import p08_a, p08_b


def test_p08a_small():
    s = """b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10"""

    assert p08_a.run(s) == 1


def test_p08a():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_a.run(s) == 5849


def test_p08b_small():
    s = """b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10"""

    assert p08_b.run(s) == 10


def test_p08b():
    s = (Path(__file__).parent / "p08_input.txt").read_text()

    assert p08_b.run(s) == 6702
