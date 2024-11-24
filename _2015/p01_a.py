def run(s: str) -> int:
    floor_num = 0
    for char in s:
        if char == "(":
            floor_num += 1
        elif char == ")":
            floor_num -= 1

    return floor_num
