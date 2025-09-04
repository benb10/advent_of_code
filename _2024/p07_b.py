def check_has_solution(result: int, nums: list[int]) -> bool:
    possible_answers = {nums[0]}

    functions = [
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: int(str(a) + str(b)),
    ]

    for num in nums[1:]:
        new_possible_answers = set()
        for possible_answer in possible_answers:
            for function in functions:
                answer = function(possible_answer, num)
                new_possible_answers.add(answer)
        possible_answers = new_possible_answers

    return result in possible_answers


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0
    for line in lines:
        result_part, nums_part = line.split(":")
        result = int(result_part)
        nums = [int(x) for x in nums_part.strip().split(" ")]
        if check_has_solution(result, nums):
            total += result

    return total
