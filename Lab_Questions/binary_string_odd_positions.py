"""Question 20(A)
Check if a string is a binary string. If yes, display elements at all odd positions
(1-indexed). Example: Input 01010101011 -> Output 000001
"""

s = input("Enter a string: ")

if all(c in "01" for c in s):
    # Odd positions (1-indexed): positions 1, 3, 5, ... -> indices 0, 2, 4, ...
    odd_pos = "".join(s[i] for i in range(0, len(s), 2))
    print(odd_pos)
else:
    print("Not a binary string")
