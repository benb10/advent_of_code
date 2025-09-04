def get_outcome_score(opponent_hand: str, my_hand: str) -> int:
    if opponent_hand == my_hand:
        # draw
        return 3

    hands = sorted([opponent_hand, my_hand])

    if hands == ["paper", "rock"]:
        return 6 if my_hand == "paper" else 0

    if hands == ["paper", "scissors"]:
        return 6 if my_hand == "scissors" else 0

    if hands == ["rock", "scissors"]:
        return 6 if my_hand == "rock" else 0

    raise ValueError(hands)


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        opponent_char, my_char = line.split(" ")
        opponent_hand = {"A": "rock", "B": "paper", "C": "scissors"}[opponent_char]
        my_hand = {"X": "rock", "Y": "paper", "Z": "scissors"}[my_char]

        hand_score = {"X": 1, "Y": 2, "Z": 3}[my_char]
        outcome_score = get_outcome_score(opponent_hand, my_hand)
        total += hand_score + outcome_score

    return total
