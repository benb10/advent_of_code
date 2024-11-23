from typing import List


class Disc:
    def __init__(self, num_positions, inital_position):
        self.num_positions = num_positions
        self.inital_position = inital_position

    def ball_will_pass(self, time: int) -> bool:
        return (self.inital_position + time) % self.num_positions == 0


def drop_ball(drop_time: int, discs: List[Disc]) -> None:
    for i, disc in enumerate(discs):
        time = drop_time + i + 1

        if disc.ball_will_pass(time):
            continue
        else:
            # ball has bounced off
            return

    print(f"Ball has passed all the way through!  drop_time {drop_time}")


def run(s: str) -> int:
    discs = []

    for line in s.strip().split("\n"):
        num_positions = int(line.split(" positions; ")[0].split(" ")[-1])
        inital_position = int(line.split(" ")[-1].replace(".", ""))

        disc = Disc(
            num_positions=num_positions,
            inital_position=inital_position,
        )

        discs.append(disc)

    for time in range(100):
        drop_ball(time, discs)

    return 0
