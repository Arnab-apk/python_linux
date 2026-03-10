"""Read a list and print it in reverse order."""

items = input("Enter list elements separated by space: ").split()
reversed_items = items[::-1]

print("Original list:", items)
print("Reversed list:", reversed_items)
