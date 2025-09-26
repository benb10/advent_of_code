from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    register_to_value = defaultdict(int)

    for line in lines:
        register, operation, x_str, _if, condition_register, condition, compare_value_str = line.split(" ")

        compare_value = int(compare_value_str)
        condition_result = check_condition(register_to_value[condition_register], condition, compare_value)
        if not condition_result:
            continue

        x = int(x_str)
        if operation == "inc":
            register_to_value[register] += x
        elif operation == "dec":
            register_to_value[register] -= x
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return max(register_to_value.values())


def check_condition(value: int, condition: str, compare_value: int) -> bool:
    condition_to_fn = {
        "<": lambda a, b: a < b,
        ">": lambda a, b: a > b,
        "<=": lambda a, b: a <= b,
        ">=": lambda a, b: a >= b,
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
    }
    fn = condition_to_fn.get(condition)
    if fn is None:
        raise ValueError(f"Unknown condition: {condition}")

    return fn(value, compare_value)
