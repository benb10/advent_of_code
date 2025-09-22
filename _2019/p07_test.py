from pathlib import Path

import pytest

from . import p07_a, p07_b


def test_p07a_small():
    s = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"

    assert p07_a.run(s) == 54321


def test_p07a():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_a.run(s) == 51679


@pytest.mark.skip("solution not complete")
def test_p07b_small():
    s = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

    assert p07_b.run(s) == 139629729


@pytest.mark.skip("solution not complete")
def test_p07b():
    s = (Path(__file__).parent / "p07_input.txt").read_text()

    assert p07_b.run(s) == 1
