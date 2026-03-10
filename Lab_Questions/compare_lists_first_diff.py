"""Compare equal-sized lists and print first index where they differ."""

L1 = list(map(int, input("Enter first list elements separated by space: ").split()))
L2 = list(map(int, input("Enter second list elements separated by space: ").split()))

if len(L1) != len(L2):
    print("Lists are not of equal size")
else:
    mismatch_index = -1
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            mismatch_index = i
            break

    if mismatch_index == -1:
        print("Both lists are equal")
    else:
        print(f"First mismatch at index {mismatch_index}: {L1[mismatch_index]} != {L2[mismatch_index]}")
