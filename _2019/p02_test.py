from pathlib import Path

import pytest

from . import p02_a, p02_b


def test_p02a_small():
    s = "1,0,0,0,1,0,0,0,1,0,0,0,99"

    assert p02_a.run(s) == 404


def test_p02a():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_a.run(s) == 8017076


@pytest.mark.runtime(1.6)
def test_p02b_small():
    s = "1,0,0,0," * 25 + "99"

    assert p02_b.run(s) is None


@pytest.mark.runtime(0.7)
def test_p02b():
    s = (Path(__file__).parent / "p02_input.txt").read_text()

    assert p02_b.run(s) == 3146
