def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    original_num_cards = len(lines)
    card_num_to_count = {i: 1 for i in range(1, original_num_cards + 1)}

    for line in lines:
        start, number_part = line.split(":")
        card_num = int(start.replace("Card ", ""))
        winning_nums_part, card_nums_part = number_part.split("|")
        winning_nums = [int(x) for x in winning_nums_part.strip().split(" ") if x]
        card_nums = [int(x) for x in card_nums_part.strip().split(" ") if x]
        num_matches = sum(1 for card_num in card_nums if card_num in winning_nums)

        if num_matches > 0:
            next_card_num = card_num + 1
            card_nums_won = range(next_card_num, next_card_num + num_matches)
            for card_num_won in card_nums_won:
                card_num_to_count[card_num_won] += card_num_to_count[card_num]

    return sum(card_num_to_count.values())
