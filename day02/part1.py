import argparse
import pytest


def compute(data):

    choice_match = {"A": "X", "B": "Y", "C": "Z"}

    win_config = {"A": "Z", "B": "X", "C": "Y", "X": "C", "Y": "A", "Z": "B"}

    selection_score = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    strategies = data.splitlines()

    score = 0

    for strategy in strategies:

        opp_choice, my_choice = strategy.split(" ")
        score += selection_score[my_choice]

        if choice_match[opp_choice] == my_choice:  # Draw
            score += 3
        elif opp_choice == win_config[my_choice]:  # I win
            score += 6

    return score


INPUT = """\
A Y
B X
C Z
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 15)])
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
