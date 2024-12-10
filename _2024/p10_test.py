from pathlib import Path

from . import p10_a, p10_b


def test_p10a_small():
    s = """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732"""

    assert p10_a.run(s) == 36


def test_p10a():
    s = (Path(__file__).parent / "p10_input.txt").read_text()

    assert p10_a.run(s) == 512


def test_p10b_small():
    s = """
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732"""

    assert p10_b.run(s) == 81


def test_p10b():
    s = (Path(__file__).parent / "p10_input.txt").read_text()

    assert p10_b.run(s) == 1045
