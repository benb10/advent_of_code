def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    total = 0

    for line in lines:
        game_title, reveals = line.split(": ")

        colour_to_min_num = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for reveal_str in reveals.split("; "):
            pairs = reveal_str.split(", ")
            for pair_str in pairs:
                num_str, colour = pair_str.split(" ")
                num = int(num_str)
                colour_to_min_num[colour] = max(colour_to_min_num[colour], num)

        min_nums = colour_to_min_num.values()
        p = 1
        for min_num in min_nums:
            p *= min_num
        total += p

    return total
