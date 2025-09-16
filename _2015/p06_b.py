from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    coords_to_brightness = defaultdict(int)

    for line in lines:
        words = line.split(" ")
        pair_1 = words[-3]
        pair_2 = words[-1]

        x_min, y_min = [int(x) for x in pair_1.split(",")]
        x_max, y_max = [int(x) for x in pair_2.split(",")]

        turn_on = line.startswith("turn on")
        turn_off = line.startswith("turn off")
        toggle = line.startswith("toggle")

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                if turn_on:
                    coords_to_brightness[(x, y)] += 1
                elif turn_off:
                    coords_to_brightness[(x, y)] = max(0, coords_to_brightness[(x, y)] - 1)
                elif toggle:
                    coords_to_brightness[(x, y)] += 2
                else:
                    raise ValueError("unknown action: {line}")

    return sum(brightness for brightness in coords_to_brightness.values())
