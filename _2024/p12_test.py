from pathlib import Path

from . import p12_a, p12_b


def test_p12a_small():
    s = """
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE"""

    assert p12_a.run(s) == 1930


def test_p12a():
    s = (Path(__file__).parent / "p12_input.txt").read_text()

    assert p12_a.run(s) == 1533644


def test_p12b_small():
    s = """AAAA
    BBCD
    BBCC
    EEEC"""

    assert p12_b.run(s) == 80


def test_p12b():
    s = (Path(__file__).parent / "p12_input.txt").read_text()

    assert p12_b.run(s) == 936718
