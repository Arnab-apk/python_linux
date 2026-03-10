"""2. Product Using Recursion - Find product of two numbers"""

def product(a, b):
    """Find product using recursion without multiplication operator"""
    if b == 0:
        return 0
    elif b > 0:
        return a + product(a, b - 1)
    else:
        return -product(a, -b)

num1 = 5
num2 = 4

result = product(num1, num2)
print(f"Product of {num1} and {num2} = {result}")
