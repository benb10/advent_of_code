def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    horizontal_position = 0
    depth = 0
    aim = 0

    for line in lines:
        instruction, x_str = line.split(" ")
        x = int(x_str)

        if instruction == "forward":
            horizontal_position += x
            depth += aim * x
        elif instruction == "down":
            aim += x
        elif instruction == "up":
            aim -= x
        else:
            raise ValueError(instruction)

    return horizontal_position * depth
