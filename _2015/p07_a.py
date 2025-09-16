from copy import deepcopy


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    lines_to_process = deepcopy(lines)

    wire_to_value = {}

    while lines_to_process:
        processed_line_indices = set()

        for i, line in enumerate(lines_to_process):
            processed = process_line(line, wire_to_value)

            if processed:
                processed_line_indices.add(i)

        lines_to_process = [x for i, x in enumerate(lines_to_process) if i not in processed_line_indices]

    return wire_to_value["a"]


def process_line(line: str, wire_to_value: dict[str, int]) -> bool:
    lhs, wire = line.split(" -> ")

    if lhs.isdigit():
        wire_to_value[wire] = int(lhs)
        return True

    if " LSHIFT " in lhs or " RSHIFT " in lhs:
        input_expression, operation, num_str = lhs.split(" ")

        input_value = get_input_value(input_expression, wire_to_value)
        if input_value is None:
            return False

        num = int(num_str)

        if operation == "LSHIFT":
            output = input_value << num
        elif operation == "RSHIFT":
            output = input_value >> num
        else:
            raise ValueError(operation)

        wire_to_value[wire] = output
        return True

    if " AND " in lhs or " OR " in lhs:
        input_expression_1, operation, input_expression_2 = lhs.split(" ")

        input_value_1 = get_input_value(input_expression_1, wire_to_value)
        if input_value_1 is None:
            return False

        input_value_2 = get_input_value(input_expression_2, wire_to_value)
        if input_value_2 is None:
            return False

        if operation == "AND":
            output = input_value_1 & input_value_2
        elif operation == "OR":
            output = input_value_1 | input_value_2
        else:
            raise ValueError(operation)

        wire_to_value[wire] = output
        return True

    if lhs.startswith("NOT "):
        input_expression = lhs.removeprefix("NOT ")

        input_value = get_input_value(input_expression, wire_to_value)
        if input_value is None:
            return False

        output = (~input_value) % 2**16
        wire_to_value[wire] = output
        return True

    if lhs.isalpha():
        input_wire = lhs
        if input_wire not in wire_to_value:
            return False

        input_value = wire_to_value[input_wire]
        wire_to_value[wire] = input_value
        return True

    raise ValueError(f"unknown operation: {line}")


def get_input_value(input_expression: str, wire_to_value: dict[str, int]) -> int | None:
    if input_expression.isdigit():
        return int(input_expression)

    return wire_to_value.get(input_expression)
