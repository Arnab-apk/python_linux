"""Simple calculator using user input."""

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("Division by zero is not allowed")
        raise SystemExit(1)
    result = a / b
else:
    print("Invalid operator")
    raise SystemExit(1)

print(f"Result = {result}")
