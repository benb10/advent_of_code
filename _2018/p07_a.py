from collections import defaultdict


def run(s: str) -> str:
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

    while steps_to_complete:
        available_steps = [
            step for step in steps_to_complete if all(x in completed_steps for x in step_to_prereqs[step])
        ]
        step = min(available_steps)
        completed_steps.append(step)
        steps_to_complete.remove(step)

    return "".join(completed_steps)
