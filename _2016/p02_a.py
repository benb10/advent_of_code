def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    r = 1
    c = 1

    num_pad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    nums = []

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

            new_coords_are_valid = 0 <= new_r <= 2 and 0 <= new_c <= 2
            if new_coords_are_valid:
                r = new_r
                c = new_c

        num = num_pad[r][c]
        nums.append(num)

    return int("".join(str(num) for num in nums))
