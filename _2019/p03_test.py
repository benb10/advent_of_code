from pathlib import Path

from . import p03_a, p03_b


def test_p03a_small():
    s = """R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83"""

    assert p03_a.run(s) == 159


def test_p03a():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_a.run(s) == 2180


def test_p03b_small():
    s = """R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83"""

    assert p03_b.run(s) == 610


def test_p03b():
    s = (Path(__file__).parent / "p03_input.txt").read_text()

    assert p03_b.run(s) == 112316
