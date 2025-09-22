from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]

    output = run_intcode(nums, input_values=[1])

    outputs = output.outputs
    assert all(x == 0 for x in outputs[:-1])
    return outputs[-1]
