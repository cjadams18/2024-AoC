import re
from collections import Counter
from pathlib import Path


def read_input():
    parent_dir = Path(__file__).resolve().parent
    with open(parent_dir / "input.txt", "r") as file:
        line_split_regex = r"(\d{5})\s+(\d{5})"
        left, right = [], []
        for line in file:
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
    # right_dict = {}
    # for i in range(5):
    #     if right_dict.get(right[i]) is None:
    #         right_dict[right[i]] = 1
    #     else:
    #         right_dict[right[i]] += 1
    # similarity_score = 0
    # for i in range(5):
    #     num_right_occur = right_dict.get(left[i])
    #     if num_right_occur is None:
    #         continue
    #     else:
    #         similarity_score += int(left[i]) * int(num_right_occur)
    # return similarity_score
    right_counter = Counter(right)
    similarity_score = sum(
        int(l) * right_counter[l] for l in left if l in right_counter
    )
    return similarity_score


def main():
    left, right = read_input()
    part_one_result = part_one(left, right)
    part_two_result = part_two(left, right)
    print(f"Part One: {part_one_result}\nPart Two: {part_two_result}")


if __name__ == "__main__":
    main()