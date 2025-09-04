from copy import deepcopy


def run_opcode(nums: list[int]) -> list[int]:
    output = deepcopy(nums)
    position = 0

    while True:
        opcode = output[position]
        if opcode == 99:
            return output

        a = output[position + 1]
        b = output[position + 2]
        c = output[position + 3]

        x = output[a]
        y = output[b]

        if opcode == 1:
            new_num = x + y
        elif opcode == 2:
            new_num = x * y
        else:
            raise ValueError(opcode)

        output[c] = new_num
        position += 4


def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]
    nums[1] = 12
    nums[2] = 2

    output = run_opcode(nums)

    return output[0]
