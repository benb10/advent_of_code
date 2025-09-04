def run(s: str) -> str:
    lines = [line.strip() for line in s.strip().split("\n")]

    r = 2
    c = 0

    num_pad = [
        "  1  ",
        " 234 ",
        "56789",
        " ABC ",
        "  D  ",
    ]
    chars = []

    for line in lines:
        for direction in line:
            new_r = r
            new_c = c
            if direction == "U":
                new_r -= 1
            elif direction == "R":
                new_c += 1
            elif direction == "D":
                new_r += 1
            elif direction == "L":
                new_c -= 1
            else:
                raise ValueError(direction)

            new_coords_are_valid = 0 <= new_r <= 4 and 0 <= new_c <= 4 and num_pad[new_r][new_c] != " "
            if new_coords_are_valid:
                r = new_r
                c = new_c

        char = num_pad[r][c]
        chars.append(char)

    return "".join(chars)
