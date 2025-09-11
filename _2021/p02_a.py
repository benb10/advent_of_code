def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    horizontal_position = 0
    depth = 0

    for line in lines:
        instruction, distance_str = line.split(" ")
        distance = int(distance_str)

        if instruction == "forward":
            horizontal_position += distance
        elif instruction == "down":
            depth += distance
        elif instruction == "up":
            depth -= distance
        else:
            raise ValueError(instruction)

    return horizontal_position * depth
