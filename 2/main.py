import re
from pathlib import Path


def read_input():
    parent_dir = Path(__file__).resolve().parent
    with open(parent_dir / "input2.txt", "r") as file:
        return file.readlines()


def same_direction(input):
    asc = input[0] < input[1]
    for i in range(len(input) - 1):
        if asc and input[i] > input[i + 1]:
            return False
        elif not asc and input[i] < input[i + 1]:
            return False
    return True


def is_safe_report(report):
    if not same_direction(report):
        return False
    for i in range(len(report) - 1):
        diff = abs(int(report[i]) - int(report[i + 1])) 
        if diff < 1 or diff > 3:
            return False
    return True


def part_one(input):
    pattern = r"(\d+)"
    num_safe_reports = 0
    for line in input:
        match = re.findall(pattern, line)
        print(match)
        if match is None:
            print("No match found")
            continue
        result = is_safe_report(match)
        print(result)
        if result:
            num_safe_reports += 1
    return num_safe_reports
                


def main():
    input = read_input()
    part_one_result = part_one(input)
    print(f"Part One: {part_one_result}")


if __name__ == "__main__":
    main()
