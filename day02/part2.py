import argparse
import pytest


def compute(data):

    win_config = {
        "A": "B",
        "B": "C",
        "C": "A",
    }

    lose_config = {"A": "C", "B": "A", "C": "B"}

    selection_score = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    strategies = data.splitlines()

    score = 0

    for strategy in strategies:

        opp_choice, req_outcome = strategy.split(" ")

        if req_outcome == "X":  # lose
            my_choice = lose_config[opp_choice]
        if req_outcome == "Y":  # draw
            my_choice = opp_choice
            score += 3
        if req_outcome == "Z":  # win
            my_choice = win_config[opp_choice]
            score += 6

        score += selection_score[my_choice]

    return score


INPUT = """\
A Y
B X
C Z
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 12)])
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
