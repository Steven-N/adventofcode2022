import argparse
import pytest
import re


def parse_input(crates):

    stacks = {}
    pattern = r"\[[A-Z]\]"
    for line in crates.splitlines():
        containers = [line[i : i + 4].strip() for i in range(0, len(line), 4)]  # noqa
        for idx, container in enumerate(containers, start=1):
            if idx not in stacks:
                stacks[idx] = []
            if re.search(pattern, container):
                stacks[idx].append(container[1])

    return stacks


def compute(data):

    crates, moves = data.split("\n\n")
    stacks = parse_input(crates)

    result = ""
    pattern_move = r"move \d+"
    pattern_from = r"from \d+"
    pattern_to = r"to \d+"
    for move in moves.splitlines():
        crates_to_move = int(re.search(pattern_move, move)[0].split()[1])
        stack_start = int(re.search(pattern_from, move)[0].split()[1])
        stack_end = int(re.search(pattern_to, move)[0].split()[1])

        for _ in range(crates_to_move):
            if len(stacks[stack_start]) > 0:
                crate = stacks[stack_start].pop(0)
                stacks[stack_end].insert(0, crate)

    for _, stack in stacks.items():
        if len(stack) > 0:
            result += stack[0]

    return result


INPUT = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, "CMZ")])
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
