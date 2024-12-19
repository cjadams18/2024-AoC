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


def part_one(input: List[str]) -> int:
    total = 0
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in input:
        match = re.findall(pattern, line)
        if match is None:
            print(f"No match found in line: {line.split()}")
            continue
        for i in match:
            x, y = i
            total += int(x) * int(y)
    return total


def part_two(input: List[str]) -> int:
    total = 0
    valid_section = True
    for line in input:
        sections = re.split(r"(do\(\)|don't\(\))", line)
        for section in sections:
            if section == "do()":
                valid_section = True
            elif section == "don't()":
                valid_section = False
            elif valid_section:
                matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", section)
                for x, y in matches:
                    total += int(x) * int(y)
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to input file")
    args = parser.parse_args()

    input = read_file_lines(args.filename)
    part_one_result = part_one(input)
    part_two_result = part_two(input)
    print(f"Part One: {part_one_result}\nPart Two: {part_two_result}")


if __name__ == "__main__":
    main()
