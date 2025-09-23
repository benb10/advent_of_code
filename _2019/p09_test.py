from pathlib import Path

import pytest

from . import p09_a, p09_b


def test_p09a_small():
    s = "104,3,99"

    assert p09_a.run(s) == 3


def test_p09a():
    s = (Path(__file__).parent / "p09_input.txt").read_text()

    assert p09_a.run(s) == 3100786347


def test_p09b_small():
    s = "104,3,99"

    assert p09_b.run(s) == 3


@pytest.mark.runtime(1.1)
def test_p09b():
    s = (Path(__file__).parent / "p09_input.txt").read_text()

    assert p09_b.run(s) == 87023
