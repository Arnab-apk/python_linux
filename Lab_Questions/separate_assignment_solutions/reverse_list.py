"""Reverse a list."""
item=list(map(int, input("Enter no of elements ").split()))
reversed_items = item[::-1]
print(f"Original list: {item}")
print(f"Reversed list: {reversed_items}")
