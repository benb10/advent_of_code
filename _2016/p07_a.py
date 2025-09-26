def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        line_is_abba = False

        in_sq_brackets = False
        for i in range(len(line)):
            char = line[i]

            if char == "[":
                in_sq_brackets = True

            if char == "]":
                in_sq_brackets = False

            sub_str = line[i : i + 4]
            if len(sub_str) != 4:
                continue
            if not sub_str.isalpha():
                continue

            is_abba = sub_str == sub_str[::-1] and sub_str[0] != sub_str[1]
            if is_abba:
                if in_sq_brackets:
                    line_is_abba = False
                    break
                else:
                    line_is_abba = True

        if line_is_abba:
            total += 1

    return total
