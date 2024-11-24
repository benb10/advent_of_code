def run(s: str) -> int:
    nums = [int(x) for x in s.split(",")]

    for day in range(1, 81):
        new_nums = []

        for num in nums:
            if num == 0:
                new_nums.extend([6, 8])
            else:
                new_nums.append(num - 1)

        nums = new_nums

    return len(nums)
