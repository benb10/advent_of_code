from pathlib import Path

from . import p07_a, p07_b


def test_p07a_small():
    s = """32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483"""

    assert p07_a.run(s) == 6440


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == 253603890


def test_p07b_small():
    s = """32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483"""

    assert p07_b.run(s) == 5905


def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 253630098
