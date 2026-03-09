"""Question 19(A)
Print the prime factors of an integer.
"""


def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


num = int(input("Enter an integer: "))
result = prime_factors(num)
print(f"Prime factors of {num}: {result}")
