import argparse
import pytest


def compute(data):

    overlaps = 0
    for line in data.splitlines():
        pair_1, pair_2 = line.split(",")
        pair_1_s, pair_1_e = pair_1.split("-")
        pair_2_s, pair_2_e = pair_2.split("-")

        if (
            int(pair_1_s) <= int(pair_2_s)
            and int(pair_1_e) >= int(pair_2_s)
            or int(pair_2_s) <= int(pair_1_s)
            and int(pair_2_e) >= int(pair_1_s)
        ):
            overlaps += 1

    return overlaps


INPUT = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 4)])
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
