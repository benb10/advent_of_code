from copy import deepcopy
from itertools import cycle, permutations

from .common import run_intcode


def run(s: str) -> int:
    init_nums = [int(x) for x in s.strip().split(",")]

    max_value = 0
    for phase_settings in permutations([5, 6, 7, 8, 9], 5):
        input_signal = 0
        amp_index_to_state = {}
        for i in range(5):
            amp_index_to_state[i] = (deepcopy(init_nums), 0)

        final_output = None

        for it_num, i in enumerate(cycle([0, 1, 2, 3, 4])):
            nums, instruction_pointer = amp_index_to_state[i]
            input_values = []

            if it_num < 5:
                input_values.append(phase_settings[i])

            if input_signal is not None:
                input_values.append(input_signal)

            output = run_intcode(
                nums,
                input_values=input_values,
                instruction_pointer=instruction_pointer,
                stop_after_n_outputs=1,
            )

            if output.outputs:
                assert len(output.outputs) == 1
                output_signal = output.outputs[0]
            else:
                output_signal = None

            amp_index_to_state[i] = (output.nums, output.instruction_pointer)
            if i == 4 and output_signal is not None:
                final_output = output_signal

            input_signal = output_signal

            if i == 4 and output.program_has_completed:
                break

        if final_output is not None and final_output > max_value:
            max_value = final_output

    return max_value
