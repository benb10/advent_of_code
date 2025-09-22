import pytest

from .common import IntcodeOutput, run_intcode


@pytest.mark.parametrize(
    ("input_kwargs", "expected_output"),
    (
        # simple
        (
            dict(input_nums=[1, 0, 0, 0, 99]),
            IntcodeOutput(nums=[2, 0, 0, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        (
            dict(input_nums=[1, 1, 1, 4, 99, 5, 6, 0, 99]),
            IntcodeOutput(
                nums=[30, 1, 1, 4, 2, 5, 6, 0, 99], outputs=[], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[2, 3, 0, 3, 99]),
            IntcodeOutput(nums=[2, 3, 0, 6, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        (
            dict(input_nums=[2, 4, 4, 5, 99, 0]),
            IntcodeOutput(nums=[2, 4, 4, 5, 99, 9801], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # opcode 5 jump
        (
            dict(input_nums=[1105, 1, 4, 0, 99]),
            IntcodeOutput(nums=[1105, 1, 4, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # opcode 5 no jump
        (
            dict(input_nums=[1105, 0, 4, 99]),
            IntcodeOutput(nums=[1105, 0, 4, 99], outputs=[], instruction_pointer=3, program_has_completed=True),
        ),
        # opcode 6 jump
        (
            dict(input_nums=[1106, 0, 4, 0, 99]),
            IntcodeOutput(nums=[1106, 0, 4, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # opcode 6 no jump
        (
            dict(input_nums=[1106, 1, 4, 99]),
            IntcodeOutput(nums=[1106, 1, 4, 99], outputs=[], instruction_pointer=3, program_has_completed=True),
        ),
        # opcode 7 store 1
        (
            dict(input_nums=[1107, 2, 3, 0, 99]),
            IntcodeOutput(nums=[1, 2, 3, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # opcode 7 store 0
        (
            dict(input_nums=[1107, 3, 2, 0, 99]),
            IntcodeOutput(nums=[0, 3, 2, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # opcode 8 store 1
        (
            dict(input_nums=[1108, 5, 5, 0, 99]),
            IntcodeOutput(nums=[1, 5, 5, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # opcode 8 store 0
        (
            dict(input_nums=[1108, 5, -3, 0, 99]),
            IntcodeOutput(nums=[0, 5, -3, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # position mode
        (
            dict(input_nums=[1101, 5, 6, 0, 99]),
            IntcodeOutput(nums=[11, 5, 6, 0, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        (
            dict(input_nums=[102, 5, 4, 3, 99]),
            IntcodeOutput(nums=[102, 5, 4, 495, 99], outputs=[], instruction_pointer=4, program_has_completed=True),
        ),
        # inputs and outputs
        (
            dict(input_nums=[3, 1, 4, 1, 99], input_values=[123]),
            IntcodeOutput(nums=[3, 123, 4, 1, 99], outputs=[123], instruction_pointer=4, program_has_completed=True),
        ),
        # p5 part 2 examples
        (
            dict(input_nums=[3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input_values=[8]),
            IntcodeOutput(
                nums=[3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8], outputs=[1], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input_values=[9]),
            IntcodeOutput(
                nums=[3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8], outputs=[0], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input_values=[5]),
            IntcodeOutput(
                nums=[3, 9, 7, 9, 10, 9, 4, 9, 99, 1, 8], outputs=[1], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input_values=[111]),
            IntcodeOutput(
                nums=[3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8], outputs=[0], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 3, 1108, -1, 8, 3, 4, 3, 99], input_values=[8]),
            IntcodeOutput(
                nums=[3, 3, 1108, 1, 8, 3, 4, 3, 99], outputs=[1], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 3, 1108, -1, 8, 3, 4, 3, 99], input_values=[-44]),
            IntcodeOutput(
                nums=[3, 3, 1108, 0, 8, 3, 4, 3, 99], outputs=[0], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 3, 1107, -1, 8, 3, 4, 3, 99], input_values=[1]),
            IntcodeOutput(
                nums=[3, 3, 1107, 1, 8, 3, 4, 3, 99], outputs=[1], instruction_pointer=8, program_has_completed=True
            ),
        ),
        (
            dict(input_nums=[3, 3, 1107, -1, 8, 3, 4, 3, 99], input_values=[11]),
            IntcodeOutput(
                nums=[3, 3, 1107, 0, 8, 3, 4, 3, 99], outputs=[0], instruction_pointer=8, program_has_completed=True
            ),
        ),
        # p5 part 2 jump tests
        (
            dict(input_nums=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input_values=[5]),
            IntcodeOutput(
                nums=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 5, 1, 1, 9],
                outputs=[1],
                instruction_pointer=11,
                program_has_completed=True,
            ),
        ),
        (
            dict(input_nums=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input_values=[0]),
            IntcodeOutput(
                nums=[3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 0, 0, 1, 9],
                outputs=[0],
                instruction_pointer=11,
                program_has_completed=True,
            ),
        ),
        (
            dict(input_nums=[3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input_values=[7]),
            IntcodeOutput(
                nums=[3, 3, 1105, 7, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
                outputs=[1],
                instruction_pointer=11,
                program_has_completed=True,
            ),
        ),
        (
            dict(input_nums=[3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input_values=[0]),
            IntcodeOutput(
                nums=[3, 3, 1105, 0, 9, 1101, 0, 0, 12, 4, 12, 99, 0],
                outputs=[0],
                instruction_pointer=11,
                program_has_completed=True,
            ),
        ),
    ),
)
def test_run_intcode(input_kwargs, expected_output):
    output = run_intcode(**input_kwargs)

    assert output == expected_output
