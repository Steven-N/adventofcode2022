import argparse
import pytest


def compute(data):

    elves = data.split("\n\n")

    elf_calories = {}

    for idx, elf in enumerate(elves):
        calories = elf.split("\n")
        elf_calories[idx] = sum(map(int, calories))

    top_3_calories = sum(sorted(elf_calories.values(), reverse=True)[:3])
    return top_3_calories


INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 45000)])
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
