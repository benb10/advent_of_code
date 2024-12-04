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
    visited_coords = {(0, 0)}

    for direction in directions:
        side = direction[0]
        distance = int(direction[1:])
        current_direction = turn(current_direction, side)
        if current_direction == "N":
            new_coords = [(x, y + i) for i in range(1, distance + 1)]
            y += distance

        elif current_direction == "E":
            new_coords = [(x + i, y) for i in range(1, distance + 1)]
            x += distance

        elif current_direction == "S":
            new_coords = [(x, y - i) for i in range(1, distance + 1)]
            y -= distance

        elif current_direction == "W":
            new_coords = [(x - i, y) for i in range(1, distance + 1)]
            x -= distance

        for new_coord in new_coords:
            if new_coord in visited_coords:
                new_x, new_y = new_coord
                return abs(new_x) + abs(new_y)

            visited_coords.add(new_coord)
