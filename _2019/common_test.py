import pytest

from .common import run_intcode


@pytest.mark.parametrize(
    ("input_kwargs", "expected_output"),
    (
        # simple
        (dict(input_nums=[1, 0, 0, 0, 99]), [2, 0, 0, 0, 99]),
        (dict(input_nums=[1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99]),
        (dict(input_nums=[2, 3, 0, 3, 99]), [2, 3, 0, 6, 99]),
        (dict(input_nums=[2, 4, 4, 5, 99, 0]), [2, 4, 4, 5, 99, 9801]),
        # opcode 5 jump
        (dict(input_nums=[1105, 1, 4, 0, 99]), [1105, 1, 4, 0, 99]),
        # opcode 5 no jump
        (dict(input_nums=[1105, 0, 4, 99]), [1105, 0, 4, 99]),
        # opcode 6 jump
        (dict(input_nums=[1106, 0, 4, 0, 99]), [1106, 0, 4, 0, 99]),
        # opcode 6 no jump
        (dict(input_nums=[1106, 1, 4, 99]), [1106, 1, 4, 99]),
        # opcode 7 store 1
        (dict(input_nums=[1107, 2, 3, 0, 99]), [1, 2, 3, 0, 99]),
        # opcode 7 store 0
        (dict(input_nums=[1107, 3, 2, 0, 99]), [0, 3, 2, 0, 99]),
        # opcode 8 store 1
        (dict(input_nums=[1108, 5, 5, 0, 99]), [1, 5, 5, 0, 99]),
        # opcode 8 store 0
        (dict(input_nums=[1108, 5, -3, 0, 99]), [0, 5, -3, 0, 99]),
        # position mode
        (dict(input_nums=[1101, 5, 6, 0, 99]), [11, 5, 6, 0, 99]),
        (dict(input_nums=[102, 5, 4, 3, 99]), [102, 5, 4, 495, 99]),
        # inputs and outputs
        (dict(input_nums=[3, 1, 4, 1, 99], input_value=123, return_outputs=True), ([3, 123, 4, 1, 99], [123])),
        # p5 part 2 examples
        (
            dict(input_nums=[3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input_value=8, return_outputs=True),
            ([3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8], [1]),
        ),
        (
            dict(input_nums=[3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input_value=9, return_outputs=True),
            ([3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8], [0]),
        ),
        (
            dict(input_nums=[3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input_value=5, return_outputs=True),
            ([3, 9, 7, 9, 10, 9, 4, 9, 99, 1, 8], [1]),
        ),
        (
            dict(input_nums=[3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input_value=111, return_outputs=True),
            ([3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8], [0]),
        ),
        (
            dict(input_nums=[3, 3, 1108, -1, 8, 3, 4, 3, 99], input_value=8, return_outputs=True),
            ([3, 3, 1108, 1, 8, 3, 4, 3, 99], [1]),
        ),
        (
            dict(input_nums=[3, 3, 1108, -1, 8, 3, 4, 3, 99], input_value=-44, return_outputs=True),
            ([3, 3, 1108, 0, 8, 3, 4, 3, 99], [0]),
        ),
        (
            dict(input_nums=[3, 3, 1107, -1, 8, 3, 4, 3, 99], input_value=1, return_outputs=True),
            ([3, 3, 1107, 1, 8, 3, 4, 3, 99], [1]),
        ),
        (
            dict(input_nums=[3, 3, 1107, -1, 8, 3, 4, 3, 99], input_value=11, return_outputs=True),
            ([3, 3, 1107, 0, 8, 3, 4, 3, 99], [0]),
        ),
        # p5 part 2 jump tests
        (
            dict(
                input_nums=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input_value=5, return_outputs=True
            ),
            ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 5, 1, 1, 9], [1]),
        ),
        (
            dict(
                input_nums=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input_value=0, return_outputs=True
            ),
            ([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 0, 0, 1, 9], [0]),
        ),
        (
            dict(input_nums=[3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input_value=7, return_outputs=True),
            ([3, 3, 1105, 7, 9, 1101, 0, 0, 12, 4, 12, 99, 1], [1]),
        ),
        (
            dict(input_nums=[3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input_value=0, return_outputs=True),
            ([3, 3, 1105, 0, 9, 1101, 0, 0, 12, 4, 12, 99, 0], [0]),
        ),
    ),
)
def test_run_intcode(input_kwargs, expected_output):
    output = run_intcode(**input_kwargs)

    assert output == expected_output
