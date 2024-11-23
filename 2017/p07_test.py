from pathlib import Path

import p07_a
import p07_b
import pytest


@pytest.mark.skip("solution not complete")
def test_p07a_small():
    s = """"""

    assert p07_a.run(s) == 1


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
