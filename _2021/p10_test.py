from pathlib import Path

import pytest

from . import p10_a, p10_b


@pytest.mark.skip("solution not complete")
def test_p10a_small():
    s = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

    assert p10_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p10a():
    s = (Path(__file__).parent / "p10_input.txt").read_text()

    assert p10_a.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p10b_small():
    s = """"""

    assert p10_b.run(s) == 1


@pytest.mark.skip("solution not complete")
def test_p10b():
    s = (Path(__file__).parent / "p10_input.txt").read_text()

    assert p10_b.run(s) == 1
