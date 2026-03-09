"""Question 21(B)
Sum the sequence 2/6 + 6/13 + 8/17 + ... up to n terms.

Pattern derived from the given terms:
  Numerators:   2, 6, 8, 12, 14, ... (alternating +4 and +2)
  Denominators: 6, 13, 17, 24, 28, ... (alternating +7 and +4)
"""

n = int(input("Enter number of terms: "))

num = 2
den = 6
total = 0

for i in range(n):
    print(f"Term {i + 1}: {num}/{den} = {num / den:.4f}")
    total += num / den
    if i % 2 == 0:
        num += 4
        den += 7
    else:
        num += 2
        den += 4

print(f"\nSum up to {n} terms: {total:.4f}")
