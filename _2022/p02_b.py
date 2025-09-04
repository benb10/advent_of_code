def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    total = 0

    for line in lines:
        opponent_char, my_char = line.split(" ")
        desired_outcome = {"X": "lose", "Y": "draw", "Z": "win"}[my_char]
        opponent_hand = {"A": "rock", "B": "paper", "C": "scissors"}[opponent_char]

        hand_winner_to_loser = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        hand_loser_to_winner = {v: k for k, v in hand_winner_to_loser.items()}

        if desired_outcome == "lose":
            my_hand = hand_winner_to_loser[opponent_hand]
        elif desired_outcome == "draw":
            my_hand = opponent_hand
        elif desired_outcome == "win":
            my_hand = hand_loser_to_winner[opponent_hand]
        else:
            raise ValueError(desired_outcome)

        hand_score = {"rock": 1, "paper": 2, "scissors": 3}[my_hand]
        outcome_score = {"lose": 0, "draw": 3, "win": 6}[desired_outcome]
        total += hand_score + outcome_score

    return total
