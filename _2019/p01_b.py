def get_single_fuel(n):
    return n // 3 - 2


def get_fuel_req(n):
    fuel_sum = 0

    while True:
        sf = get_single_fuel(n)
        if sf <= 0:
            break
        fuel_sum += sf
        n = sf

    return fuel_sum


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    nums = [int(line) for line in lines]
    fuel_reqs = [get_fuel_req(n) for n in nums]
    return sum(fuel_reqs)
