from .common import run_intcode


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]

    output = run_intcode(nums, input_values=[5])

    outputs = output.outputs
    assert len(outputs) == 1
    return outputs[0]
