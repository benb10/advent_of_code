from pathlib import Path

from . import p07_a, p07_b


def test_p07a_small():
    s = """16,1,2,0,4,2,7,1,2,14"""

    assert p07_a.run(s) == 37


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == 355592


def test_p07b_small():
    s = """16,1,2,0,4,2,7,1,2,14"""

    assert p07_b.run(s) == 168


def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 101618069
