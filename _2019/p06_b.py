from collections import defaultdict


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    planet_to_neighbours = defaultdict(set)
    planet_to_orbit = {}

    for line in lines:
        big_planet, small_planet = line.split(")")
        planet_to_neighbours[small_planet].add(big_planet)
        planet_to_neighbours[big_planet].add(small_planet)
        planet_to_orbit[small_planet] = big_planet

    start_planet = planet_to_orbit["YOU"]
    end_planet = planet_to_orbit["SAN"]

    routes = [(start_planet,)]
    seen_planets = {start_planet}

    while True:
        new_routes = []

        for route in routes:
            current_planet = route[-1]
            for next_planet in planet_to_neighbours[current_planet]:
                if next_planet in seen_planets:
                    continue  # no backtracking

                new_route = route + (next_planet,)
                if next_planet == end_planet:
                    return len(new_route) - 1
                new_routes.append(new_route)
                seen_planets.add(next_planet)

        routes = new_routes
