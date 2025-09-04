from itertools import permutations


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        line = line.replace("\t", " ")
        nums = [int(x) for x in line.split(" ")]
        checksum = None

        for num_1, num_2 in permutations(nums, 2):
            if num_1 % num_2 == 0:
                checksum = num_1 // num_2
                break

        if checksum is None:
            raise ValueError(f"Could not find checksum for {line}")

        total += checksum

    return total
