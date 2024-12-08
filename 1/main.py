import argparse
import re
from collections import Counter
from typing import List, Tuple


def read_file_lines(filename: str) -> List[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: the file {filename} was not found")
        exit(1)
    except IOError as e:
        print(f"Error: An I/O error occurred while reading the file: {e}")
        exit(1)


def parse_file_lines(input: List[str]) -> Tuple[List[str], List[str]]:
    line_split_regex = r"(\d{5})\s+(\d{5})"
    left, right = [], []
    for line in input:
        match = re.search(line_split_regex, line)
        if match:
            left.append(match[1])
            right.append(match[2])
    return left, right


def part_one(left, right):
    left.sort()
    right.sort()
    return sum(abs(int(l) - int(r)) for l, r in zip(left, right))


def part_two(left, right):
    right_counter = Counter(right)
    similarity_score = sum(
        int(l) * right_counter[l] for l in left if l in right_counter
    )
    return similarity_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to input file")
    args = parser.parse_args()

    input = read_file_lines(args.filename)
    left, right = parse_file_lines(input)

    part_one_result = part_one(left, right)
    part_two_result = part_two(left, right)
    print(f"Part One: {part_one_result}\nPart Two: {part_two_result}")


if __name__ == "__main__":
    main()
