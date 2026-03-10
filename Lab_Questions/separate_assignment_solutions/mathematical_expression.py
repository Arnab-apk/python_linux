"""Evaluate the mathematical expression: ((X-x^2)/2!)+(X^3+3!)-(x^4/4!)"""

import math

x = float(input("Enter value of x: "))

term1 = (x - x**2) / math.factorial(2)
term2 = (x**3 + math.factorial(3))
term3 = x**4 / math.factorial(4)

result = term1 + term2 - term3

print(f"Expression: ((x - x^2)/2!) + (x^3 + 3!) - (x^4/4!)")
print(f"x = {x}")
print(f"Term 1: (x - x^2)/2! = {term1}")
print(f"Term 2: x^3 + 3! = {term2}")
print(f"Term 3: x^4/4! = {term3}")
print(f"Result = {result}")
