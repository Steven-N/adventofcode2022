import argparse
import pytest


def alphabet_dict():

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    alphabet_dict = {}

    for idx, char in enumerate(alphabet, start=1):
        alphabet_dict[char] = idx

    return alphabet_dict


def compute(data):

    priorities = alphabet_dict()
    score = 0
    lines = data.splitlines()
    groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]  # noqa
    for group in groups:

        (difference,) = set(group[0]) & set(group[1]) & set(group[2])

        score += priorities[difference]

    return score


INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 70)])
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
