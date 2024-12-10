from pathlib import Path

import pytest

from . import p09_a, p09_b


def test_p09a_small():
    s = "2333133121414131402"

    assert p09_a.run(s) == 1928


def test_p09a():
    s = (Path(__file__).parent / "p09_input.txt").read_text()

    assert p09_a.run(s) == 6356833654075


def test_p09b_small():
    s = "2333133121414131402"

    assert p09_b.run(s) == 2858


@pytest.mark.skip("not complete")
def test_p09b():
    s = (Path(__file__).parent / "p09_input.txt").read_text()

    assert p09_b.run(s) == 1
