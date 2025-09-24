from copy import deepcopy
from dataclasses import dataclass


@dataclass
class IntcodeOutput:
    nums: list[int]
    outputs: list[int]
    instruction_pointer: int
    relative_base: int
    program_has_completed: bool


def run_intcode(
    input_nums: list[int],
    input_values: list[int] | None = None,
    instruction_pointer: int = 0,
    relative_base: int = 0,
    stop_after_n_outputs: int | None = None,
    stop_when_input_required: bool = False,
    log: bool = False,
) -> IntcodeOutput:
    def _log(s):
        if log:
            print(s)

    inputs = [] if input_values is None else deepcopy(input_values)

    nums = deepcopy(input_nums)
    outputs = []

    while True:
        num_str = str(nums[instruction_pointer]).zfill(5)
        param_3_mode = int(num_str[0])
        param_2_mode = int(num_str[1])
        param_1_mode = int(num_str[2])
        opcode = int(num_str[3:])
        _log(f"At {instruction_pointer}, num={num_str}, opcode={opcode}")

        if opcode == 99:
            return IntcodeOutput(
                nums=nums,
                outputs=outputs,
                instruction_pointer=instruction_pointer,
                relative_base=relative_base,
                program_has_completed=True,
            )

        if opcode in [1, 2]:
            param_1 = get_param(nums, instruction_pointer + 1, param_1_mode, relative_base)
            param_2 = get_param(nums, instruction_pointer + 2, param_2_mode, relative_base)
            param_3_addr = get_address_param(nums, instruction_pointer + 3, param_3_mode, relative_base)

            result = param_1 + param_2 if opcode == 1 else param_1 * param_2
            _log(f"    setting addr {param_3_addr} to {result}")
            make_address_available(nums, address=param_3_addr)
            nums[param_3_addr] = result
            instruction_pointer += 4

        elif opcode == 3:
            param_1_addr = get_address_param(nums, instruction_pointer + 1, param_1_mode, relative_base)

            if not inputs:
                if stop_when_input_required:
                    return IntcodeOutput(
                        nums=nums,
                        outputs=outputs,
                        instruction_pointer=instruction_pointer,
                        relative_base=relative_base,
                        program_has_completed=False,
                    )
                else:
                    raise ValueError("Ran out of input_values")

            input_value = inputs.pop(0)
            _log(f"    setting addr {param_1_addr} to {input_value}")
            make_address_available(nums, address=param_1_addr)
            nums[param_1_addr] = input_value
            instruction_pointer += 2

        elif opcode == 4:
            param_1 = get_param(nums, instruction_pointer + 1, param_1_mode, relative_base)

            _log(f"    adding {param_1} to outputs")
            outputs.append(param_1)
            instruction_pointer += 2
            if stop_after_n_outputs is not None and len(outputs) >= stop_after_n_outputs:
                return IntcodeOutput(
                    nums=nums,
                    outputs=outputs,
                    instruction_pointer=instruction_pointer,
                    relative_base=relative_base,
                    program_has_completed=False,
                )

        elif opcode in [5, 6]:
            param_1 = get_param(nums, instruction_pointer + 1, param_1_mode, relative_base)
            param_2 = get_param(nums, instruction_pointer + 2, param_2_mode, relative_base)

            # jump-if-true + jump-if-false
            should_jump = (opcode == 5 and param_1 != 0) or (opcode == 6 and param_1 == 0)

            if should_jump:
                _log(f"    changing ip to {param_2}")
                instruction_pointer = param_2
            else:
                _log("    no jump")
                instruction_pointer += 3

        elif opcode in [7, 8]:
            param_1 = get_param(nums, instruction_pointer + 1, param_1_mode, relative_base)
            param_2 = get_param(nums, instruction_pointer + 2, param_2_mode, relative_base)
            param_3_addr = get_address_param(nums, instruction_pointer + 3, param_3_mode, relative_base)

            # less than + equals
            condition = param_1 < param_2 if opcode == 7 else param_1 == param_2
            num_to_store = 1 if condition else 0

            _log(f"    setting addr {param_3_addr} to {num_to_store}")
            make_address_available(nums, address=param_3_addr)
            nums[param_3_addr] = num_to_store

            instruction_pointer += 4

        elif opcode == 9:
            param_1 = get_param(nums, instruction_pointer + 1, param_1_mode, relative_base)

            relative_base += param_1
            _log(f"    changing relative_base to {relative_base}")
            instruction_pointer += 2

        else:
            raise ValueError(f"Unknown opcode: {opcode}")


def get_param(nums: list[int], index: int, mode: int, relative_base: int) -> int | None:
    value_at_position = nums[index]

    if mode == 1:
        return value_at_position

    if mode == 0:
        if value_at_position < 0:
            raise ValueError(f"Error for param mode 0: {value_at_position}")

        if value_at_position >= len(nums):
            return 0

        return nums[value_at_position]

    if mode == 2:
        target_index = relative_base + value_at_position
        if target_index < 0:
            raise ValueError(f"Error for param mode 2: {target_index}")

        if target_index >= len(nums):
            return 0

        return nums[target_index]

    raise ValueError(f"unknown mode: {mode}")


def get_address_param(nums: list[int], index: int, mode: int, relative_base: int) -> int:
    value_at_position = nums[index]

    if mode == 1:
        raise ValueError("Parameters that an instruction writes to should never be in immediate mode.")

    if mode == 0:
        return value_at_position

    if mode == 2:
        return relative_base + value_at_position

    raise ValueError(f"unknown mode: {mode}")


def make_address_available(nums: list[int], address: int) -> None:
    if address >= len(nums):
        # we need to extend with zeros
        shortfall = address - len(nums) + 1
        nums.extend([0] * shortfall)
