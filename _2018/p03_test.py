from pathlib import Path

from . import p03_a, p03_b


def test_p03a_small():
    s = """#1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2"""

    assert p03_a.run(s) == 4


def test_p03a():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_a.run(s) == 120408


def test_p03b_small():
    s = """#1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2"""

    assert p03_b.run(s) == 3


def test_p03b():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_b.run(s) == 1276
