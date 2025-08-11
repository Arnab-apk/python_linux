# Example list
lst = [1, 2, 3, 4, 5]

# Get length
n = len(lst)

# Swap elements from both ends
for i in range(n // 2):
    lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]

print("Reversed list:", lst)
