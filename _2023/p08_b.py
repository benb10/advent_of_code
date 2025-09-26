from collections import defaultdict
from itertools import count, cycle


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    directions, _, *mappings = lines

    node_mappings = {}
    for line in mappings:
        lhs, rhs = line.split(" = ")
        a, b = rhs.replace("(", "").replace(")", "").split(", ")
        node_mappings[lhs] = (a, b)

    nodes = [node for node in node_mappings if node.endswith("A")]
    step_nums = [get_num_steps_to_z_node(node, directions, node_mappings) for node in nodes]
    return get_lcm(step_nums)


def get_num_steps_to_z_node(node: str, directions: str, node_mappings: dict[str, tuple[str, str]]) -> int:
    num_steps = 0

    for direction in cycle(directions):
        num_steps += 1
        i = {"L": 0, "R": 1}[direction]
        node = node_mappings[node][i]
        if node.endswith("Z"):
            break

    return num_steps


def get_lcm(nums: list[int]) -> int:
    pfs = [get_pf(num) for num in nums]
    prime_to_power = defaultdict(int)

    for pf in pfs:
        for prime, power in pf:
            if prime_to_power[prime] < power:
                prime_to_power[prime] = power

    lcm = 1
    for prime, power in prime_to_power.items():
        lcm *= prime**power

    return lcm


def get_pf(n: int) -> list[tuple[int, int]]:
    pf = []
    current_num = n

    for multiple in count(2):
        power = 0
        while current_num % multiple == 0:
            current_num //= multiple
            power += 1

        if power:
            pf.append((multiple, power))

        if current_num == 1:
            break

    return pf
