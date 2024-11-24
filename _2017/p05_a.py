def clean_input(i):
    return [int(x) for x in i.strip().split("\n")]


def print_status(nums, position):
    strs = [f"({num})" if i == position else f" {num} " for i, num in enumerate(nums)]
    print("".join(strs))


def get_num_steps(nums):
    position = 0
    num_steps = 0
    print_status(nums, position)

    while True:
        if position >= len(nums):
            break

        distance_to_move = nums[position]
        nums[position] += 1
        position += distance_to_move
        num_steps += 1

        # print_status(nums, position)

    print(num_steps)
    return num_steps


def run(s: str) -> int:
    nums = clean_input(s)

    return get_num_steps(nums)
