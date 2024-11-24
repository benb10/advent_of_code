def fold_y(pts, y_fold):
    new_pts = set()
    for x, y in pts:
        if y < y_fold:
            y += 2 * abs(y - y_fold)
        new_pts.add((x, y))
    return sorted(new_pts)


def fold_x(pts, x_fold):
    new_pts = set()
    for x, y in pts:
        if x < x_fold:
            x += 2 * abs(x - x_fold)
        new_pts.add((x, y))
    return sorted(new_pts)


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    pts = s.split("fold")[0]

    pts = [[int(x) for x in y.split(",")] for y in pts.strip().split("\n")]

    fold = next(line for line in lines if line.startswith("fold"))
    type = "x" if "x" in fold else "y"
    fold = int(fold.split("=")[1])
    fn = fold_x if type == "x" else fold_y

    pts = fn(pts, fold)
    print(len(pts))
    return len(pts)
