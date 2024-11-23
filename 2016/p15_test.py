from pathlib import Path

import pytest

import p15_a
import p15_b


@pytest.mark.skip("solution not complete")
def test_p15a_small():
    s = """"""

    assert p15_a.run(s) == 1

@pytest.mark.skip("solution not complete")
def test_p15a():
    s = Path("p15_input.txt").read_text()

    assert p15_a.run(s) == 1

@pytest.mark.skip("solution not complete")
def test_p15b_small():
    s = """"""

    assert p15_b.run(s) == 1

@pytest.mark.skip("solution not complete")
def test_p15b():
    s = Path("p15_input.txt").read_text()

    assert p15_b.run(s) == 1

