def run(s: str) -> int:
    nums = [int(c) for c in s.strip()]

    offset = len(nums) // 2

    total = 0

    for i, num in enumerate(nums):
        next_index = (i + offset) % len(nums)
        next_num = nums[next_index]
        if num == next_num:
            total += num

    return total
