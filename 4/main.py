import argparse
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


# 2018 too low
def part_one(input: List[str]) -> int:
    total = 0
    height = len(input)
    width = len(input[0])
    arr = [[char if char in "XMAS" else "" for char in line] for line in input]
    for i, line in enumerate(arr):
        for j in range(len(line)):
            if j + len("XMAS") < width and "".join(line[j : j + len("XMAS")]) == "XMAS":
                print("found XMAS horizontal forward")
                total += 1
            if (
                j - len("XMAS") >= 0
                and "".join(
                    line[j : j - len("XMAS") if j - len("XMAS") > 0 else None : -1]
                )
                == "XMAS"
            ):
                print("found XMAS horizontal reverse")
                total += 1
            elif (
                i + len("XMAS") < height
                and f"{line[j]}{arr[i+1][j]}{arr[i+2][j]}{arr[i+3][j]}" == "XMAS"
            ):
                print("found XMAS vertical down")
                total += 1
            elif (
                i - len("XMAS") >= 0
                and "".join([arr[i - 1][j], arr[i - 2][j], arr[i - 3][j], line[j]])
                == "XMAS"
            ):
                print("found XMAS vertical up")
                total += 1
            elif (
                i + len("XMAS") < height
                and j + len("XMAS") < width
                and f"{line[j]}{arr[i+1][j+1]}{arr[i+2][j+2]}{arr[i+3][j+3]}" == "XMAS"
            ):
                print("found XMAS diagonal down right")
                total += 1
            elif (
                i - len("XMAS") >= 0
                and j + len("XMAS") < width
                and f"{line[j]}{arr[i-1][j+1]}{arr[i-2][j+2]}{arr[i-3][j+3]}" == "XMAS"
            ):
                print("found XMAS diagonal up right")
                total += 1
            elif (
                i + len("XMAS") < height
                and j - len("XMAS") >= 0
                and f"{line[j]}{arr[i+1][j-1]}{arr[i+2][j-2]}{arr[i+3][j-3]}" == "XMAS"
            ):
                print("found XMAS diagonal down left")
                total += 1
            elif (
                i - len("XMAS") >= 0
                and j - len("XMAS") >= 0
                and f"{line[j]}{arr[i-1][j-1]}{arr[i-2][j-2]}{arr[i-3][j-3]}" == "XMAS"
            ):
                print("found XMAS diagonal up left")
                total += 1
    return total


def part_two(input: List[str]) -> int:
    return 0


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
