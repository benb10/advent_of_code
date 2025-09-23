from pathlib import Path

import pytest

from . import p05_a, p05_b


def test_p05a_small():
    s = """0
    3
    0
    1
    -3"""

    assert p05_a.run(s) == 5


def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == 373543


def test_p05b_small():
    s = """0
    3
    0
    1
    -3"""

    assert p05_b.run(s) == 10


@pytest.mark.runtime(7)
def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == 27502966
