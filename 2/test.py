import re


def same_direction(input):
    asc = input[0] < input[1]
    for i in range(len(input) - 1):
        if asc and input[i] > input[i + 1]:
            return False
        elif not asc and input[i] < input[i + 1]:
            return False
    return True


input = [45, 67, 89, 34]
input2 = [45, 67, 89, 90]
input3 = [45, 40, 33, 36]
input4 = [12, 40, 33, 12]
print(same_direction(input))
print(same_direction(input2))
print(same_direction(input3))
print(same_direction(input4))
