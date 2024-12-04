from collections import Counter


def check_can_add_char(current_command: str, char: str) -> bool:
    if "mul(".startswith(current_command + char):
        return True

    if current_command.startswith("mul(") and char.isdigit():
        return True

    can_add_comma = (
        current_command.startswith("mul(")
        and len(current_command) > 4  # there is at least 1 digit after "("
        and Counter(current_command)[","] == 0  # no commas
    )
    if can_add_comma and char == ",":
        return True

    can_add_closing_bracket = (
        current_command.startswith("mul(")
        and len(current_command) >= 7  # there is at least "mul(x,y"
        and Counter(current_command)[","] == 1  # has one comma
        and current_command[-1].isdigit()  # ends with digit
    )
    if can_add_closing_bracket and char == ")":
        return True

    return False


def run(s: str) -> int:
    total = 0
    current_command = ""

    for char in s:
        if check_can_add_char(current_command, char):
            current_command += char
        else:
            current_command = ""

        is_end_of_command = current_command and current_command[-1] == ")"
        if is_end_of_command:
            num_part = current_command[4:-1]
            a, b = num_part.split(",")
            m = int(a) * int(b)
            total += m
            current_command = ""

    return total
