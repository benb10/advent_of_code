from pathlib import Path

import pytest

from . import p05_a, p05_b


def test_p05a_small():
    s = "dabAcCaCBAcCcaDA"

    assert p05_a.run(s) == 10


@pytest.mark.skip("slow")
def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == 9526


def test_p05b_small():
    s = "dabAcCaCBAcCcaDA"

    assert p05_b.run(s) == 4


@pytest.mark.skip("slow")
def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == 6694
