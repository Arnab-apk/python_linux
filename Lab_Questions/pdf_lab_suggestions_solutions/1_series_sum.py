"""1. Series Sum - Calculate sum of series for a given x"""

x = 2
n = 5

# Series: x + x^2 + x^3 + ... + x^n
series_sum = 0
for i in range(1, n + 1):
    series_sum += x ** i

print(f"Series: x + x^2 + x^3 + ... + x^{n}")
print(f"x = {x}, n = {n}")
print(f"Sum = {series_sum}")
