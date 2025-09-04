def run(s: str) -> int:
    directions = s.strip()

    coords_visited = {(0, 0)}
    current_x = 0
    current_y = 0

    for direction in directions:
        if direction == "^":
            current_y += 1
        elif direction == ">":
            current_x += 1
        elif direction == "v":
            current_y -= 1
        elif direction == "<":
            current_x -= 1
        else:
            raise ValueError(direction)

        coords_visited.add((current_x, current_y))

    return len(coords_visited)
