input = "SAMXABCDEF"
for i in range(len(input)):
    stop_val = i - len("xmas")
    print(input[i : stop_val if stop_val > 0 else None : -1])
