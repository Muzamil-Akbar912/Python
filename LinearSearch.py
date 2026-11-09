nums = [1, 3, 12, 14, 4, 10, 13, 18, 33]

x = 10
idx = 0

for val in nums:
    if(val == x):
        print(f"{x} found at index {idx}")
        break
    idx += 1