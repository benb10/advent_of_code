def run(s: str) -> int:
    directions = s.strip()

    coords_visited = {(0, 0)}
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0

    for i, direction in enumerate(directions):
        dx = 0
        dy = 0

        if direction == "^":
            dy = 1
        elif direction == ">":
            dx = 1
        elif direction == "v":
            dy = -1
        elif direction == "<":
            dx = -1
        else:
            raise ValueError(direction)

        santas_move = i % 2 == 1

        if santas_move:
            santa_x += dx
            santa_y += dy
            coords_visited.add((santa_x, santa_y))
        else:
            robo_x += dx
            robo_y += dy
            coords_visited.add((robo_x, robo_y))

    return len(coords_visited)
