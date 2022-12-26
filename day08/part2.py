import argparse
import pytest
import collections
import sys


def compute(data):

    max_scenic_score = float("-inf")

    coords = collections.defaultdict(lambda: sys.maxsize)
    lines = data.splitlines()

    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            coords[(x, y)] = int(num)

    for (x, y), num in tuple(coords.items()):
        if x == 0 or x == len(lines[0]) - 1 or y == 0 or y == len(lines) - 1:
            continue

        # check left
        trees_left = 0
        for i in range(x - 1, -1, -1):
            trees_left += 1
            if coords[i, y] >= num:
                break

        # check right
        trees_right = 0
        for i in range(x + 1, len(line)):
            trees_right += 1
            if coords[i, y] >= num:
                break

        # check up
        trees_up = 0
        for j in range(y - 1, -1, -1):
            trees_up += 1
            if coords[x, j] >= num:
                break

        # check down
        trees_down = 0
        for j in range(y + 1, len(lines)):
            trees_down += 1
            if coords[x, j] >= num:
                break

        scenic_score = trees_left * trees_right * trees_up * trees_down

        max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score


INPUT = """\
30373
25512
65332
33549
35390
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 8)])
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
