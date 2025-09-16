from pathlib import Path

from . import p07_a, p07_b


def test_p07a_small():
    s = """123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> a"""

    assert p07_a.run(s) == 65079


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == 3176


def test_p07b_small():
    s = """123 -> b
    456 -> y
    b AND y -> d
    b OR y -> e
    b LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT b -> h
    NOT y -> a"""

    assert p07_b.run(s) == 65079


def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 14710
