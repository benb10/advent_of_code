from pathlib import Path

from . import p02_a, p02_b


def test_p02a_small():
    s = """forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2"""

    assert p02_a.run(s) == 150


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 1580000


def test_p02b_small():
    s = """forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2"""

    assert p02_b.run(s) == 900


def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 1251263225
