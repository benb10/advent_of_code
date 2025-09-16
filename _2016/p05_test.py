from pathlib import Path

import pytest

from . import p05_a, p05_b


@pytest.mark.skip("slow")
def test_p05a_small():
    s = "abc"

    assert p05_a.run(s) == "18f47a30"


@pytest.mark.skip("slow")
def test_p05a():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_a.run(s) == "f77a0e6e"


@pytest.mark.skip("slow")
def test_p05b_small():
    s = "abc"

    assert p05_b.run(s) == "05ace8e3"


@pytest.mark.skip("slow")
def test_p05b():
    s = (Path(__file__).parent / "p05_input.txt").read_text()

    assert p05_b.run(s) == "999828ec"
