"""Question 19(B)
Find all roots of a quadratic equation ax^2 + bx + c = 0 for all possible
combinations of a, b and c (real roots, repeated roots, complex roots, linear case).
"""

import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    if b == 0:
        print("Not a valid equation")
    else:
        root = -c / b
        print(f"Linear equation. Root: {root}")
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        r1 = (-b + discriminant ** 0.5) / (2 * a)
        r2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f"Two distinct real roots: {r1} and {r2}")
    elif discriminant == 0:
        r = -b / (2 * a)
        print(f"One repeated real root: {r}")
    else:
        r1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        r2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"Two complex roots: {r1} and {r2}")
