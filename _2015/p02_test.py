from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """2x3x4
    1x1x10"""

    assert p02_a.run(s) == 101


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 1588178


def test_p02b_small():
    s = """2x3x4
        1x1x10"""

    assert p02_b.run(s) == 48


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 3783758
