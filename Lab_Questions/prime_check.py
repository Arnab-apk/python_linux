"""Question 11(B)
Check whether a number is a prime number or not.
"""

num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    print(f"{num} is {'a prime' if is_prime else 'not a prime'} number")
