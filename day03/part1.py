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
    for line in data.splitlines():
        bag_size = len(line) // 2

        comp_1, comp_2 = set(line[:bag_size]), set(line[bag_size:])

        (differences,) = comp_1.intersection(comp_2)
        score += priorities[differences]

    return score


INPUT = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 157)])
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
