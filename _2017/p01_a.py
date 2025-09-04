def run(s: str) -> int:
    nums = [int(c) for c in s.strip()]

    total = 0

    for i, num in enumerate(nums):
        next_index = (i + 1) % len(nums)
        next_num = nums[next_index]
        if num == next_num:
            total += num

    return total
