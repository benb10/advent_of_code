def run(s: str) -> int:
    nums = [int(x) for x in s.strip().split(",")]
    sorted_nums = sorted(nums)
    optimal_meeting_point = sorted_nums[len(sorted_nums) // 2]

    return sum(abs(num - optimal_meeting_point) for num in nums)
