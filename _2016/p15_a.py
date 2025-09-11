from dataclasses import dataclass


@dataclass
class Disc:
    num_positions: int
    initial_position: int

    def capsule_will_pass(self, num_seconds: int) -> bool:
        return (self.initial_position + num_seconds) % self.num_positions == 0


def run(s: str) -> int | None:
    discs = []

    for line in s.strip().split("\n"):
        num_positions = int(line.split(" positions; ")[0].split(" ")[-1])
        initial_position = int(line.split(" ")[-1].replace(".", ""))

        disc = Disc(
            num_positions=num_positions,
            initial_position=initial_position,
        )

        discs.append(disc)

    initial_drop_time, interval = get_times_for_biggest_disc(discs)

    drop_time = initial_drop_time
    while True:
        capsule_passes_through = check_capsule_passes_through(drop_time, discs)
        if capsule_passes_through:
            return drop_time
        drop_time += interval


def check_capsule_passes_through(drop_time: int, discs: list[Disc]) -> bool:
    for i, disc in enumerate(discs):
        num_seconds = drop_time + i + 1
        capsule_will_pass = disc.capsule_will_pass(num_seconds)
        if not capsule_will_pass:
            return False

    return True


def get_times_for_biggest_disc(discs: list[Disc]) -> tuple[int, int]:
    biggest_disc_i, biggest_disc = max(enumerate(discs), key=lambda x: x[1].num_positions)

    n = 1
    while True:
        elapsed_time = biggest_disc.num_positions * n - biggest_disc.initial_position
        delay = biggest_disc_i + 1
        if elapsed_time >= delay:
            return elapsed_time - delay, biggest_disc.num_positions
        n += 1
