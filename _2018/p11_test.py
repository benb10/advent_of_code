from pathlib import Path

import pytest

from . import p11_a, p11_b


def test_p11a_small():
    s = "42"

    assert p11_a.run(s) == "21,61"


def test_p11a():
    s = (Path(__file__).parent / "p11_input.txt").read_text()

    assert p11_a.run(s) == "243,43"


@pytest.mark.runtime(60)
def test_p11b_small():
    s = "18"

    assert p11_b.run(s) == "90,269,16"


@pytest.mark.runtime(60)
def test_p11b():
    s = (Path(__file__).parent / "p11_input.txt").read_text()

    assert p11_b.run(s) == "236,151,15"
