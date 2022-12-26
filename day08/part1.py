import argparse
import pytest
import collections
import sys


def compute(data):

    visible_trees = 0

    coords = collections.defaultdict(lambda: sys.maxsize)
    lines = data.splitlines()

    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            coords[(x, y)] = int(num)

    for (x, y), num in tuple(coords.items()):
        if x == 0 or x == len(lines[0]) - 1 or y == 0 or y == len(lines) - 1:
            visible_trees += 1
            continue

        # check left
        for i in range(0, x):
            if coords[i, y] >= num:
                break
        else:
            visible_trees += 1
            continue

        # check right
        for i in range(x + 1, len(line)):
            if coords[i, y] >= num:
                break
        else:
            visible_trees += 1
            continue

        # check up
        for j in range(0, y):
            if coords[x, j] >= num:
                break
        else:
            visible_trees += 1
            continue

        # check down
        for j in range(y + 1, len(lines)):
            if coords[x, j] >= num:
                break
        else:
            visible_trees += 1
            continue

    return visible_trees


INPUT = """\
30373
25512
65332
33549
35390
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 21)])
def test(test_input, expected):
    assert compute(test_input) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read()))


if __name__ == "__main__":
    exit(main())
