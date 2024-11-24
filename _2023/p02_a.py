def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    colour_to_max_num = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    total = 0

    for line in lines:
        game_title, reveals = line.split(": ")
        game_num = int(game_title.split(" ")[1])
        is_possible = True

        for reveal_str in reveals.split("; "):
            pairs = reveal_str.split(", ")
            for pair_str in pairs:
                num_str, colour = pair_str.split(" ")
                num = int(num_str)
                max_num = colour_to_max_num[colour]
                if num > max_num:
                    is_possible = False

        if is_possible:
            total += game_num

    return total
