from pathlib import Path

import pytest

from . import p12_a, p12_b


def test_p12a_small():
    s = """start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end"""

    assert p12_a.run(s) == 10


def test_p12a():
    s = (Path(__file__).parent / "p12_input.txt").read_text()

    assert p12_a.run(s) == 4241


def test_p12b_small():
    s = """start-A
    start-b
    A-c
    A-b
    b-d
    A-end
    b-end"""

    assert p12_b.run(s) == 36


@pytest.mark.skip("slow")
def test_p12b():
    s = (Path(__file__).parent / "p12_input.txt").read_text()

    assert p12_b.run(s) == 122134
