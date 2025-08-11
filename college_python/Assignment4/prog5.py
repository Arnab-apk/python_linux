# Example list
lst = [12, 45, 7, 23, 56, 89, 34, 2, 77, 15]

# Input range
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

# Validate range
if 0 <= start <= end < len(lst):
    # Slice the list in the given range (inclusive of start, inclusive of end)
    sub_list = lst[start:end+1]
    
    # Find max and min
    max_val = max(sub_list)
    min_val = min(sub_list)
    
    print(f"List in the specified range: {sub_list}")
    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")
else:
    print("Invalid index range!")
