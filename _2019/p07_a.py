from copy import deepcopy
from itertools import permutations

from .common import run_intcode


def run(s: str) -> int:
    init_nums = [int(x) for x in s.strip().split(",")]

    max_value = 0
    for phase_settings in permutations([0, 1, 2, 3, 4], 5):
        nums = deepcopy(init_nums)
        input_signal = 0
        for i in range(5):
            input_values = [phase_settings[i], input_signal]
            output = run_intcode(nums, input_values=input_values)
            outputs = output.outputs
            nums = output.nums

            assert len(outputs) == 1
            input_signal = outputs[0]

        if input_signal > max_value:
            max_value = input_signal

    return max_value
