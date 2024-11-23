from pathlib import Path

import p11_a
import p11_b
import pytest


@pytest.mark.skip("solution not complete")
def test_p11a_small():
    s = """"""

    assert p11_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p11a():
    s = Path("p11_input.txt").read_text()

    assert p11_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p11b_small():
    s = """"""

    assert p11_b.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p11b():
    s = Path("p11_input.txt").read_text()

    assert p11_b.run(s) == 1
