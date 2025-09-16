def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    planet_to_orbit = {}

    for line in lines:
        big_planet, small_planet = line.split(")")
        planet_to_orbit[small_planet] = big_planet

    all_orbits = set()

    for base_planet in planet_to_orbit:
        planet = base_planet

        while planet != "COM":
            planet = planet_to_orbit[planet]
            all_orbits.add((base_planet, planet))

    return len(all_orbits)
