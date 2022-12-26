import argparse
import pytest


def build_tree(data):

    directories = {"/": set()}
    directory_sizes = {"/": 0}

    cwd = []
    for line in data.splitlines():
        split_line = line.split()
        if split_line[0] == "$":
            if split_line[1] == "cd":
                directory = split_line[2]
                if directory != "..":
                    cwd.append(directory)
                    full_path = "/".join(cwd)
                    if full_path not in directories:
                        directories[full_path] = set()
                    if full_path not in directory_sizes:
                        directory_sizes[full_path] = 0
                else:
                    cwd.pop()
            elif split_line[1] == "ls":
                continue
        else:
            full_path = "/".join(cwd)
            directories[full_path].add(split_line[1])
            if split_line[0] != "dir":
                file_size = int(split_line[0])
                for i in range(len(cwd)):
                    dir_to_update = "/".join(cwd[0 : i + 1])  # noqa
                    directory_sizes[dir_to_update] += file_size

    return directories, directory_sizes


def compute(data):

    _, directory_sizes = build_tree(data)

    result = 0
    for _, size in directory_sizes.items():
        if size <= 100000:
            result += size

    return result


INPUT = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 95437)])
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
