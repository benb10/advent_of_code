def run(s: str) -> str:
    lines = [line.strip() for line in s.strip().split("\n")]

    programs = set()
    child_programs = set()

    for line in lines:
        words = line.split(" ")
        parent_program = words[0]
        programs.add(parent_program)
        child_programs.update(x.replace(",", "") for x in words[3:])

    bottom_programs = programs - child_programs
    assert len(bottom_programs) == 1
    return list(bottom_programs)[0]
