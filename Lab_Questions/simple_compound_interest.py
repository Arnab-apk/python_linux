"""Question 13(B)
Calculate the amount payable after simple and compound interest.
"""

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter time period (in years): "))

si = (p * t * r) / 100
si_total = p + si

ci = p * ((1 + r / 100) ** t - 1)
ci_total = p + ci

print(f"Simple Interest: {si}")
print(f"Amount after Simple Interest: {si_total}")
print(f"Compound Interest: {ci:.2f}")
print(f"Amount after Compound Interest: {ci_total:.2f}")
