from pathlib import Path

import pytest

from . import p06_a, p06_b


def test_p06a_small():
    s = """turn on 1,1 through 3,3
    toggle 1,1 through 1,5
    turn off 2,2 through 3,3"""

    assert p06_a.run(s) == 4


@pytest.mark.skip("slow")
def test_p06a():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_a.run(s) == 543903


def test_p06b_small():
    s = """turn on 1,1 through 3,3
    toggle 1,1 through 1,5
    turn off 2,2 through 3,3"""

    assert p06_b.run(s) == 15


@pytest.mark.skip("slow")
def test_p06b():
    s = (Path(__file__).parent / "p06_input.txt").read_text()

    assert p06_b.run(s) == 14687245
