from pathlib import Path

import pytest

import p07_a
import p07_b

@pytest.mark.skip("solution not complete")
def test_p07a_small():
    s = """32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483"""

    assert p07_a.run(s) == 6440

@pytest.mark.skip("solution not complete")
def test_p07a():
    s = Path("p07_input.txt").read_text()

    assert p07_a.run(s) == 1

@pytest.mark.skip("solution not complete")
def test_p07b_small():
    s = """"""

    assert p07_b.run(s) == 1

@pytest.mark.skip("solution not complete")
def test_p07b():
    s = Path("p07_input.txt").read_text()

    assert p07_b.run(s) == 1

