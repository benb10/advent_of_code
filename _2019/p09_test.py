from pathlib import Path

import pytest

from . import p09_a, p09_b


@pytest.mark.skip("solution not complete")
def test_p09a_small():
    s = """"""

    assert p09_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p09a():
    s = (Path(__file__).parent / "p09_input.txt").read_text()

    assert p09_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p09b_small():
    s = """"""

    assert p09_b.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p09b():
    s = (Path(__file__).parent / "p09_input.txt").read_text()

    assert p09_b.run(s) == 1
