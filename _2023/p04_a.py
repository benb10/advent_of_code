def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        number_part = line.split(":")[1]
        winning_nums_part, card_nums_part = number_part.split("|")
        winning_nums = [int(x) for x in winning_nums_part.strip().split(" ") if x]
        card_nums = [int(x) for x in card_nums_part.strip().split(" ") if x]
        num_matches = sum(1 for card_num in card_nums if card_num in winning_nums)
        if num_matches > 0:
            total += 2 ** (num_matches - 1)

    return total
