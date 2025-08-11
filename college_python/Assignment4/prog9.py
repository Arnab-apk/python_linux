def search_number(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i  # Return the index where it's found
    return -1  # Not found

# Example usage
numbers = [10, 20, 30, 40, 50]
target = int(input("Enter number to search: "))

index = search_number(numbers, target)

if index != -1:
    print(f"Number found at index {index}")
else:
    print("Number not found in the list")
