def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56]
target = 23
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
