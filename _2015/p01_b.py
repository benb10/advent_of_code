def run(s: str) -> int:
    floor_num = 0
    for i, char in enumerate(s):
        if char == "(":
            floor_num += 1
        elif char == ")":
            floor_num -= 1

        if floor_num == -1:
            return i + 1
