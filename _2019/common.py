from copy import deepcopy


def run_intcode(
    input_nums: list[int],
    input_value: int | None = None,
    return_outputs: bool = False,
) -> list[int] | tuple[list[int], list[int]]:
    nums = deepcopy(input_nums)
    outputs = []
    instruction_pointer = 0
    log = False

    while True:
        num_str = str(nums[instruction_pointer]).zfill(5)
        param_3_mode = int(num_str[0])
        param_2_mode = int(num_str[1])
        param_1_mode = int(num_str[2])
        opcode = int(num_str[3:])
        if log:
            print(f"At {instruction_pointer}, opcode={opcode}")

        if param_3_mode == 1:
            raise ValueError("Parameters that an instruction writes to should never be in immediate mode.")

        if opcode == 99:
            if return_outputs:
                return nums, outputs
            return nums

        value_at_param_1, param_1 = get_param(nums, instruction_pointer + 1, param_1_mode)
        value_at_param_2, param_2 = get_param(nums, instruction_pointer + 2, param_2_mode)
        value_at_param_3, param_3 = get_param(nums, instruction_pointer + 3, param_3_mode)

        if opcode in [1, 2]:
            result = param_1 + param_2 if opcode == 1 else param_1 * param_2
            if log:
                print(f"    setting pos {value_at_param_3} to {result}")
            nums[value_at_param_3] = result
            instruction_pointer += 4

        elif opcode == 3:
            if log:
                print(f"    setting pos {value_at_param_1} to {input_value}")
            nums[value_at_param_1] = input_value
            instruction_pointer += 2

        elif opcode == 4:
            if log:
                print(f"    adding {param_1} to outputs")
            outputs.append(param_1)
            print(outputs)
            instruction_pointer += 2

        elif opcode in [5, 6]:
            # jump-if-true + jump-if-false
            should_jump = (opcode == 5 and param_1 != 0) or (opcode == 6 and param_1 == 0)

            if should_jump:
                if log:
                    print(f"    changing ip to {param_2}")
                instruction_pointer = param_2
            else:
                instruction_pointer += 3

        elif opcode in [7, 8]:
            # less than + equals
            condition = param_1 < param_2 if opcode == 7 else param_1 == param_2
            num_to_store = 1 if condition else 0

            if log:
                print(f"    saving {num_to_store} to pos {value_at_param_3}")
            nums[value_at_param_3] = num_to_store

            instruction_pointer += 4

        else:
            raise ValueError(f"Unknown opcode: {opcode}")


def get_param(nums: list[int], index: int, mode: int) -> tuple[int | None, int | None]:
    if not (0 <= index < len(nums)):
        return None, None

    value_at_position = nums[index]

    if mode == 1:
        return value_at_position, value_at_position

    if mode == 0:
        if not (0 <= value_at_position < len(nums)):
            return value_at_position, None
        return value_at_position, nums[value_at_position]

    raise ValueError(f"unknown mode: {mode}")
