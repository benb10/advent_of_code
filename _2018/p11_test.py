from pathlib import Path

import pytest

from . import p11_a, p11_b


@pytest.mark.skip("solution not complete")
def test_p11a_small():
    s = """"""

    assert p11_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p11a():
    s = (Path(__file__).parent / "p11_input.txt").read_text()

    assert p11_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p11b_small():
    s = """"""

    assert p11_b.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p11b():
    s = (Path(__file__).parent / "p11_input.txt").read_text()

    assert p11_b.run(s) == 1
