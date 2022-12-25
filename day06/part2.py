import argparse
import pytest


def compute(data):

    distinct_count = 14

    for i in range(len(data)):
        marker = data[i : i + distinct_count]  # noqa
        if len(set(marker)) == distinct_count:
            return i + distinct_count


INPUT = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 19)])
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
