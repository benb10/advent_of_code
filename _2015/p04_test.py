from pathlib import Path

import pytest

from . import p04_a, p04_b


def test_p04a_small():
    s = "a"

    assert p04_a.run(s) == 12181


def test_p04a():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_a.run(s) == 117946


@pytest.mark.skip("slow")
def test_p04b_small():
    s = "abcdef"

    assert p04_b.run(s) == 6742839


@pytest.mark.skip("slow")
def test_p04b():
    s = (Path(__file__).parent / "p04_input.txt").read_text()

    assert p04_b.run(s) == 3938038
