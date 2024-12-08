import argparse
import re
from typing import List


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


def is_monotonic(sequence: List[int]) -> bool:
    if len(sequence) < 2:
        return True
    if sequence[0] == sequence[1]:
        return False
    is_ascending = sequence[0] < sequence[1]
    return all(
        (
            sequence[i] < sequence[i + 1]
            if is_ascending
            else sequence[i] > sequence[i + 1]
        )
        for i in range(len(sequence) - 1)
    )


def is_safe_report(report: List[int]) -> bool:
    if not is_monotonic(report):
        return False
    return all(1 <= abs(a - b) <= 3 for a, b in zip(report, report[1:]))


def part_one(input: List[str]) -> int:
    num_safe_reports = 0
    pattern = r"(\d+)"
    for line in input:
        match = re.findall(pattern, line)
        if match is None:
            print(f"No match found in line {line.strip()}")
            continue
        report = [int(x) for x in match]
        if is_safe_report(report):
            num_safe_reports += 1
    return num_safe_reports


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to input file")
    args = parser.parse_args()

    input = read_file_lines(args.filename)
    part_one_result = part_one(input)
    print(f"Part One: {part_one_result}")


if __name__ == "__main__":
    main()
