# Example list
lst = [1, 3, 2, 3, 4, 1, 5, 2, 1]

seen = set()
unique_part = []
duplicates = []

for item in lst:
    if item not in seen:
        seen.add(item)
        unique_part.append(item)
    else:
        duplicates.append(item)

# Combine unique values first, duplicates later
result = unique_part + duplicates

print("Original list:", lst)
print("Rearranged list:", result)

