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


@pytest.mark.skip("solution not complete")
def test_p05b_small():
    s = """"""

    assert p05_b.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == 1
