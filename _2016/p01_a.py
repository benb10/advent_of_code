def turn(current_direction: str, side: str) -> str:
    if side == "L":
        return {"N": "W", "E": "N", "S": "E", "W": "S"}[current_direction]

    if side == "R":
        return {"N": "E", "E": "S", "S": "W", "W": "N"}[current_direction]

    raise ValueError(f"Unknown side: {side}")


def run(s: str) -> int:
    directions = [x.strip() for x in s.split(",")]

    x = 0
    y = 0
    current_direction = "N"

    for direction in directions:
        side = direction[0]
        distance = int(direction[1:])
        current_direction = turn(current_direction, side)
        if current_direction == "N":
            y += distance
        elif current_direction == "E":
            x += distance
        elif current_direction == "S":
            y -= distance
        elif current_direction == "W":
            x -= distance

    return abs(x) + abs(y)
