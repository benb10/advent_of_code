from collections import Counter


def get_hand_type_score(cards: str) -> int:
    counter = Counter(cards)
    counts = sorted(counter.values())

    is_5oac = counts == [5]
    if is_5oac:
        return 7

    counter = Counter(cards)
    counts = sorted(list(counter.values()))
    is_4oac = counts == [1, 4]
    if is_4oac:
        return 6

    is_full_house = counts == [2, 3]
    if is_full_house:
        return 5

    is_3oac = counts == [1, 1, 3]
    if is_3oac:
        return 4

    is_two_pair = counts == [1, 2, 2]
    if is_two_pair:
        return 3

    is_one_pair = counts == [1, 1, 1, 2]
    if is_one_pair:
        return 2

    is_high_card = counts == [1, 1, 1, 1, 1]
    if is_high_card:
        return 1

    raise ValueError(cards)


def get_card_score(card: str) -> int:
    card_to_score = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    return card_to_score[card]


def get_hand_sort_key(hand: tuple[str, int]) -> tuple[int, ...]:
    cards, _ = hand
    hand_type_score = get_hand_type_score(cards)

    card_scores = [get_card_score(card) for card in cards]

    return hand_type_score, *card_scores


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]
    hands = []

    for line in lines:
        cards, num_str = line.split(" ")
        hands.append((cards, int(num_str)))

    hands.sort(key=get_hand_sort_key)
    print(hands)
    total = 0
    for i, (_, num) in enumerate(hands, 1):
        total += i * num

    return total
