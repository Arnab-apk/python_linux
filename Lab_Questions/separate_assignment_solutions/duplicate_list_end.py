"""Duplicate the value at the end of the list."""

items = list(map(int, input("Enter list elements separated by space: ").split()))

if len(items) == 0:
    print("List is empty. Cannot duplicate.")
else:
    last_value = items[-1]
    items.append(last_value)
    
    print(f"Original list: {items[:-1]}")
    print(f"Last value: {last_value}")
    print(f"List after duplication: {items}")
