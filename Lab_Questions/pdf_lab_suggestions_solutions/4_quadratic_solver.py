"""4. Quadratic Equation Solver - Find roots of ax^2 + bx + c = 0"""

import math

a = 1
b = -5
c = 6

print(f"Equation: {a}x^2 + {b}x + {c} = 0\n")

if a == 0:
    print("Not a quadratic equation (a cannot be 0)")
else:
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Roots are real and distinct:")
        print(f"Root 1 = {root1}")
        print(f"Root 2 = {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"Roots are real and equal: {root}")
    else:
        print("Roots are complex (imaginary)")
