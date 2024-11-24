def fold_y(pts, y_fold):
    new_pts = set()
    for x, y in pts:
        if y > y_fold:
            y -= 2 * abs(y - y_fold)
        new_pts.add((x, y))
    return sorted(new_pts)


def fold_x(pts, x_fold):
    new_pts = set()
    for x, y in pts:
        if x > x_fold:
            x -= 2 * abs(x - x_fold)
        new_pts.add((x, y))
    return sorted(new_pts)


def get_pp_str(pts, max_size):
    xs = [pt[0] for pt in pts]
    ys = [pt[1] for pt in pts]
    x_min = min(xs)
    x_max = min(max(xs), x_min + max_size)
    y_min = min(ys)
    y_max = min(max(ys), y_min + max_size)

    pts = set(pts)
    output = ""

    for y in range(y_min, y_max + 1):
        x_vals = ["#" if (x, y) in pts else "." for x in range(x_min, x_max + 1)]
        output += "".join(x_vals) + "\n"

    return output


def pp(pts, max_size):
    print(get_pp_str(pts, max_size))


def run(s: str) -> int:
    lines = [line.strip() for line in s.strip().split("\n")]

    pts = s.split("fold")[0]

    pts = [tuple(int(x) for x in y.split(",")) for y in pts.strip().split("\n")]
    pp(pts, 100)

    folds = [line for line in lines if line.startswith("fold")]

    for fold in folds:
        type = "x" if "x" in fold else "y"
        fold = int(fold.split("=")[1])
        fn = fold_x if type == "x" else fold_y
        pts = fn(pts, fold)
        print(len(pts))
        pp(pts, 1000)

    return get_pp_str(pts, 1000)
