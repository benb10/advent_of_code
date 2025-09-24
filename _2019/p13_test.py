from pathlib import Path

import pytest

from . import p13_a, p13_b


def test_p13a_small():
    s = "104,0,104,0,104,2,104,1,104,1,104,2,99"

    assert p13_a.run(s) == 2


def test_p13a():
    s = (Path(__file__).parent / "p13_input.txt").read_text()

    assert p13_a.run(s) == 296


def test_p13b_small():
    s = "0,0,0,0,104,0,104,0,104,3,104,1,104,1,104,4,99"

    assert p13_b.run(s) == 0


@pytest.mark.runtime(5)
def test_p13b():
    s = (Path(__file__).parent / "p13_input.txt").read_text()

    assert p13_b.run(s) == 13824
