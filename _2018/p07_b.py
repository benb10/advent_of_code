from collections import defaultdict
from dataclasses import dataclass

NUM_WORKERS = 5
DURATION_OFFSET = 60


@dataclass
class Worker:
    current_step: str | None = None
    time_remaining: int = 0

    @property
    def is_available(self) -> bool:
        return self.current_step is None

    @property
    def is_busy(self) -> bool:
        return self.current_step is not None

    @property
    def is_finished(self) -> bool:
        return self.current_step and self.time_remaining == 0

    def unassign(self) -> None:
        if not self.is_finished:
            raise ValueError("Worker must be finished job to unassign")

        self.current_step = None
        self.time_remaining = 0

    def assign_job(self, step: str) -> None:
        if not self.is_available:
            raise ValueError("Not able to assign job when worker is busy")

        self.current_step = step
        self.time_remaining = get_step_duration(step)

    def go_forward_in_time(self, num_seconds: int) -> None:
        if num_seconds >= self.time_remaining:
            self.time_remaining = 0
        else:
            self.time_remaining -= num_seconds


def get_step_duration(step: str) -> int:
    return ord(step) - 64 + DURATION_OFFSET


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    step_to_prereqs: dict[str, list[str]] = defaultdict(list)
    steps = set()

    for line in lines:
        words = line.split(" ")
        step_1 = words[1]
        step_2 = words[7]
        step_to_prereqs[step_2].append(step_1)
        steps.add(step_1)
        steps.add(step_2)

    completed_steps = []
    steps_to_complete = list(steps)
    workers = [Worker() for _ in range(NUM_WORKERS)]
    num_seconds = 0

    while True:
        if not steps_to_complete and not any(x.is_busy for x in workers):
            break

        available_steps = sorted(
            step for step in steps_to_complete if all(x in completed_steps for x in step_to_prereqs[step])
        )
        available_workers = [x for x in workers if x.is_available]

        if available_steps and available_workers:
            time_jump = 0
        else:
            # jump ahead until a worker is free
            busy_workers = [x for x in workers if not x.is_available]
            min_time_rem = min(x.time_remaining for x in busy_workers)
            time_jump = min_time_rem

        num_seconds += time_jump

        for worker in workers:
            worker.go_forward_in_time(time_jump)

        # process finished jobs
        for worker in workers:
            if worker.is_finished:
                completed_steps.append(worker.current_step)
                worker.unassign()

        # assign new jobs to workers
        available_steps = sorted(
            step for step in steps_to_complete if all(x in completed_steps for x in step_to_prereqs[step])
        )
        available_workers = [x for x in workers if x.is_available]
        for worker in available_workers:
            if not available_steps:
                break
            step = available_steps.pop(0)
            steps_to_complete.remove(step)
            worker.assign_job(step)

    return num_seconds
