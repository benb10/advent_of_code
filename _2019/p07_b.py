from copy import deepcopy
from itertools import cycle, permutations

from .common import run_intcode


def run(s: str) -> int:
    init_nums = [int(x) for x in s.strip().split(",")]

    max_value = 0
    for phase_settings in permutations([5, 6, 7, 8, 9], 5):
        print(f"\n\n\n trying phase_settings {phase_settings}")
        input_signal = 0
        amp_index_to_state = {}
        for i in range(5):
            amp_index_to_state[i] = (deepcopy(init_nums), 0)

        for i in cycle([0, 1, 2, 3, 4]):
            print(f"\nRunning amp {i}")
            nums, instruction_pointer = amp_index_to_state[i]
            output = run_intcode(
                nums,
                input_values=[phase_settings[i], input_signal],
                instruction_pointer=instruction_pointer,
                stop_on_output=True,
                log=True,
            )

            amp_index_to_state[i] = (output.nums, output.instruction_pointer)
            if len(output.outputs) != 1:
                a = 0
            assert len(output.outputs) == 1
            input_signal = output.outputs[0]

            if i == 4 and output.program_has_completed:
                break

        if input_signal > max_value:
            max_value = input_signal

    return max_value


# s = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
#
# print(run(s))
