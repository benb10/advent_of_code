def get_fuel_req(x, locations):
    return sum(abs(x - location) for location in locations)


def run(s: str) -> int:
    locations = [int(x) for x in s.split(",")]

    min_location = min(locations)
    max_location = max(locations)

    position_to_fuel = {}

    for x in range(min_location, max_location + 1):
        fuel_req = get_fuel_req(x, locations)

        position_to_fuel[x] = fuel_req

    optimal_location = min(position_to_fuel.items(), key=lambda p: p[1])

    return optimal_location[1]
