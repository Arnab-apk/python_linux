"""Compare equal-sized lists and print first index where they differ."""

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 9, 4, 5]

print(f"List 1: {L1}")
print(f"List 2: {L2}")

for i in range(len(L1)):
    if L1[i] != L2[i]:
        print(f"First difference at index {i}: {L1[i]} != {L2[i]}")
        break
else:
    print("Lists are identical")
