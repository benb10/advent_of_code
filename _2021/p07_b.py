from math import floor
from statistics import mean


def run(s: str) -> int:
    positions = [int(x) for x in s.strip().split(",")]
    starting_point = floor(mean(positions))

    meeting_point_to_fuel = {starting_point: get_total_fuel_cost(positions, starting_point)}
    choose_point_above = True

    while True:
        # check if we have found a minimum
        optimal_meeting_point = get_minimum_fuel_position(meeting_point_to_fuel)
        if optimal_meeting_point is not None:
            break

        if choose_point_above:
            new_point = max(meeting_point_to_fuel) + 1
        else:
            new_point = min(meeting_point_to_fuel) - 1

        meeting_point_to_fuel[new_point] = get_total_fuel_cost(positions, new_point)
        choose_point_above = not choose_point_above

    return get_total_fuel_cost(positions, optimal_meeting_point)


def get_minimum_fuel_position(meeting_point_to_fuel: dict[int, int]) -> int | None:
    min_position = min(meeting_point_to_fuel)
    max_position = max(meeting_point_to_fuel)

    valid_transitions = {
        (None, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
    }

    last_diff_sign = None
    minimum_fuel_position = None

    for position in range(min_position, max_position):
        cost = meeting_point_to_fuel[position]
        next_cost = meeting_point_to_fuel[position + 1]
        diff = next_cost - cost
        diff_sign = 0 if diff == 0 else diff / abs(diff)
        if diff_sign == last_diff_sign:
            continue

        transition = (last_diff_sign, diff_sign)
        if transition not in valid_transitions:
            return None

        if transition[0] == -1:
            minimum_fuel_position = position

        last_diff_sign = diff_sign

    if last_diff_sign != 1:
        return None

    return minimum_fuel_position


def get_total_fuel_cost(positions: list[int], meeting_point: int) -> int:
    return sum(get_fuel_cost(x, meeting_point) for x in positions)


def get_fuel_cost(position: int, destination: int) -> int:
    return get_tri_num(abs(destination - position))


def get_tri_num(n: int) -> int:
    return (n**2 + n) // 2
